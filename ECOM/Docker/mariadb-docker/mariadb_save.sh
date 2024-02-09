#!/bin/bash

TIMESTAMP=$(date '+%Y-%m-%d_%H-%M-%S')
BACKUP_DIR="./backup/"
BACKUP_FILE="$BACKUP_DIR/mariadb_backup_$TIMESTAMP.sql"

docker exec mariadb-docker mysqldump -u root --password="tpRT9025" --single-transaction --databases ecomddb --skip-column-statistics > $BACKUP_FILE
