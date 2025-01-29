import os, sys, logging, urllib3, click

from quber_cli.minio_commands import ListMinioBucketObjectsCommand
from quber_cli.sample_command import SampleStandaloneExecutionCommand, CalcCommand
from qubership_pipelines_common_library.v1.execution.exec_logger import ExecutionLogger

from quber_cli.umbrella_test.in_memory_context import create_execution_context
from quber_cli.umbrella_test.umbrella_command import UmbrellaCommand

DEFAULT_CONTEXT_FILE_PATH = 'context.yaml'


@click.group(chain=True)
def cli():
    logging.basicConfig(stream=sys.stdout, format=ExecutionLogger.DEFAULT_FORMAT, level=logging.INFO)
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_path)
    urllib3.disable_warnings()


@cli.command("run-sample")
@click.option('--context_path', required=True, default=DEFAULT_CONTEXT_FILE_PATH, type=str, help="Path to context")
def __run_sample(context_path):
    command = SampleStandaloneExecutionCommand(context_path)
    command.run()


@cli.command("calc")
@click.option('--context_path', required=True, default=DEFAULT_CONTEXT_FILE_PATH, type=str, help="Path to context")
def __calc(context_path):
    command = CalcCommand(context_path)
    command.run()


@cli.command("list-minio-files")
@click.option('--context_path', required=True, default=DEFAULT_CONTEXT_FILE_PATH, type=str, help="Path to context")
def __list(context_path):
    command = ListMinioBucketObjectsCommand(context_path)
    command.run()

@cli.command("umbrella-test")
def __devtest():
    command = UmbrellaCommand(folder_path="./RESULTS_FOLDER", input_params={"systems": {"gitlab": {"url": "https://gitlab.com"}}})
    command.run()
