#!/bin/bash
set -euxo pipefail

docker rm -f fastapi-demo || true
