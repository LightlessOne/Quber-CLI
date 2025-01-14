## Development Guide

<!-- TOC -->
  * [Development Guide](#development-guide)
    * [Adding new commands](#adding-new-commands)
    * [Building locally using provided scripts](#building-locally-using-provided-scripts-)
    * [Running CLI](#running-cli)
    * [Working with external services](#working-with-external-services)
<!-- TOC -->

### Adding new commands

New commands should all extend `ExecutionCommand` class. This project provides several examples of commands that work via context files (and it's the intended way of using qubership-common-library, since it's made for using in devops pipelines)

Library itself provides methods of working with context and params files.

The most straightforward example is `SampleStandaloneExecutionCommand`, which is mapped to `@cli.command("run-sample")` CLI command.

It expects to receive location of [`context.yaml` file](../TESTS/context.yaml) (or looks for it in working directory), which points to locations of [input parameters](../TESTS/params.yaml) and where to put resulting report.

The usual `ExecutionCommand` lifecycle consists of
- validating required input parameters (that will be automatically parsed from context)
- performing work and logging its results per agreed contract
 
In our example - this sample command just sums up two integer parameters and writes them into `results.yaml`


### Building locally using provided scripts 

This project provides a set of [scripts](../scripts) that help with local development - cleaning up workspace, building CLI as a ZIPAPP, and example of how it can be executed.

There's also a separate python script ([check_test_results.py](../scripts/python/check_test_results.py)) used by GitHub Actions to validate test results and create workflow summary.


### Running CLI

Use (and modify) provided [test.sh](../scripts/test.sh) to run CLI and test your scenarios during development.

The [TESTS](../TESTS) folder also contains examples of context/params configurations.

In current configuration, it's expected to get `result.yaml` and `result_calc.yaml` files next to existing context with results of test commands.


### Working with external services
- [MiniO Guide](../docs/minio.md)
- TBD...




