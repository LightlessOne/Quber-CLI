cd ..
python -m venv .venv

pip install -q pyyaml
python ./scripts/python/check_test_results.py