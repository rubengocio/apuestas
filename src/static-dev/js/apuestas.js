function open_modal_register(){
    $('#modal_register').modal('show');
}

function cancel_modal_register(){
    $('#modal_register').find('#id_username').val('');
    $('#modal_register').find('#id_password1').val('');
    $('#modal_register').find('#id_password2').val('');
    $('#modal_register').modal('hide');
}

function send_register_form(){
    $.ajax({
        type: "POST",
        url: $('#id_form_register').attr('action'),
        data: $('#id_form_register').serialize(),
        success: function(response){
            alert(response)
        }
    })
}