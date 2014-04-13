/**
 * Created by roberto on 4/10/14.
 */


$(document).ready(function(){
    $('.btnClick').on('click', handleClick);
});

function showData(data){
    $('.resultado').attr('value',data.formValues);
    //org.maniacSoft.ajaxcall.hideMessage();
}

function callMessage(){
    org.maniacSoft.ajaxcall.showMessage();
}

function handleClick(e){
    $.ajax('/index.html', {type:'GET',
        data: {fmt:'json', formValues: $('.txtData').val()},
        success: showData,
        beforeSend: callMessage
    });
}
