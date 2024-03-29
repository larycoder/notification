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

async function fetch_tag_get(tag_id) {
  let resp = await fetch(`/api/tag/${tag_id}`, {
    "method": "GET",
    "headers": {
      "content-type": "application/json"
    },
  });
  return resp.json();
}

async function fetch_tags_get() {
  let resp = await fetch(`/api/tags`, {
    "method": "GET",
    "headers": {
      "content-type": "application/json"
    },
  });
  return resp.json();
}

async function fetch_notes_filter(tag_name) {
  let params = new URLSearchParams({
    "tag_name": tag_name,
  });
  let resp = await fetch(`/api/notes/filter?${params.toString()}`, {
    "method": "GET",
    "headers": {
      "content-type": "application/json"
    },
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

async function dom_note_tag_make(note_id) {
  let tags = await fetch_tags_get();
  let tag_opts = $("#note-tag-list")[0];
  tag_opts.innerHTML = "<option value='-1' selected>Tag list</option>";
  for (let tag of tags) {
    tag_opts.innerHTML += `
      <option value=${tag.id}>${tag.name}</option>
    `;
  }
  $("#note-tag-modal").attr("tabindex", note_id);
  $("#note-tag-modal").modal("show");
}

async function dom_notes_table_opts(note_id) {
  return `
  <div class="dropdown">
    <button type="button" class="btn" data-toggle="dropdown">
      <span class="fa fa-ellipsis-v"></span>
    </button>
    <div class="dropdown-menu">
      <a class="dropdown-item" href="#" onclick="dom_note_view_make(${note_id})">View</a>
      <a class="dropdown-item" href="#" onclick="dom_note_edit_make(${note_id})">Edit</a>
      <a class="dropdown-item" href="#" onclick="dom_note_del(${note_id})">Delete</a>
      <a class="dropdown-item" href="#" onclick="dom_note_tag_make(${note_id})">Tag</a>
    </div>
  </div>`;
}


async function dom_notes_table_make(notes_get_func) {
  var fields = ["id", "subject", "tag", "action"];
  let table = $("#note-table")[0];

  /* header */
  let headers = document.createElement("thead");
  headers.classList.add("thead-dark");
  for (let field of fields) {
    let header = document.createElement("th");
    header.setAttribute("scope", "col");
    header.style["text-align"] = "center";
    header.innerText = field;
    headers.appendChild(header);
  }
  table.appendChild(headers);

  /* row */
  let body = document.createElement("tbody");
  let notes = await notes_get_func();
  for (let note of notes) {
    let row = document.createElement("tr");
    row.setAttribute("id", `notes-table-row-${note.id}`)
    for (let field of fields) {
      if (field == "id") {
        let row_hdr = document.createElement("th");
        row_hdr.setAttribute("scope", "row");
        row_hdr.style["text-align"] = "center";
        row_hdr.innerText = note.id;
        row.appendChild(row_hdr);
      } else if (field == "action") {
        let row_dat = document.createElement("td")
        row_dat.style["text-align"] = "center";
        row_dat.innerHTML = await dom_notes_table_opts(note.id);
        row.appendChild(row_dat);
      } else if (field == "tag") {
        let tag = {
          "name": ""
        };
        let row_dat = document.createElement("td");
        row_dat.style["text-align"] = "center";
        if (note.tags.length > 0)
          tag = await fetch_tag_get(note.tags[0]); // assume one note one tag
        row_dat.innerText = tag.name;
        row.appendChild(row_dat);
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
    dom_notes_table_make(fetch_notes_list);
  });
  $("#action-notes-delete").click(async () => {
    await fetch_notes_del();
    $("#note-table")[0].innerHTML = '';
    dom_notes_table_make(fetch_notes_list);
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
  $("#note-tag-save").click(async () => {
    let note_id = $("#note-tag-modal").attr("tabindex");
    let note = await fetch_note_get(note_id);
    let tag_id = $("#note-tag-list")[0].value;
    if (tag_id == -1) {
      console.log("Please choose one tag.");
      return;
    }
    note.tags = [tag_id];
    $("#note-table")[0].innerHTML = '';
    await fetch_note_patch(note_id, note);
    $("#note-tag-modal").modal("hide");
    dom_notes_table_make(fetch_notes_list);
  });
  $("#action-note-filter").click(async () => {
    let tag_name = $("#action-note-filter-value")[0].value;
    $("#note-table")[0].innerHTML = '';
    dom_notes_table_make(async () => {
      return await fetch_notes_filter(tag_name);
    });
  });
}
