echo [$(date)]: "START"

echo [$(date)]: "Creating env with python 3.10 version"

python3.10 -m venv .env

echo [$(date)]: "activating the environment"

source .env/bin/activate

echo [$(date)]: "Installing the dev requirements"

pip install -r requirements_dev.txt

echo [$(date)]: "END"