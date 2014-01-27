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
  var div_msg = document.getElementById('background-msg')
  div_msg.style.display = 'block';
  ajax_require('background-msg', "/create");
}

function remove_record(name, location){
  var div_msg = document.getElementById('background-msg')
  div_msg.style.display = 'block';
  var msg = '<p class="msg">Você deseja apagar o registro:<br/> <strong>Name:</strong> ' + name + '<br/><strong>Location:</strong> ' + location + '?<br/>' ;
  msg += '<input type="button" value="Sim" />';
  msg +=  '<input type="button" value="Não" onclick="close_msg()"/>';
  msg += '</p>';
  div_msg.innerHTML = msg
}

function edit_record(name, location){
  var div_msg = document.getElementById('background-msg')
  div_msg.style.display = 'block';
  ajax_require('background-msg', "/edit?q=" + name);
}

function close_msg(){
  var div_msg = document.getElementById('background-msg')
  div_msg.style.display = 'none';
}
