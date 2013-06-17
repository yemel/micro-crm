source env/bin/activate

export DATABASE_URL="postgres://postgres:1@localhost/crm"
export STATIC_URL="/static/"
export IMAGE_ROOT="img/"
export PUBLIC_URL="http://localhost:8000"

export ROOT=`pwd`
export MANAGE="python $ROOT/manage.py"

alias m=$MANAGE
