cd ../DATA/
python --version

python quber_cli --help
#python quber_cli list-minio-files --context_path=./minio/context.yaml
python quber_cli run-sample
python quber_cli calc --context_path=context2.yaml

python quber_cli umbrella-test
cd RESULTS_FOLDER
find . | sed -e "s/[^-][^\/]*\// |/g" -e "s/|\([^ ]\)/|-\1/"

#export GITHUB_TOKEN=""
#python quber_cli github-run-pipeline-demo

echo Tests done!