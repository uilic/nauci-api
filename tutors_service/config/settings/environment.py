from pathlib import Path

import environ


# ENVIROMENT
# ------------------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent

# document_service/
BASE_DIR = ROOT_DIR / "tutors_service"
APPS_DIR = BASE_DIR / "apps"

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / "config" / "envs" / ".env"))


# strip out any of the environment marked with our magic '<stub>' value.
# This is a limitation of parameter store, in that it must always have content.
for key, value in list(env.ENVIRON.items()):
    if value == "<stub>":
        env.ENVIRON.pop(key)
