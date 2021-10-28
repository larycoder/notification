Table tasks {
  id int [pk]
  parentId int [ref: > tasks.id]
  task text [not null]
  notes text [default: null]
  label text [default: null]
  priority text [default: null]
  created_time timestamp
  deadline timestamp [default: null]
  measurement text [default: null]
  process float8 [default: null]
}

Table diary {
  id int [pk]
  activity text [not null]
  notes text [default: null]
  created_time timestamp
  start_time timestamp [default: null]
  duration timestamp [default: null]
  taskId int [ref: > tasks.id, default: null]
}