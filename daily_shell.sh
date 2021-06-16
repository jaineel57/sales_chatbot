#!/bin/bash  
echo "This is a shell script"  
echo "Running script for queries"
python3 queries.py
echo "stopping and clearing out old running containers"
docker rm -fv $(docker ps -aq)
echo "ending running existing tmux sessions"
tmux kill-session -t rasa-docker
echo "re executing rasa containers"
docker build ./actions -t action-server:latest
echo "making new session"
tmux new -s rasa-docker "docker-compose up"
echo "containers are live"  
kill -9 $PPID