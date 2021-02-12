# Note DB (SQLite)
- Don't use INCREAMENTAL AS id

## NOTES_T
+ note_id (uuid)
+ note_name

## RELATIONS_T
+ relation_id
+ parent_id
+ child_id

## TABLES_T
+ table_id
+ table_name
+ note_id

## CELLS_T
+ cell_id
+ table_id
+ cell_name
+ cell_note
+ start_time
+ end_time
+ is_notify