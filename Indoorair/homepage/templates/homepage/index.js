function onContactClick() {
  window.location.href = "/contact";
}

function onLoginClick() {
  window.location.href ="/login";

}
function onRegisterClick() {
  window.location.href ="/register";

}
function onVersionClick() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById('version').innerHTML = this.responseText;
    }
  }
  xhttp.open('GET', 'api/version', true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send();
}
