cd ../TESTS/
python --version

python quber_cli --help
#python quber_cli list-minio-files --context_path=./minio/context.yaml
python quber_cli run-sample
python quber_cli calc --context_path=context2.yaml

echo Tests done!