#!/bin/sh
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ "${1-}" = "--infologs" ]; then
    python3 "$SCRIPT_DIR/setup_pst.py" --infologs
else
    python3 "$SCRIPT_DIR/setup_pst.py"
fi

exit $?
