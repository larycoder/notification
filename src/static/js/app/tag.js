/*
 * API fetch functions
 * */
async function fetch_tags_list() {
  let resp = await fetch("/api/tags", {
    "method": "GET"
  });
  return resp.json();
}

/*
 * DOM modification functions
 * */
async function dom_list_tags_make() {
  let tags = await fetch_tags_list();
  for (let tag of tags) {
    let dom_tag_str = `
    <li class="nav-item">
      <p><span class="fa fa-tag"></span> ${tag.name}</p>
    </li>
    `;
    let dom_tag = new DOMParser()
      .parseFromString(dom_tag_str, "text/html")
      .body.firstElementChild;
    $("#tags-list")[0].appendChild(dom_tag);
  }
}
