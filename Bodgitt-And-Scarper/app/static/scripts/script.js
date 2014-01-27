function searchResult(str){
  xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange=function(){
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
        document.getElementById("table-body").innerHTML = xmlhttp.responseText;
    }
  }
  xmlhttp.open("GET","/search?q="+str,true);
  xmlhttp.send();
}

function addRow(myTable, columns) {

        var table = document.getElementById(myTable);

        var row = table.insertRow(1);
        row.className = 'table-row-data';
        for(x = 0; x < (columns.length - 1); x++){

          var data = row.insertCell(x);
          var element_data = document.createElement("input");
          element_data.type = "text";
          element_data.name = columns[x]['field_name'];
          element_data.id = columns[x]['field_name'];
          element_data.className = 'input-new-record';
          data.appendChild(element_data);
        }
          var data = row.insertCell(x);
          var data = row.insertCell(x + 1);

          var data = row.insertCell(x + 2);
          data.className = 'line-menu'

          var element_data = document.createElement("input");
          element_data.type = "button";
          element_data.className = 'btn-search';
          element_data.id = 'create-record';
          element_data.name = 'create-record';
          element_data.value = 'Salvar';
          data.appendChild(element_data);
          var element_data = document.createElement("input");
          element_data.type = "button";
          element_data.className = 'btn-search';
          element_data.id = 'remove-line';
          element_data.name = 'remove-line';
          element_data.value = 'Cancelar';
          data.appendChild(element_data);
}

function addRecords(){
  var div_msg = document.getElementById('background-msg')
  div_msg.style.display = 'block';
  xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange=function(){
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
        document.getElementById("background-msg").innerHTML = xmlhttp.responseText;
    }
  }
  xmlhttp.open("GET","/create",true);
  xmlhttp.send();
}

function enumerate_table_rows(table_id){
  var table = document.getElementById(table_id);
  var total_rows = table.rows.length;
  var table_rows_no_header = total_rows - 1

  if (table.rows[0].cells[0].innerHTML != '#'){
    var title = table.rows[0].insertCell(0);
    title.innerHTML = '#'
  }
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
function close_msg(){
  var div_msg = document.getElementById('background-msg')
  div_msg.style.display = 'none';
}