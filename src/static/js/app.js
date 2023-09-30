/*
 * API fetch functions
 * */

async function fetch_notes_list() {
  let resp = await fetch("/api/notes", {
    "method": "GET"
  });
  return resp.json();
}

async function fetch_notes_del() {
  let resp = await fetch("/api/notes", {
    "method": "DELETE"
  });
  return resp.json();
}

async function fetch_note_add(item) {
  let resp = await fetch("/api/note", {
    "method": "POST",
    "headers": {
      "content-type": "application/json"
    },
    "body": JSON.stringify(item)
  });
  return resp.json();
}

/*
 * DOM modification functions
 * */

async function dom_notes_table_make() {
  var fields = ["id", "subject", "action"];
  let table = $("#note-table")[0];

  /* header */
  let headers = document.createElement("thead");
  headers.classList.add("thead-dark");
  for (let field of fields) {
    let header = document.createElement("th");
    header.setAttribute("scope", "col");
    header.innerText = field;
    headers.appendChild(header);
  }
  table.appendChild(headers);

  /* row */
  let body = document.createElement("tbody");
  let notes = await fetch_notes_list();
  for (let note of notes) {
    let row = document.createElement("tr");
    for (let field of fields) {
      if (field == "id") {
        let row_hdr = document.createElement("th");
        row_hdr.setAttribute("scope", "row");
        row_hdr.innerText = note.id;
        row.appendChild(row_hdr);
      } else {
        let row_dat = document.createElement("td");
        row_dat.innerText = note[field];
        row.appendChild(row_dat);
      }
    }
    body.appendChild(row);
  }
  table.appendChild(body);
}

async function dom_note_add() {
  console.log("add new note");
}

async function dom_actions_add_onclick() {
  $("#action-notes-refresh").click(() => {

  });
  $("#action-notes-delete").click(async () => {
    await fetch_notes_del();
    $("#note-table")[0].innerHTML = '';
    dom_notes_table_make();
  });
  $("#action-note-add").click(() => {
    $("#note-readonly")[0].style.display = "none";
    if ($("#note-header")[0].style.display == "none") {
      $("#note-rw-save")[0].setAttribute("data-note-id", "-1");
      $("#note-rw-save").click(dom_note_add);
      $("#note-header")[0].style.display = "block";
      $("#note-rw")[0].style.display = "block";
    } else {
      $("#note-header")[0].style.display = "none";
      $("#note-rw")[0].style.display = "none";
    }
  });
  $("#note-rw-discard").click(() => {
    $("#note-subject")[0].value = "";
    tinyMCE.get("note-editor").setContent("");
    $("#note-header")[0].style.display = "none";
    $("#note-rw")[0].style.display = "none";
  });
}
