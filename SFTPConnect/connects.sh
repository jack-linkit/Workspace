#!/bin/bash

# SFTP server information
SFTP_HOST="ftp.linkit.com"
SFTP_PORT="22"  # Default SFTP port is 22
SFTP_USERNAME="Jack"
SFTP_REMOTE_DIR="/Districts/Pennsylvania/WPSD/Alma"  # Change this to the remote directory you want to pull from

# Local directory to store downloaded files
LOCAL_DIR="."  # Change this to your desired local directory

# SSH private key file (optional, only if using key-based authentication)
# SSH_PRIVATE_KEY="EWw}f3-a*Fx7A[3S"

# Connect and pull files from SFTP server
if [ -n "$SSH_PRIVATE_KEY" ]; then
    sftp -i "$SSH_PRIVATE_KEY" -P "$SFTP_PORT" "$SFTP_USERNAME@$SFTP_HOST" <<EOF
    pwd
    ls
    get -r "$SFTP_REMOTE_DIR" "$LOCAL_DIR"
    quit
EOF
else
    sftp -P "$SFTP_PORT" "$SFTP_USERNAME@$SFTP_HOST" <<EOF
    pwd
    ls
    get -r "$SFTP_REMOTE_DIR" "$LOCAL_DIR"
    quit
EOF
fi

echo "Files downloaded from SFTP server."
