function callSimpleApi(method, link, body = null) {
    let request = new XMLHttpRequest();
    request.open(method, link, false);
    request.setRequestHeader("Content-Type", "application/json");
    request.send(body);
    return request.response;
}


function callAsyncSimpleApi(method, link, promiseFunc, body = null) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if(this.stateChange == 4) {
            promiseFunc(this.status, this.response);
        }
    };
    request.open(method, link, true);
    request.send(body);
}