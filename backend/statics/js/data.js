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


function convertUrlParamToJson(url) {
    let params = url.split("?");
    params = params[params.length - 1];
    let array = params.split("&");
    let obj = {};
    for(let value of array) {
        let pair = value.split("=");
        obj[pair[0]] = pair[1];
    }
    return obj;
}


function getObjectFromResponse(resp, idx) {
    let data = convertTextToJson(resp);
    if(!typeof data.count === "number" || data.count < idx + 1) {
        return {}
    } else {
        return data.data[idx];
    }
}


function convertObjToArray(keys, obj) {
    let array = [];
    for(let field of Object.keys(obj)) {
        let tempObj = {}
        tempObj[keys[0]] = field;
        tempObj[keys[1]] = obj[field];
        array.push(tempObj);
    }
    return array;
}