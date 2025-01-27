import os, yaml

ZIPAPP_PATH = "./TESTS/quber_cli.pyz"


def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Yi{suffix}"


def write_step_summary(text: str):
    print(text)
    with open(os.getenv('GITHUB_STEP_SUMMARY'), 'w') as summary_file:
        summary_file.write(text)


def report_execution_result(is_success: bool, error: Exception = None):
    zipapp_size = sizeof_fmt(os.path.getsize(ZIPAPP_PATH))
    message = f"""### Validate test results report:
- Result is {"SUCCESS :white_check_mark:" if is_success else "FAILURE :x:"}
- Resulting zipapp artifact size is **{zipapp_size}**
- Used version: {os.getenv('QUBERSHIP_VERSION', "UNKNOWN")}
    """
    if error:
        message += f"\n\nError message:\n```{type(error)} - {error}```"
    write_step_summary(message)


def test_run_sample():
    with open('./TESTS/result.yaml', 'r', encoding='utf-8') as file:
        result = yaml.safe_load(file)
        if 19 != result['params']['result']:
            raise Exception("result.yaml is invalid")


def test_calc():
    with open('./TESTS/result_calc.yaml', 'r', encoding='utf-8') as file:
        result = yaml.safe_load(file)
        if 0.9 != result['params']['result_divide']:
            raise Exception("result_calc.yaml is invalid")

def test_new_quber_commands():
    with open('./TESTS/test_result.txt', 'r', encoding='utf-8') as file:
        if len(file.read()) == 0:
            raise Exception("test_result.txt is invalid")


if __name__ == '__main__':
    # todo: rework into 'integration-test-suite':
    #     run quber_cli as a subprocess in each test, then assert it's results
    # Think about integration tests:
    # possible approach: some tests in lib will require local service running (like minio), and expect to have it on localhost:9000 or something
    # these tests are marked as INTEGRATION, and won't run with usual unittests, only in a separate on-demand pipeline
    # also: integration tests: use github-workflow provided 'services'with required docker images (minio for now) (to test commands)
    try:
        test_new_quber_commands()
        #test_run_sample()
        #test_calc()
        report_execution_result(True)
    except Exception as e:
        report_execution_result(False, e)
        exit(1984)
