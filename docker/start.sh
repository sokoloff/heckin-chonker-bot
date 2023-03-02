#!/usr/bin/env sh
set -e

. /venv/bin/activate

if [ $RUN_PRESTART == 1 ] ; then
    echo "Running pre-start script"
    ./prestart.sh
else
    echo "Not running pre-start script"
fi

exec python heckin_chonker_bot/bot.py
