#!/bin/sh

aws s3 cp ./document.md  s3://${BUCKET_NAME}/document/${GITHUB_REF_NAME}/ --quiet