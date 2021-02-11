#!/bin/bash

####### VAR ############
SQL_SCIRPT_NAME='gen_script.sql'
SQL_DB_NAME='notification.db'

########################

SCRIPT=$0
WORKDIR=$1

getSqlGenScript(){
    t_script=$(readlink -f $1)
    sql_path=$(dirname $t_script)
    echo $sql_path/$SQL_SCIRPT_NAME
}

SQL_SCIRPT=$(getSqlGenScript $SCRIPT)


# remove exists db
if [[ -f "$WORKDIR/$SQL_DB_NAME" ]]
then
    rm $WORKDIR/$SQL_DB_NAME
fi 

# generate new db
sqlite3 $WORKDIR/$SQL_DB_NAME < $SQL_SCIRPT