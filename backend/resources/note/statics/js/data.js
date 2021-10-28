function convertTextToJson(text) {
    return JSON.parse(text);
}


function getColumnValuesOfTable(table, columnName) {
    let head = table.getElementsByTagName("tr")[0];
    let rows = table.getElementsByTagName("tr");
    rows = Object.values(rows);
    rows = rows.slice(1, rows.length);

    let idx = -1;
    for(let key of head.getElementsByTagName("th")) {
        idx += 1;
        if(key.innerHTML == columnName) {
            break;
        }
    }

    let array = [];
    for(let row of rows) {
        data = row.getElementsByTagName("td")[idx];
        array.push(data.innerHTML);
    }
    return array;
}
