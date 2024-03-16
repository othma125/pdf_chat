#!/bin/bash
sudo service mysql start
# source venv/bin/activate
USER=admin PASSWORD=admin_pwd DB=pdf_chat_db HOST=localhost python3 -m api.app