if [ -z "$1" ]; then
    echo "Usage: $0 <name>"
    exit 1
fi
NAME=$1
CURRENT_TIME=$(date "+%Y-%m-%d %H:%M:%S %Z")
echo "Hello $NAME, right now the time is $CURRENT_TIME"
