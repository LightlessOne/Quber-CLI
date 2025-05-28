python -m venv .venv

unzip -q ./quber_cli.pyz -d ./tests/quber_cli # where do we need unpacked pyz from root?
pip install -q -r ./.github/scripts/requirements.txt
python ./tests/run_test_suite.py