/**
 * Created by roberto on 4/13/14.
 */
var org = {};
org.maniacSoft = {};
org.maniacSoft.messages = {
    showMessage: function(htmlElement){
        $('#dialog-message').attr('title','Hola');
        $('#dialog-message').append(htmlElement);
        $( "#dialog-message" ).dialog({
            modal: true,
            buttons: {
                Ok: function() {
                    $( this ).dialog( "close" );
                }
            }
        });
    },

    hideMessage: function(){
        $( "#dialog-message" ).dialog( "close" );
    }
};


org.maniacSoft.ajaxcall = {
    showMessage: function(htmlElement){
        $('#dialog-message').attr('title','Wait');
        $('#dialog-message').append(htmlElement);
        $( "#dialog-message" ).dialog({
            modal: true
        });
    },

    hideMessage: function(){
        $( "#dialog-message" ).dialog( "close" );
    }
};