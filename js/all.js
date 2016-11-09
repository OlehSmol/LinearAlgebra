console.log("all.js is running");

function readMatrixValue(id) {
    "use strict";
    var table = document.getElementById(id),
        matrix = new Array(table.children.length); //table.children[0].children.length);

    for (var i = 0; i < table.children.length; i++) {
        var tr = table.children[i],
            row = new Array(tr.children.length + 1);
        for (var j = 0; j < tr.children.length; j++) {
            var td = tr.children[j],
                val = td.children[0].value;
            if (val === "" || Number(val) === NaN) {
                val = Number(td.children[0].placeholder);
            } else {
                val = Number(td.children[0].value)
            }
            row[j] = val;
        }
        matrix[i] = row;
    }
    return matrix;

}

function removeMatrix(id) {
    "use strict";
    document.getElementById('input-container').removeChild(document.getElementById(id));
}

function clearContent(id) {
    "use strict";
    document.getElementById(id).innerHTML = '';
}

function generateMatrixTable(m, n, id) {
    "use strict";
    var table = document.createElement('table');
    table.id = id;
    table.className = 'matrix';

    for (var i = 0; i < Number(m); i++) {
        var tr = document.createElement('tr');
        for (var j = 0; j < Number(n); j++) {
            var td = document.createElement('td');
            var input = document.createElement('input');
            input.placeholder = '1';
            td.appendChild(input);
            tr.appendChild(td);
        }
        table.appendChild(tr)
    }

    document.getElementById('input-container').appendChild(table);
}

function generateJSONmessage() {
    "use strict";
    var matrix = readMatrixValue('user-matrix'),
        bVector = readMatrixValue('b-vector');
    for (var i = 0; i < matrix.length; i++) {
        matrix[i][matrix[i].length - 1] = bVector[i][0];
    }

    return JSON.stringify({
        matrix
    });
}

//
// --------------------------------displayResponse ------------------------------
//

function displayResponse(response) {
    "use strict";
    var fillWord = "inconsistent";
    if (JSON.parse(response) == true) {
        fillWord = "consistent";
    } 
    var message = "The system Ax = b is <span class='bold wrapped'>" + fillWord + "</span> "
    var p = document.createElement('p');
    p.innerHTML = message;
    document.getElementById('solution-description').appendChild(p);

}

//
// --------------------------------XMLHttpRequest------------------------------
//

function makeXMLrequest(method, URI, onloadHandler, onerrorHandler, message) {
    "use strict";
    var xhr = new XMLHttpRequest();
    xhr.open(method, URI, true);

    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function () {
        onloadHandler(xhr.response);
    };
    xhr.onerror = function () {
        onerrorHandler(xhr.status + ': ' + xhr.statusText);
    };
    xhr.send(message);
}

//
// --------------------------------window.onload------------------------------
//
window.onload = function () {
    "use strict";

    // create and add two tables in main-section
    generateMatrixTable(2, 2, 'user-matrix');
    generateMatrixTable(2, 1, 'b-vector');

    // #matrix-size selector onchange handler
    document.getElementById('matrix-size').onchange = function () {
        var size = this.options[this.selectedIndex].value;
        removeMatrix('user-matrix');
        removeMatrix('b-vector');
        generateMatrixTable(size, size, 'user-matrix');
        generateMatrixTable(size, 1, 'b-vector');

    };

    // #submit button onclick handler
    document.getElementById('submit').onclick = function () {
        this.innerHTML = "Processing...";
        this.disabled = true;

        clearContent('solution-description');
        
        var myJSONString = generateJSONmessage();
        console.log(myJSONString);

        var onloadMethod = function (response) {
            document.getElementById('submit').innerHTML = "Push me again, I like it";
            document.getElementById('submit').disabled = false;
            displayResponse(response);
            console.log(response);
        };

        var onerrorMethod = function (responseMessage) {
            document.getElementById('submit').innerHTML = "Error, try again";
            document.getElementById('submit').disabled = false;
            console.log(responseMessage);
        };
        //        makeXMLrequest('POST', 'http://127.0.0.1:5000/linearalgebra/api/v1.0/consistent', onloadMethod, onerrorMethod, myJSONString);
        makeXMLrequest('POST', 'https://mnitd.pythonanywhere.com/linearalgebra/api/v1.0/consistent', onloadMethod, onerrorMethod, myJSONString);
    };
};

//
// --------------------------------window.onscroll------------------------------
//
window.onscroll = function () {
    "use strict";
    var headerHeight = 90,
        scrolled = window.pageYOffset || document.documentElement.scrollTop;

    if (scrolled >= headerHeight) {
        document.getElementById("left-menu").className = "left-menu fixed";
    } else {
        document.getElementById("left-menu").className = "left-menu";
    }
}