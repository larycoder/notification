Table notes {
  id int [pk]
  subject text [not null]
  content text [default: null]
  created_time timestamp
  updated_time timestamp
}