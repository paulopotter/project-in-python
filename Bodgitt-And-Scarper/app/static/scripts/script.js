function ajax_require(element, page, method, post_values){
  method = typeof method !== 'undefined' ? method : 'GET';
  post_values = typeof post_values !== 'undefined' ? post_values : null;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function(){
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
        document.getElementById(element).innerHTML = xmlhttp.responseText;
    }
  }
  xmlhttp.open(method, page, true);
  xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
  xmlhttp.send(post_values);
}

function searchResult(str){
  ajax_require('table-body',"/search?q=" + str);
}

function addRecords(validate){
 if (validate) {
  var name_value  = encodeURIComponent(document.getElementById("name").value)
  var location_value  = encodeURIComponent(document.getElementById("location").value)
  var specialties_value = encodeURIComponent(document.getElementById("specialties").value)
  var size_value  = encodeURIComponent(document.getElementById("size").value)
  var rate_value  = encodeURIComponent(document.getElementById("rate").value)

  var post_values = "name=" + name_value + "&location=" + location_value + "&specialties=" + specialties_value + "&size=" + size_value + "&rate=" + rate_value

    ajax_require('background-msg', '/create-validation', 'POST', post_values)
  } else {
    var div_msg = document.getElementById('background-msg');
    div_msg.style.display = 'block';
    ajax_require('background-msg', '/create');
  }
}

function verify_new_record(meta_data){
  var div_msg = document.getElementById('background-msg');
  div_msg.style.display = 'block';
  ajax_require('body', "/create-validation");
}

function remove_record(name, location, validate){

  if (validate) {
    ajax_require('background-msg', '/remove-validation?name=' + name + '&location=' + location)
  } else {
    var div_msg = document.getElementById('background-msg');
    div_msg.style.display = 'block';
    ajax_require('background-msg', '/remove?name=' + name + '&location=' + location);
  }
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

/* ==== Inline editor ==== */

InlineEditor.customEditor = function( theElement )
  {
      // Only interested in setting up something custom
      // for paragraph tags.
      if( theElement.tagName != 'P' )
          return;

      var editor = document.createElement( 'textarea' );
      editor.innerHTML    = theElement.innerHTML;
      editor.style.width  = "100%";
      editor.style.height = theElement.offsetHeight + "px";

      return editor;
  }   // end customEditor

InlineEditor.editorValue = function( editor )
{
    // Hypothetical editor with some obscure way
    // of determing what the user selection is.
    if( editor.tagName == 'SomeObscureControl' )
        return editor.squareRootOfSelectedMenuItem;

}   // end editorValue


InlineEditor.elementValue = function( theElement )
{
    // Ignore the extra 'span' I threw in there. Just give me text.
    return theElement.innerText;

}   // end elementValue


InlineEditor.elementChanged = function( theElement, oldVal, newVal )
{
    InlineEditor.addClass( theElement, 'uneditable' ); // Special InlineEditor class
    InlineEditor.addClass( theElement, 'saving' );     // My own class, maybe gray text

    var request = new XMLHttpRequest();
    var url = "/edit-me?id=" + encodeURIComponent(theElement.id) + '&val=' + encodeURIComponent(newVal);

    request.open("GET", url, true);
    request.onreadystatechange = function() {
        if (request.readyState == 4) {

            InlineEditor.removeClass( theElement, 'uneditable' );
            InlineEditor.removeClass( theElement, 'saving' );

        }   // end if: readystate 4
    };  // end onreadystatechange
    request.send(null);

};  // end elementChanged
