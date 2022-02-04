$(document).ready(function() {

  $('#boton2').on('click', function() {

      //El metodo .modal(), se utiliza para abrir la ventana modal de bootstrap 4
      $('#modal-date').modal();
  })

  $('.fj-date1').datepicker({
      language: "es",
      todayBtn: "linked",
      clearBtn: true,
      format: "dd/mm/yyyy",
      multidate: false,
      todayHighlight: true

  });

  $('.fj-date1').datepicker({
      language: "es",
      todayBtn: "linked",
      clearBtn: true,
      format: "dd/mm/yyyy",
      multidate: false,
      todayHighlight: true

  });

})