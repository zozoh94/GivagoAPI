from django.views.decorators.http import require_GET
from django.http import Http404, HttpResponseServerError, HttpResponse
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from decimal import Decimal
from decimal import InvalidOperation
from ipware.ip import get_ip
from django.conf import settings
import hashlib
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Sum

from .models import Survey

@require_GET
def survey_completed_view(request):       
    ip = get_ip(request)
    if(ip not in settings.PEANUTS_LAB_IPS):
        return  HttpResponseServerError('Your ip is not authorized.')

    offer_invitation_id = request.GET.get('offerInvitationId')
    if(offer_invitation_id is None):
        raise Http404("offerInvitationId not specified")
    
    oid_hash = request.GET.get('oidHash')
    if(oid_hash is None):
        raise Http404("oidHash not specified")

    if(hashlib.md5((offer_invitation_id+settings.PEANUTS_LAB_ACTFUND_APP_ID).encode('utf-8')).hexdigest() != oid_hash):
        return  HttpResponseServerError('Application hash is not good')

    transaction_id = request.GET.get('transactionId')
    if(transaction_id is None):
        raise Http404("transactionId not specified")
    
    txn_hash = request.GET.get('txnHash')
    if(txn_hash is None):
        raise Http404("txnHash not specified")

    if(hashlib.md5((transaction_id+settings.PEANUTS_LAB_ACTFUND_TRANSACTION_ID).encode('utf-8')).hexdigest() != txn_hash):
        return  HttpResponseServerError('Transaction hash is not good')
    
    user_id = None
    try:
        user_id = int(request.GET.get('endUserId'))
    except ValueError:
        raise Http404("endUserId is not a number")
    
    amount = request.GET.get('amt')

    survey = Survey()    
    
    user = None
    if(user_id and user_id != 0):
        try:
            user = get_user_model().objects.get(id=user_id)
        except get_user_model().DoesNotExist:
            raise Http404("User does not exist")
    survey.user = user
        
    if(amount):
        try:            
            survey.amount = Decimal(amount)
        except InvalidOperation:            
            return  HttpResponseServerError('Amount not well formated')
    else:
        raise Http404("Amount not specified")

    try:
        survey.save()
    except IntegrityError:
        return  HttpResponseServerError('Problem with the database.')

    return HttpResponse('1')

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def survey_total_amount_view(request):
    total = Survey.objects.all().aggregate(Sum('amount'))
    return Response({"total": total['amount__sum']})
