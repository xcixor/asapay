#!/usr/bin/env bash

set -o errexit
set -o pipefail
# set -o nounset
# set -o xtrace

get_var() {
  local name="$1"
  curl -s -H "Metadata-Flavor: Google" \
    "http://metadata.google.internal/computeMetadata/v1/instance/attributes/${name}"
}

get_required_variables () {
    export IP_ADDRESS="$(get_var "ip_address")"
    export SECRET_KEY="$(sudo openssl rand -hex 64)"
    export NAME="$(get_var "database_name")"
    export USER="$(get_var "database_user")"
    export PASSWORD="$(get_var "database_password")"
    export HOST="$(get_var "host")"
    export PORT="$(get_var "port")"
    export APPLICATION_HOST="$(get_var "application_host")"
    export GITHUB_BRANCH="$(get_var "github_branch")"
    export NGINX_SERVER_NAME="${APPLICATION_HOST}"
    export SERVICE_ACCOUNT="$(get_var "gs_credentials")"
    export DUMP_FILE="$(get_var "dump_file")"
    export GOOGLE_APPLICATION_CREDENTIALS="/usr/local/gs-account/account.json"
}

start_app () {
    cd ~/asapay/src/core/
    gunicorn -b 0.0.0.0:8000 --error-logfile /var/log/asapay-error.log core.wsgi
}

main () {
    get_required_variables
    start_app
}

main "$@"
