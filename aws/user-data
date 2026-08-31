#!/bin/bash
set -eux
dnf update -y || true
dnf install -y docker || true
systemctl enable --now docker
usermod -aG docker ec2-user || true
# In AWS, pull a versioned image from ECR and set DB_* variables for RDS.
