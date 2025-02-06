cd ..
python -m venv .venv

pip install -q pyyaml pytest
python ./tests/run_test_suite.py