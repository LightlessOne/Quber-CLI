import os, sys, logging,urllib3, click

from qubership_pipelines_common_library_cli_test.test_command import SampleStandaloneExecutionCommand, CalcCommand
from qubership_pipelines_common_library.v1.execution.exec_logger import ExecutionLogger

DEFAULT_CONTEXT_FILE_PATH = 'context.yaml'

@click.group(chain=True)
def cli():
    logging.basicConfig(stream=sys.stdout, format=ExecutionLogger.DEFAULT_FORMAT, level=logging.INFO)
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_path)  
    logging.info(f"Current path: {current_path}")
    urllib3.disable_warnings()


@cli.command("run-test")
@click.option('--context_path', required=True, default=DEFAULT_CONTEXT_FILE_PATH, type=str, help="Path to context")
def __run_test(context_path):
    command = SampleStandaloneExecutionCommand(context_path)
    command.run()


@cli.command("calc")
@click.option('--context_path', required=True, default=DEFAULT_CONTEXT_FILE_PATH, type=str, help="Path to context")
def __calc(context_path):
    command = CalcCommand(context_path)
    command.run()
