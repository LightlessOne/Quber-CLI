set -e
cd ..
export PYTHONUTF8=1
python -m venv .venv
source .venv/Scripts/activate

poetry build
pip install -q --target pack --no-compile --upgrade dist/quber_cli-0.0.1-py3-none-any.whl
# pip install python-minifier
# pyminify pack/kubernetes/ --in-place --remove-literal-statements
# pyminify pack/ --in-place --remove-literal-statements
python -m zipapp pack -o ./DATA/quber_cli.pyz --main=quber_cli.__main__:cli --compress
unzip -q ./DATA/quber_cli.pyz -d ./DATA/quber_cli

echo Build done!