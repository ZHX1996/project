from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from wechatpy.utils import check_signature  
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message, create_reply
from wechatpy.replies import BaseReply

import urllib.request
import json
# Create your views here.
TOKEN = 'ZHX1996'
appId = 'wx9ed3c52bf21b0684'
appSecret = '0eaac207a935e00aac6b22de95c7268d'

@csrf_exempt
def verify(request):
    if request.method == 'GET':
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        try:  
            check_signature(TOKEN, signature, timestamp, nonce)  
        except InvalidSignatureException:  
            echostr = 'error'        
        response = HttpResponse(echostr, content_type="text/plain")
        return response
    else:     
        msg = parse_message(request.body)       
        if msg.type == 'text':
            reply = create_reply(u'文本消息:' + msg.content, msg)
            
        elif msg.type == 'image':
            URL = msg.image
            articles = [
                        {
                         'title': '图片消息',
                         'description': '图片为',
                         'image': URL,
                         'url': URL
                         },                         
                        ]
            reply = create_reply(articles, msg)
            
        else:
            reply = create_reply(msg.type, msg)
            
    if not reply or not isinstance(reply, BaseReply):
        reply = create_reply('暂不支持其他操作', msg)
    
    response = HttpResponse(reply.render(), content_type = "application/xml")
    return response

        
        

