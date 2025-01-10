cd ../TESTS/
python --version
python quber_cli.pyz --help
python quber_cli.pyz run-test && python quber_cli.pyz calc --context_path=context2.yaml
echo DONE!