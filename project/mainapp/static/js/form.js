function nextForm(flag) {
    document.getElementById("form" + flag).style.display = 'none';
    document.getElementById("form" + (parseInt(flag) + 1)).style.display = 'block';
}

function prevForm(flag) {
    document.getElementById("form" + flag).style.display = 'none';
    document.getElementById("form" + (parseInt(flag) - 1)).style.display = 'block';
}