#!/bin/bash
docker-compose down -v
docker-compose up -d
docker exec -it hadoop-namenode hdfs namenode -format
docker-compose restart hadoop-namenode hadoop-datanode
docker exec -it hive-server bash -c "schematool -dbType postgres -initSchema"
