/**
 * Created by roberto on 4/12/14.
 */

$(document).ready(function (){
    $('#btnLogin').on('click', handleClickLogin);
});


function handleClickLogin(e){
    $.ajax('/login.html', {type:'GET',
        data: {fmt:'json', usuario:'maniac787', clave: 'qwe123'},
        success: succesEventLogin,
        beforeSend: callMessage
    }).done(doneEvent);

}


function callMessage(){
    org.maniacSoft.messages.showMessage();
}

function doneEvent(data){
    alert('done');
}
function succesEventLogin(data){
    alert('s');
}