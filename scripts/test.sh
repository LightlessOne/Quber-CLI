cd ../TESTS/
python --version

python quber_cli --help

python quber_cli add-integers --arg1=9 --arg2=$(python quber_cli add-integers --arg1=5 --arg2=5)

python quber_cli add-integers-and-then-ten-more --arg1=9 --arg2=10

python quber_cli save --data="$(python quber_cli do-stuff-with-context --project='fdroid/fdroidclient' --branch='master' --path='.weblate')" --result_path='./test_result.txt'

cat ./test_result.txt

echo Tests done!