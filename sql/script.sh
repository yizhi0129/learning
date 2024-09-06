#!/bin/bash

sudo mysql -u root -p --table < 2_1.sql > 2_1.log
sudo mysql -u root -p --table < 2_2.sql > 2_2.log

python3 test_mysql3_1.py
python3 test_mysql3_2.py