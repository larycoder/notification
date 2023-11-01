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
  /* TODO: build tag list */
}
