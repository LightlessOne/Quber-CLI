import os, sys, logging, urllib3, click

from quber_cli.minio_commands import ListMinioBucketObjectsCommand
from quber_cli.piped_commands import AddIntegers, SaveResultToFile, DoStuffUsingContext
from quber_cli.sample_command import SampleStandaloneExecutionCommand, CalcCommand
from qubership_pipelines_common_library.v1.execution.exec_logger import ExecutionLogger

DEFAULT_CONTEXT_FILE_PATH = 'context.yaml'


@click.group(chain=True)
def cli():
    #logging.basicConfig(stream=sys.stdout, format=ExecutionLogger.DEFAULT_FORMAT, level=logging.INFO)
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


# QUBER COMMANDS:

@cli.command("add-integers")
@click.option('--arg1', required=True, type=int)
@click.option('--arg2', required=True, type=int)
def __add_ints(arg1, arg2):
    result_dict =AddIntegers(arg1=arg1, arg2=arg2).run()
    print(result_dict["result"])  # Prints to stdout for piping to other commands


@cli.command("add-integers-and-then-ten-more")
@click.option('--arg1', required=True, type=int)
@click.option('--arg2', required=True, type=int)
def __add_ints_more(arg1, arg2):
    result_dict = AddIntegers(arg1=arg1, arg2=arg2).run()
    result_dict = AddIntegers(arg1=result_dict["result"], arg2=10).run()
    print(result_dict["result"])


@cli.command("save")
@click.option('--data', required=True, type=str)
@click.option('--result_path', required=True, type=str)
def __save_to_file(data, result_path):
    result_dict = SaveResultToFile(data=data, result_path=result_path).run()
    print(result_dict["data"])


@cli.command("do-stuff-with-context")
@click.option('--context_path', required=True, default=DEFAULT_CONTEXT_FILE_PATH, type=str, help="Path to context")
@click.option('--project', required=True, type=str)
@click.option('--branch', required=True, type=str)
@click.option('--path', required=True, type=str)
def __do_stuff_with_context(context_path, project, branch, path):
    result_dict = DoStuffUsingContext(context_path, project=project, branch=branch, path=path).run()
    print(result_dict["result"])