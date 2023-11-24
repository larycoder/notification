/*
 * API fetch functions
 * */
async function fetch_tags_list() {
  let resp = await fetch("/api/tags", {
    "method": "GET"
  });
  return resp.json();
}

async function fetch_tags_add(item) {
  let resp = await fetch("/api/tags", {
    "method": "POST",
    "headers": {
      "content-type": "application/json"
    },
    "body": JSON.stringify(item)
  });
  return resp.json();
}

async function fetch_tag_del(tag_id) {
  let resp = await fetch(`/api/tag/${tag_id}`, {
    "method": "DELETE"
  });
  return resp.json();
}

/*
 * DOM modification functions
 * */
async function tag_del(id) {
  await fetch_tag_del(id);
  $("#tags-list")[0].innerHTML = "";
  dom_list_tags_make();
}

async function dom_tag_option_make(id) {
  return `
  <div class="dropdown">
    <button type="button" class="btn btn-light" data-toggle="dropdown">
      <span class="fa fa-ellipsis-v"></span>
    </button>
    <div class="dropdown-menu">
      <a class="dropdown-item" href="#" onclick="tag_del(${id});">Delete</a>
    </div>
  </div>`;
}

async function dom_list_tags_make() {
  let tags = await fetch_tags_list();
  for (let tag of tags) {
    let dom_tag_str = `
    <li class="nav-item">
      <div class="d-flex justify-content-between">
        <p><span class="fa fa-tag"></span> ${tag.name}</p>
        ${await dom_tag_option_make(tag.id)}
      </div>
    </li>
    `;
    let dom_tag = new DOMParser()
      .parseFromString(dom_tag_str, "text/html")
      .body.firstElementChild;
    $("#tags-list")[0].appendChild(dom_tag);
  }
}

async function dom_tag_event_onclick() {
  $("#tag-add").click(async () => {
    let value = document.getElementById("tag-name").value;
    await fetch_tags_add({
      "name": value
    });
    $("#tags-list")[0].innerHTML = "";
    dom_list_tags_make();
    $("#tag-add-modal").modal("toggle");
  });
}
