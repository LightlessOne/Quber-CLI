set -e
cd ..
python -m venv .venv

poetry build
pip install -q --target pack --no-compile --upgrade dist/quber_cli-0.0.1-py3-none-any.whl
python -m zipapp pack -o ./DATA/quber_cli.pyz --main=quber_cli.__main__:cli --compress
unzip -q ./DATA/quber_cli.pyz -d ./DATA/quber_cli
export QUBERSHIP_VERSION="$(pip freeze --path pack | grep qubership)"

echo Build done!

cd ./scripts