#!/bin/bash

HOST="http://localhost:8080"

# root object
root_check()
{
    curl -X GET $HOST
}

# notes object
notes_get()
{
    curl -X GET "$HOST/api/notes"
}

notes_del()
{
    curl -X DELETE "$HOST/api/notes"
}

# note object
note_get()
{
    curl -X GET "$HOST/api/note/1"
}

note_post()
{
    curl -X POST "$HOST/api/note" \
        -H "content-type: application/json" \
        -d '{"subject": "curl generated note", "content": "This is a test generated note"}'
}

note_del()
{
    curl -X DELETE "$HOST/api/note/1"
}

note_patch()
{
    curl -X PATCH "$HOST/api/note/1" \
        -H "content-type: application/json" \
        -d '{"content": "This is a test patched note"}'
}

# tag object
tags_get()
{
    curl -X GET "$HOST/api/tags"
}

tags_del()
{
    curl -X DELETE "$HOST/api/tags"
}

tag_post()
{
    curl -X POST "$HOST/api/tag" \
        -H 'content-type: application/json' \
        -d '{"name": "demo"}'
}

### TEST SCENARIO ###
note_interact_scenario()
{
    note_post;
    note_get;
    note_patch;
    note_get;
    note_del;
}

tag_interact_scenario()
{
    tag_post;
    tags_get;
}

### MAIN TEST ENV ###
#note_interact_scenario;
tag_interact_scenario;

# tear down test
#notes_del;
tags_del;
