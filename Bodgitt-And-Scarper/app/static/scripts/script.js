function ajax_require(element, page){
  xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function(){
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
        document.getElementById(element).innerHTML = xmlhttp.responseText;
    }
  }
  xmlhttp.open("GET", page, true);
  xmlhttp.send();
}

function searchResult(str){
  ajax_require('table-body',"/search?q=" + str);
}

function addRecords(){
  var div_msg = document.getElementById('background-msg');
  div_msg.style.display = 'block';
  ajax_require('background-msg', "/create");
}

function verify_new_record(meta_data){
  var div_msg = document.getElementById('background-msg');
  div_msg.style.display = 'block';
  ajax_require('body', "/create-validation");
}

function remove_record(name, location, validate){

  if (validate) {
    ajax_require('background-msg', '/remove-validation?name=' + name + '&location=' + location)
  }else{
    var div_msg = document.getElementById('background-msg');
    div_msg.style.display = 'block';
    ajax_require('background-msg', '/remove?name=' + name + '&location=' + location);
  }
}

function edit_record(name, location){
  var div_msg = document.getElementById('background-msg');
  div_msg.style.display = 'block';
  ajax_require('background-msg', "/edit?name=" + name + '&location=' + location);
}

function close_msg(reload_page){
  var div_msg = document.getElementById('background-msg');
  div_msg.style.display = 'none';
  if (reload_page) {
    window.location.reload()
  }
}

function mask(evt, field){
  switch(field){
    case 'size':
    case 'owner':
      var charCode = (evt.which) ? evt.which : event.keyCode
      if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
      return true;
      break;
    case 'rate':
    break;
  }
}