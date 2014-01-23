function verify_search(){
  if(document.getElementById('input-name').value.length < 1 && document.getElementById('input-location').value.length < 1){
      document.getElementById('search-msg').innerHTML = "Campo < name > ou < location > necessário!";
      return false;
  }
}