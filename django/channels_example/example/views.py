from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
# from .models import TEST, TEST1, SOURCEMILKPROCESSINFO,SOURCEBOTTLEINFO,SOURCECOWSFARM,SOURCECOWSENVIRONMENT1,SOURCECOWSINFO,INDOORDEPOTINFO,INDOORMILKPRODUCTINFO,LOGISTICMILKPRODUCTINFO,LOGISTICCARINFO,LOGISTICDRIVERSINFO,LOGISTICTERMINALINFO,SOURCESALE
from .models import TEST, TEST1, TEST2, TEST3, TEST4


def ajax_dict(request):
    if request.is_ajax():
        datepick = request.GET.get('datepick')
        tname = request.GET.get('tname')
        # print(tname)
        # print(datepick)
        # try:
        #     num = 0
        #     dict = {}
        #     if tname == 'test':
        #         info = TEST.objects.filter(TIM__contains=datepick)
        #     elif tname == 'test1':
        #         info = TEST1.objects.filter(TIM__contains=datepick)
        #     for i in info:
        #         date = "date" + str(num)
        #         tem = "tem" + str(num)
        #         hum = "hum" + str(num)
        #
        #         dict[date] = i.TIM
        #         dict[tem] = i.TEM
        #         dict[hum] = i.HUM
        #         num+=1
        # except:
        #     dict = {'error': 'error'}
        num = 0
        dict = {}
        info = []
        if tname == 'test':
            try:
                info = TEST.objects.filter(TIM__contains=datepick)
                # print(info)
            except:
                info = []
        elif tname == 'test1':
            try:
                info = TEST1.objects.filter(TIM__contains=datepick)
            except:
                info = []
        elif tname == 'test2':
            try:
                info = TEST2.objects.filter(TIM__contains=datepick)
            except:
                info = []
        elif tname == 'test3':
            try:
                info = TEST3.objects.filter(TIM__contains=datepick)
            except:
                info = []
        elif tname == 'test4':
            try:
                info = TEST4.objects.filter(TIM__contains=datepick)
            except:
                info = []

        if len(info) == 0:
            dict = {'date0':'无数据', 'tem0':'无数据', 'hum0':'无数据', 'count': 1}
        else:
            for i in info:
                date = "date" + str(num)
                tem = "tem" + str(num)
                hum = "hum" + str(num)

                dict[date] = i.TIM
                dict[tem] = i.TEM
                dict[hum] = i.HUM
                num += 1
            dict['count'] = num
    return JsonResponse(dict)


def index(request):
    return render(request, 'main.html')


# def source(request):
#     settings.Q = request.GET.get('q')
#     # print(settings.Q)
#     return render(request, 'source.html')
#
#
# def attention(request):
#     return render(request, 'attention.html')


# def grass(request):
#     try:
#         # print(settings.Q)
#         # a_list = SOURCECOWSFARM.objects.get(TAGEPC='000000210426DDD800000000')
#         # b_list = SOURCECOWSENVIRONMENT1.objects.get(TAGEPC='000000210426DDD800000000')
#         # c_list = SOURCECOWSINFO.objects.get(TAGEPC='000000210426DDD800000000')
#         # print(a_list)
#     except:
#         settings.Q = None
#         a_list = None
#         b_list = None
#         c_list = None
#         print('2')
#     return render(request, 'grass.html', {'q': settings.Q, 'a_list': a_list, 'b_list': b_list, 'c_list': c_list})


# def factory(request):
#     try:
#         # d_list = SOURCEMILKPROCESSINFO.objects.get(TAGEPC=str(settings.Q))
#         # e_list = SOURCEBOTTLEINFO.objects.get(TAGEPC=str(settings.Q))
#     except:
#         settings.Q = None
#         d_list = None
#         e_list = None
#     return render(request, 'factory.html', {'q': settings.Q, 'd_list': d_list, 'e_list': e_list})


# def storage(request):
#     try:
#         print(settings.Q)
#         f_list = INDOORDEPOTINFO.objects.get(DEPOTLOC='2')
#         g_list = None
#         # print('1')
#         # settings.Q = 2
#         # g_list = INDOORMILKPRODUCTINFO.objects.get(TAGEPC=str(settings.Q))
#     except ObjectDoesNotExist:
#         print('2')
#         settings.Q = None
#         f_list = None
#         g_list = None
#     return render(request, 'storage.html', {'q': settings.Q, 'f_list': f_list, 'g_list': g_list})


# def logistic(request):
#     try:
#         # h_list = LOGISTICMILKPRODUCTINFO.objects.get(TAGEPC=str(settings.Q))
#         # i_list = LOGISTICCARINFO.objects.get(TAGEPC=str(settings.Q))
#         # j_list = LOGISTICDRIVERSINFO.objects.get(TAGEPC=str(settings.Q))
#         # k_list = LOGISTICTERMINALINFO.objects.get(TAGEPC=str(settings.Q))
#     except:
#         settings.Q = None
#         h_list = None
#         i_list = None
#         j_list = None
#         k_list = None
#     return render(request, 'logistic.html', {'q': settings.Q, 'h_list': h_list, 'i_list': i_list, 'j_list': j_list, 'k_list': k_list})
#
#
# def sale(request):
#     try:
#         # l_list = SOURCESALE.objects.get(TAGEPC=str(settings.Q))
#     except:
#         settings.Q = None
#         l_list = None
#     return render(request, 'sale.html', {'q': settings.Q, 'l_list':l_list})
