function nextForm(flag) {
    document.getElementById("form" + flag).style.display = 'none';
    document.getElementById("form" + (parseInt(flag) + 1)).style.display = 'block';
}

function prevForm(flag) {
    document.getElementById("form" + flag).style.display = 'none';
    document.getElementById("form" + (parseInt(flag) - 1)).style.display = 'block';
}

function checkForm() {
    var form = document.getElementById("form1");
    var inputs = form.getElementsByTagName("input");

    for(var i = 0; i < inputs.length; i++) {
        if(inputs[i].hasAttribute("required")) {
            alert(inputs[i].value);
            if(inputs[i].value == "") {
                alert("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO");
                return false;
            }
        }
    }
    alert("TRUE");
    return true;
}

function submitForms() {
    document.getElementById("form1").submit();
    document.getElementById("form2").submit();
    document.getElementById("form3").submit();
    document.getElementById("form4").submit();
}