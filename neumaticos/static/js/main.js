(function ($) {
    "use strict";

    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }


})(jQuery);

function modificarVehiculo(){
  var vehiculo = $("#vehiculos").val();
  if(vehiculo == 0){
    window.alert("Debes seleccionar una vehículo para modificar.");
  }else{
    window.location.href = "modificarVehiculo/"+vehiculo;
  }
}
function confirmarEliminarVehiculo(){
  var vehiculo = $("#vehiculos").val();
  if(vehiculo == 0){
    window.alert("Debes seleccionar un vehiculo para eliminar.");
  }else{
    var confirm = window.confirm("Desea eliminar el vehiculo con matrícula"+vehiculo+"?");
    if (confirm) {
      window.location.href = "eliminarVehiculo/"+vehiculo;
    }
  }
}
function modificarEmpresa(){
  var empresa = $("#empresas").val();
  if(empresa == 0){
    window.alert("Debes seleccionar una empresa para modificar.");
  }else{
    window.location.href = "modificarEmpresa/"+empresa;
  }
}
function confirmarEliminarEmpresa(){
  var empresa = $("#empresas").val();
  if(empresa == 0){
    window.alert("Debes seleccionar una empresa para eliminar.");
  }else{
    var confirm = window.confirm("Desea eliminar la mepresa con RUT "+empresa+"?");
    if (confirm) {
      window.location.href = "eliminarEmpresa/"+empresa;
    }
  }
}
function verDetallesVehiculo(){
  var vehiculo = $("#vehiculos").val();
  if(vehiculo == 0){
    window.alert("Debes seleccionar una vehiculo.");
  }else{
      window.location.href = "detallesVehiculo/"+vehiculo;
  }
}


function modificarNeumatico(){
  var neumatico = $("#neumaticos").val();
  if(neumatico == 0){
    window.alert("Debes seleccionar un neumatico para modificar.");
  }else{
    window.location.href = "modificarNeumatico/"+neumatico;
  }
}
function confirmarEliminarNeumatico(){
  var neumatico = $("#neumaticos").val();
  if(neumatico == 0){
    window.alert("Debes seleccionar un neumatico para eliminar.");
  }else{
    var confirm = window.confirm("Desea eliminar el naumatico con RUT "+neumatico+"?");
    if (confirm) {
      window.location.href = "eliminarNeumatico/"+neumatico;
    }
  }
}
function filtrarNeumaticos(vehiculo){
  var xhttp = new XMLHttpRequest();
 xhttp.onreadystatechange = function() {
   if (this.readyState == 4 && this.status == 200) {
     var neumaticos = JSON.parse(this.responseText);

      var selectNeumaticos = document.getElementById("neumaticos");
      var largo = selectNeumaticos.length;
      for (var i = 0; i < largo; i++) {
         selectNeumaticos.remove(0);
       }
       for(var i=1;i<= Object.keys(neumaticos).length;i++){
         var option = document.createElement("option");
         option.text = neumaticos[i];
         selectNeumaticos.add(option,neumaticos[i]);
       }
   }
 };
 xhttp.open("GET", "filtrarNeumaticos/"+vehiculo, true);
 xhttp.send();


}
