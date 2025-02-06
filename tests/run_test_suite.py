import logging
import os, pytest
import sys

ZIPAPP_PATH = "./quber_cli.pyz"


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


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                        format=u'[%(asctime)s] [%(levelname)-s] [%(filename)s]: %(message)s')
    try:
        os.chdir("./DATA")
        res = pytest.main(args=["../tests"])
        if res != 0:
            raise Exception("Tests failed!")
        report_execution_result(True)
    except Exception as e:
        report_execution_result(False, e)
        exit(1984)
