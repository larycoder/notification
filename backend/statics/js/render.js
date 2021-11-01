function renderJsonAsTable(obj, posId) {
    let count = obj["count"];
    if(!typeof count === "number" || count < 1) {
        let emptyRow = "<tr><th>Empty</th></tr>";
        return `<table id="${posId}_table">${emptyRow}</table>`
    }

    let listObj = obj["data"];
    let firstObj = listObj[0];

    // head
    headText = "<tr>";
    for (let key of Object.keys(firstObj)) {
        headText += "<th>" + key + "</th>";
    }
    headText += "</tr>";

    // data
    dataText = "";
    for (let obj of listObj) {
       dataText += "<tr>";
       for (let key of Object.keys(obj)) {
            dataText += "<td>" + obj[key] + "</td>";
       }
       dataText += "</tr>";
    }

    return `<table border=1 id="${posId}_table">${headText} ${dataText}</table>`;
}


function addColToTable(table, name, values) {
    let head = table.getElementsByTagName("tr")[0];
    let rows = table.getElementsByTagName("tr");
    rows = Object.values(rows);
    rows = rows.slice(1, rows.length);

    head.innerHTML += "<th>" + name + "</th>";
    let idx = 0;
    for(let row of rows) {
        console.log(values[idx]);
        row.innerHTML += "<td>" + values[idx] + "</td>";
        idx += 1;
    }
}


// inputBoxFunc used to detect input tag for each field
function renderInputBox(fields, inputBoxFunc, posId) {
    let box = "";
    for(let field of fields) {
        let id = posId + "_" + field;
        let labelId = id + "_title";
        let label = `<label for="${id}" id="${labelId}">${field}: </label>`;
        let input = inputBoxFunc(field, posId);
        box += `${label} ${input} <br>`;
    }
    return box;
}