function nextForm(flag) {
    document.getElementById("form" + flag).style.display = 'none';
    document.getElementById("form" + (parseInt(flag) + 1)).style.display = 'block';
}

function prevForm(flag) {
    document.getElementById("form" + flag).style.display = 'none';
    document.getElementById("form" + (parseInt(flag) - 1)).style.display = 'block';
}

function submitForms() {
    document.getElementById("form1").submit();
    document.getElementById("form2").submit();
    document.getElementById("form3").submit();
    document.getElementById("form4").submit();
}