function sendData1() {
    var value1 = document.getElementById('rating1').value;
    var rat_id = document.getElementById('mov_id').value;
    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value1, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value1)
        },
        error: function (error) {
            console.log(error);
        }
    });
}
function sendData2() {
    var value2 = document.getElementById('rating2').value;
    var rat_id = document.getElementById('mov_id').value;

    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value2, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value2)
        },
        error: function (error) {
            console.log(error);
        }

    });
}
function sendData3() {
    var value3 = document.getElementById('rating3').value;
    var rat_id = document.getElementById('mov_id').value;

    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value3, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value3)
        },
        error: function (error) {
            console.log(error);
        }
    });
}
function sendData4() {
    var value4 = document.getElementById('rating4').value;
    var rat_id = document.getElementById('mov_id').value;

    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value4, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value4)
        },
        error: function (error) {
            console.log(error);
        }
    });
}
function sendData5() {
    var value5 = document.getElementById('rating5').value;
    var rat_id = document.getElementById('mov_id').value;

    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value5, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value5)
        },
        error: function (error) {
            console.log(error);
        }
    });
}
function sendData6() {
    var value6 = document.getElementById('rating6').value;
    var rat_id = document.getElementById('mov_id').value;

    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value6, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value6)
        },
        error: function (error) {
            console.log(error);
        }
    });
}
function sendData7() {
    var value7 = document.getElementById('rating7').value;
    var rat_id = document.getElementById('mov_id').value;

    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value7, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value7)
        },
        error: function (error) {
            console.log(error);
        }
    });
}
function sendData8() {
    var value8 = document.getElementById('rating8').value;
    var rat_id = document.getElementById('mov_id').value;

    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value8, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value8)
        },
        error: function (error) {
            console.log(error);
        }
    });
}
function sendData9() {
    var value9 = document.getElementById('rating9').value;
    var rat_id = document.getElementById('mov_id').value;

    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value9, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value9)
        },
        error: function (error) {
            console.log(error);
        }
    });
}
function sendData10() {
    var value10 = document.getElementById('rating10').value;
    var rat_id = document.getElementById('mov_id').value;

    $.ajax({
        url: '/rating',
        type: 'POST',
        data: { 'data': value10, 'id_data': rat_id },
        success: function (response) {
            document.getElementById('output').innerHTML = response;
            alert("You have rated: " + value10)
        },
        error: function (error) {
            console.log(error);
        }
    });
}