Table no_class {
  clid int [pk]
  name varchar(5) [not null]
}

Table no_type {
  tid int [pk]
  name varchar(10) [not null, unique]
  size int [default: null]
  description text [default: null]
}

Table no_content {
  cid int [pk]
  value text [not null]
  type int [not null]
  class int [default: null]
  referral int [default: null]
  label int [default: null]
  meta text [default: null]
}
Ref: no_content.type > no_type.tid
Ref: no_content.class > no_class.clid
Ref: no_content.referral > no_content.cid

Table no_note {
  nid int [pk]
  name text [not null, unique]
  description text [default: null]
}

Table no_lookup {
  lkid int [pk]
  nid int [not null]
  cid int [not null]
  is_origin int [default: null]
}
Ref: no_lookup.nid > no_note.nid
Ref: no_lookup.cid > no_content.cid

