fastapi dev train_times.py >/dev/null 2>&1 & backend=$!
printf "spinning up backend...\n"
sleep 1
uv run frontend.py
printf "disposing backend...\n"
kill -2 "$backend"

