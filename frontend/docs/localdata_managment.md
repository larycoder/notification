# Brief Description

Come with flutter, a local data management choice is pretty difficult since it
need to support vary types of platform. After make a short overview from
internet, the **hive** package is my final option for now. It satisfies all my
critical:

1. It support both web and android.
2. It is a NoSql but designed with concept of Sql in mind.
3. It is stable with high rate star

# Warning

Because Hive is still NoSql model, there are lack of many sorting, grouping or
filtering support. Therefore, I will need to do it by myself as well as on top
of hive. Fortunately, notification front-end is small app without heavy aggregate
task (I developed back-end server for them already). So this package is still
accepted. But noticing not to try load and process large scale of data at once
since they will be processed on memory and cause overflow.
