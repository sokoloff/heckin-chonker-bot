# heckin-chonker-bot

## Install & development setup

### Poetry
Use [poetry](https://python-poetry.org/docs/#installation) for packaging and dependency management.

- Install dependencies
```bash
poetry install
```
- Start virtual environment
```bash
poetry shell
```

### Configuration
- Configuration is located in `heckin_chonker_bot/config.py`.
- You can use environment variables to configure application or use `.env` file with `key=values` pairs.
Provide path to `.env` file in `DOTENV_PATH`.
- Use `config/.env.example` as a starter. Set necessary empty variables.


### Run application
```bash
export DOTENV_PATH=./config/.env
python ./heckin_chonker_bot/bot.py
```
