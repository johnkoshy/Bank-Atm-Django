function validateForm_deposit() {
  var x = document.forms["myForm"]["dep_cash"].value;
  if (x == "" || x == null) {
    alert("Amount must be filled out");
    return false;
  }
}
function validateForm_withdraw() {
  var x = document.forms["myForm"]["wit_cash"].value;
  if (x == "" || x == null) {
    alert("Amount must be filled out");
    return false;
  }
}