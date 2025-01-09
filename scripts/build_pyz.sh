cd ..
python -m venv .venv
source .venv/Scripts/activate
poetry build
pip install -q --target pack --no-compile --upgrade dist/qubership_pipelines_common_library_cli_test-0.0.1-py3-none-any.whl
python -m zipapp pack -o ./TESTS/quber_cli.pyz --main=qubership_pipelines_common_library_cli_test.__main__:cli
echo DONE!