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
