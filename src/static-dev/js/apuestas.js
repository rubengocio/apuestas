function open_modal_register(){
    $('#modal_register').modal('show');
}

function cancel_modal_register(){
    clear_form();
    $.each($('#id_form_register').find('input'), function(index, objects_i){
      $(objects_i).val('');
    });
    $('#modal_register').modal('hide');
}

function clear_form(){
  $.each($('#id_form_register').find('input'), function(index, objects_i){
    $(objects_i).removeClass('is-invalid');
    $(objects_i).removeAttr('data-toggle','tooltip');
    $(objects_i).removeAttr('data-placement','right');
    $(objects_i).removeAttr('title',objects_i[1]);
    $(objects_i).tooltip('dispose');
  });
}

function send_register_form(){
  $.each($('.is-invalid'), function(index, objects_i){
    $(objects_i).removeClass('is-invalid');
  });
  $.ajax({
    type: "POST",
    url: $('#id_form_register').attr('action'),
    data: $('#id_form_register').serialize(),
    success: function(response){
      if(response.status == 'ok'){
          alert('Felicitaciones!');
          cancel_modal_register();
      }else{
         $.each(response.errors, function(index, objects_i){
           $('#id_' + objects_i[0]).addClass('is-invalid');
           $('#id_' + objects_i[0]).attr('data-toggle','tooltip');
           $('#id_' + objects_i[0]).attr('data-placement','right');
           $('#id_' + objects_i[0]).attr('title',objects_i[1]);
           $('#id_' + objects_i[0]).tooltip('show');
         });
      }
    }
  })
}
