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