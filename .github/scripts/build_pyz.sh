set -e
python -m venv .venv

poetry build
pip install -q --target pack --no-compile --upgrade dist/*.whl
python -m zipapp pack -o ./quber_cli.pyz --main=quber_cli.__main__:cli --compress
export QUBERSHIP_VERSION="$(pip freeze --path pack | grep qubership)"
echo Build done!
