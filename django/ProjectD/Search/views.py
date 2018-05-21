from django.shortcuts import render
from .models import SOURCEMILKPROCESSINFO,SOURCEBOTTLEINFO,SOURCECOWSFARM,SOURCECOWSENVIRONMENT1,SOURCECOWSINFO,INDOORDEPOTINFO,INDOORMILKPRODUCTINFO,LOGISTICMILKPRODUCTINFO,LOGISTICCARINFO,LOGISTICDRIVERSINFO,LOGISTICTERMINALINFO,SOURCESALE
def index(request):
    epc = request.GET['epc']
    a_list = SOURCECOWSFARM.objects.get(TAGEPC = str(epc))
    b_list = SOURCECOWSENVIRONMENT1.objects.get(TAGEPC = str(epc))
    c_list = SOURCECOWSINFO.objects.get(TAGEPC = str(epc))
    d_list = SOURCEMILKPROCESSINFO.objects.get(TAGEPC = str(epc))
    e_list = SOURCEBOTTLEINFO.objects.get(TAGEPC = str(epc))
    f_list = INDOORDEPOTINFO.objects.get(TAGEPC = str(epc))
    g_list = INDOORMILKPRODUCTINFO.objects.get(TAGEPC = str(epc))
    h_list = LOGISTICMILKPRODUCTINFO.objects.get(TAGEPC = str(epc))
    i_list = LOGISTICCARINFO.objects.get(TAGEPC = str(epc))
    j_list = LOGISTICDRIVERSINFO.objects.get(TAGEPC = str(epc))
    k_list = LOGISTICTERMINALINFO.objects.get(TAGEPC = str(epc))
    l_list = SOURCESALE.objects.get(TAGEPC = str(epc))
    return render(request,'index.html',{'a_list':a_list,'b_list':b_list,'c_list':c_list,'d_list':d_list,'e_list':e_list,'f_list':f_list,'g_list':g_list,'h_list':h_list,'i_list':i_list,'j_list':j_list,'k_list':k_list,'l_list':l_list})