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
  let resp = await fetch("/api/notes", {
    "method": "POST",
    "headers": {
      "content-type": "application/json"
    },
    "body": JSON.stringify(item)
  });
  return resp.json();
}

async function fetch_note_get(note_id) {
  let resp = await fetch(`/api/note/${note_id}`, {
    "method": "GET"
  });
  return resp.json();
}

async function fetch_note_del(note_id) {
  let resp = await fetch(`/api/note/${note_id}`, {
    "method": "DELETE"
  });
  return resp.json();
}

async function fetch_note_patch(note_id, item) {
  let resp = await fetch(`/api/note/${note_id}`, {
    "method": "PATCH",
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

/*
 * dom_note_content_toggle - trigger note content card based on action
 * action could be: "close", "readonly", "rw"
 */
async function dom_note_content_toggle(action) {
  if (action == "close") {
    $("#note-readonly")[0].style.display = "none";
    $("#note-rw")[0].style.display = "none";
  } else if (action == "readonly") {
    $("#note-readonly")[0].style.display = "block";
    $("#note-rw")[0].style.display = "none";
  } else if (action == "rw") {
    $("#note-readonly")[0].style.display = "none";
    $("#note-rw")[0].style.display = "block";
  }
}

async function dom_note_view_make(note_id) {
  let note = await fetch_note_get(note_id);
  $("#note-subject-readonly")[0].value = note.subject;
  $("#note-readonly-edit")[0].setAttribute("data-note-id", note_id);
  tinyMCE.get("note-editor-readonly").setContent(note.content);
  dom_note_content_toggle("readonly");
}

async function dom_note_edit_make(note_id) {
  let note = await fetch_note_get(note_id);
  $("#note-subject")[0].value = note.subject;
  tinyMCE.get("note-editor").setContent(note.content);
  $("#note-rw-save")[0].setAttribute("data-note-id", note_id);
  dom_note_content_toggle("rw");
}

async function dom_note_del(note_id) {
  let table = $("#note-table")[0];
  let row_idx = $(`#notes-table-row-${note_id}`)[0].rowIndex;
  await fetch_note_del(note_id);
  table.deleteRow(row_idx);
}

async function dom_notes_table_opts(note_id) {
  let opts = document.createElement("div");
  let opt_attrs = `class="btn btn-primary my-2"`;
  let view = `<button ${opt_attrs} onclick="dom_note_view_make(${note_id})">view</button>`;
  let edit = `<button ${opt_attrs} onclick="dom_note_edit_make(${note_id})">edit</button>`;
  let del = `<button ${opt_attrs} onclick="dom_note_del(${note_id})">del</button>`;
  opts.innerHTML = `${view} ${edit} ${del}`;
  return opts;
}

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
    row.setAttribute("id", `notes-table-row-${note.id}`)
    for (let field of fields) {
      if (field == "id") {
        let row_hdr = document.createElement("th");
        row_hdr.setAttribute("scope", "row");
        row_hdr.innerText = note.id;
        row.appendChild(row_hdr);
      } else if (field == "action") {
        row.appendChild(await dom_notes_table_opts(note.id));
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

async function dom_actions_add_onclick() {
  $("#action-notes-refresh").click(() => {
    $("#note-table")[0].innerHTML = '';
    dom_notes_table_make();
  });
  $("#action-notes-delete").click(async () => {
    await fetch_notes_del();
    $("#note-table")[0].innerHTML = '';
    dom_notes_table_make();
  });
  $("#action-note-add").click(() => {
    if ($("#note-rw")[0].style.display == "none") {
      $("#note-rw-save")[0].setAttribute("data-note-id", "-1");
      dom_note_content_toggle("rw");
    } else {
      $("#note-rw-discard").click();
    }
  });
  $("#note-rw-discard").click(() => {
    $("#note-subject")[0].value = "";
    tinyMCE.get("note-editor").setContent("");
    dom_note_content_toggle("close");
  });
  $("#note-readonly-close").click(() => {
    dom_note_content_toggle("close");
  });
  $("#note-readonly-edit").click(() => {
    let note_id = $("#note-readonly-edit")[0].getAttribute("data-note-id");
    dom_note_edit_make(note_id);
  });
  $("#note-rw-save").click(async () => {
    let id = $("#note-rw-save")[0].getAttribute("data-note-id");
    let item = {
      "subject": $("#note-subject")[0].value,
      "content": tinyMCE.get("note-editor").getContent(),
    };
    if (id == -1)
      await fetch_note_add(item);
    else
      await fetch_note_patch(id, item);
    $("#action-notes-refresh").click();
  });
}
