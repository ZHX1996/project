var tname = '';
  $.ajaxSetup({
  data: {csrfmiddlewaretoken: '{{ csrf_token }}' }
  });
socket = new WebSocket("ws://127.0.0.1:8000/channels_example/");
$(document).ready(function(){
    setInterval(function(){
    var now= new Date();
    var year=now.getFullYear();
    var month=now.getMonth();
    var date=now.getDate();
    var h=now.getHours();
    var minute=now.getMinutes();
    var s=now.getSeconds();
    var w=now.getDay();
    if (w == 5) w=("星期五");
    if (w == 6) w=("星期六");
    if (w == 0) w=("星期日");
    if (w == 1) w=("星期一");
    if (w == 2) w=("星期二");
    if (w == 3) w=("星期三");
    if (w == 4) w=("星期四");
    document.getElementById("showtime").innerHTML=year+"年"+(month+1)+"月"+date+"日"+" "+h+":"+minute+":"+s+" "+w;
    document.getElementById("date1").setAttribute('value', year+"-"+(month+1)+"-"+date);
    }, 1000);

    var k = 0;
    $('.divtab').hide();
    $('.lip').removeClass('active');
    $('#lip1').toggle();
    $('.lip_1').addClass('active');
    setInterval(function(){
        a(k);
        k = (k+1)%5;
    }, 5000);
    function a(i){
        if(i==0)
        {
            $('.divtab').hide();
            $('.lip').removeClass('active');
            $('#lip2').toggle();
            $('.lip_2').addClass('active');
        }
        if(i==1)
        {
            $('.divtab').hide();
            $('.lip').removeClass('active');
            $('#lip3').toggle();
            $('.lip_3').addClass('active');
        }
        if(i==2)
        {
            $('.divtab').hide();
            $('.lip').removeClass('active');
            $('#lip4').toggle();
            $('.lip_4').addClass('active');
        }
        if(i==3)
        {
            $('.divtab').hide();
            $('.lip').removeClass('active');
            $('#lip5').toggle();
            $('.lip_5').addClass('active');
        }
        if(i==4)
        {
            $('.divtab').hide();
            $('.lip').removeClass('active');
            $('#lip1').toggle();
            $('.lip_1').addClass('active');
        }
    }

    setInterval(function(){socket.send("hello")}, 10000);

    $('.theme-login').click(function(){
        tname=$(this).parent().attr('id');
        $('.theme-popover-mask').fadeIn(100);
        $('.theme-popover').slideDown(200);
    });
    $('.theme-poptit .close').click(function(){
        document.getElementById('dict_result').innerHTML = "<thead><th>时间</th><th>温度</th><th>湿度</th></thead> <tbody></tbody>";
        $('.theme-popover-mask').fadeOut(100);
        $('.theme-popover').slideUp(200);
    });
    $('#date').click(function() {
        document.getElementById('dict_result').innerHTML = "<thead><th>时间</th><th>温度</th><th>湿度</th></thead> <tbody></tbody>";
        var datepick = document.getElementById('date1');
        var tab_result = document.getElementById("dict_result");
        var tBodies_result = tab_result.tBodies;
        var tbody_result = tBodies_result[0];
        $.getJSON('/ajax_dict/', {'tname': tname, 'datepick': datepick.value}, function (ret) {
            for (i = 0; i < ret['count']; i++) {
                var tr = tbody_result.insertRow(0);
                var td_1 = tr.insertCell(0);
                td_1.innerHTML = ret['date'.concat(String(i))];
                var td_2 = tr.insertCell(1);
                td_2.innerHTML = ret['tem'.concat(String(i))];
                var td_3 = tr.insertCell(2);
                td_3.innerHTML = ret['hum'.concat(String(i))];
            }
        });
    })

    // $(".lip").click(function(){
    //     $('.lip').removeClass('active');
    //     $(this).addClass("active");
    // });
    // $('.lip_1').addClass("active");

    // $('.lip_1').click(function(){
    //     $('#lip1').css('display','block');
    //     $('#lip2').css('display','none');
    //     $('#lip3').css('display','none');
    //     $('#lip4').css('display','none');
    //     $('#lip5').css('display','none');
    // });
    // $('#link-lip2').click(function(){
    //     $('#lip1').css('display','none');
    //     $('#lip2').css('display','block');
    //     $('#lip3').css('display','none');
    //     $('#lip4').css('display','none');
    //     $('#lip5').css('display','none');
    // });
    // $('#link-lip3').click(function(){
    //     $('#lip1').css('display','none');
    //     $('#lip2').css('display','none');
    //     $('#lip3').css('display','block');
    //     $('#lip4').css('display','none');
    //     $('#lip5').css('display','none');
    // });
    // $('#link-lip4').click(function(){
    //     $('#lip1').css('display','none');
    //     $('#lip2').css('display','none');
    //     $('#lip3').css('display','none');
    //     $('#lip4').css('display','block');
    //     $('#lip5').css('display','none');
    // });
    // $('#link-lip5').click(function(){
    //     $('#lip1').css('display','none');
    //     $('#lip2').css('display','none');
    //     $('#lip3').css('display','none');
    //     $('#lip4').css('display','none');
    //     $('#lip5').css('display','block');
    // });
});

// socket = new ReconnectingWebSocket("ws://127.0.0.1:8000/channels_example/")
socket.onmessage = function(e){
    var data = JSON.parse(e.data);

    var tab1=document.getElementById("tab1");
    var tBodies1 = tab1.tBodies;
    var tbody1 = tBodies1[0];

    if(tab1.rows.length == 1 || tab1.rows[1].cells[0].innerHTML != data.time1)
    {
        // alert(tab1.rows[1].cells[0].innerHTML);
        var tr1 = tbody1.insertRow(0);
        var td_11 = tr1.insertCell(0);
        td_11.innerHTML = data.time1;
        var td_21 = tr1.insertCell(1);
        td_21.innerHTML = data.tem1;
        var td_31 = tr1.insertCell(2);
        td_31.innerHTML = data.hum1;
    }

    var tab2=document.getElementById("tab2");
    var tBodies2 = tab2.tBodies;
    var tbody2 = tBodies2[0];

    if(tab2.rows.length == 1 || tab2.rows[1].cells[0].innerHTML != data.time2)
    {
        var tr2 = tbody2.insertRow(0);
        var td_12 = tr2.insertCell(0);
        td_12.innerHTML = data.time2;
        var td_22 = tr2.insertCell(1);
        td_22.innerHTML = data.tem2;
        var td_32 = tr2.insertCell(2);
        td_32.innerHTML = data.hum2;
    }

    var tab3=document.getElementById("tab3");
    var tBodies3 = tab3.tBodies;
    var tbody3 = tBodies3[0];

    if(tab3.rows.length == 1 || tab3.rows[1].cells[0].innerHTML != data.time3)
    {
        var tr3 = tbody3.insertRow(0);
        var td_13 = tr3.insertCell(0);
        td_13.innerHTML = data.time3;
        var td_23 = tr3.insertCell(1);
        td_23.innerHTML = data.tem3;
        var td_33 = tr3.insertCell(2);
        td_33.innerHTML = data.hum3;
    }

    var tab4=document.getElementById("tab4");
    var tBodies4 = tab4.tBodies;
    var tbody4 = tBodies4[0];

    if(tab4.rows.length == 1 || tab4.rows[1].cells[0].innerHTML != data.time4)
    {
        var tr4 = tbody4.insertRow(0);
        var td_14 = tr4.insertCell(0);
        td_14.innerHTML = data.time4;
        var td_24 = tr4.insertCell(1);
        td_24.innerHTML = data.tem4;
        var td_34 = tr4.insertCell(2);
        td_34.innerHTML = data.hum4;
    }

    var tab5=document.getElementById("tab5");
    var tBodies5 = tab5.tBodies;
    var tbody5 = tBodies5[0];

    if(tab5.rows.length == 1 || tab5.rows[1].cells[0].innerHTML != data.time5) {
        var tr5 = tbody5.insertRow(0);
        var td_15 = tr5.insertCell(0);
        td_15.innerHTML = data.time5;
        var td_25 = tr5.insertCell(1);
        td_25.innerHTML = data.tem5;
        var td_35 = tr5.insertCell(2);
        td_35.innerHTML = data.hum5;
    }

    if(tbody1.rows.length>=5) tbody1.deleteRow(5);
    if(tbody2.rows.length>=5) tbody2.deleteRow(5);
    if(tbody3.rows.length>=5) tbody3.deleteRow(5);
    if(tbody4.rows.length>=5) tbody4.deleteRow(5);
    if(tbody5.rows.length>=5) tbody5.deleteRow(5);

    // tab.rows[1].cells[1].innerHTML=data.time1;
    // tab.rows[1].cells[2].innerHTML=data.tem1;
    // tab.rows[1].cells[3].innerHTML=data.hum1;
    //
    // tab.rows[2].cells[1].innerHTML=data.time2;
    // tab.rows[2].cells[2].innerHTML=data.tem2;
    // tab.rows[2].cells[3].innerHTML=data.hum2;
    //
    // tab.rows[3].cells[1].innerHTML=data.time3;
    // tab.rows[3].cells[2].innerHTML=data.tem3;
    // tab.rows[3].cells[3].innerHTML=data.hum3;
    //
    // tab.rows[4].cells[1].innerHTML=data.time4;
    // tab.rows[4].cells[2].innerHTML=data.tem4;
    // tab.rows[4].cells[3].innerHTML=data.hum4;
    //
    // tab.rows[5].cells[1].innerHTML=data.time5;
    // tab.rows[5].cells[2].innerHTML=data.tem5;
    // tab.rows[5].cells[3].innerHTML=data.hum5;
    // setInterval(function(){socket.send("hello")}, 250000);
    // setInterval(function(){alert('123')}, 250000);
    // socket.send("hello");
};
socket.onopen = function(){
    socket.send("hello");
};
if (socket.readyState == WebSocket.OPEN) socket.onopen();