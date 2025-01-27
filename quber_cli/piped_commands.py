import logging
import traceback

from qubership_pipelines_common_library.v1.execution.exec_command import ExecutionCommand
from qubership_pipelines_common_library.v1.git_client import GitClient
from qubership_pipelines_common_library.v1.utils.utils_file import UtilsFile


class QuberCommand(ExecutionCommand):

    def __init__(self, context_path=None, **kwargs):
        if context_path:
            super().__init__(context_path)
        self.input = kwargs

    def run(self):
        try:
            if not self._validate():
                logging.error("Status: FAILURE")
                return None
            return self._execute()
        except Exception as e:
            logging.error(traceback.format_exc())

    def _validate(self):
        return True

    def _has_all_args(self, argument_names: list[str]):
        for key in argument_names:
            if not key in self.input:
                logging.error(f"Parameter '{key}' is mandatory but not defined")
                return False
        return True





# This QuberCommand is not using context
class AddIntegers(QuberCommand):

    def _validate(self):
        argument_names = ["arg1", "arg2"]
        return self._has_all_args(argument_names)

    def _execute(self):
        result_dict = {
            "result": self.input["arg1"] + self.input["arg2"]
        }
        return result_dict  # Returns dict to integrate with another commands from code


class DoStuffUsingContext(QuberCommand):

    def _validate(self):
        argument_names = ["project", "branch", "path"]
        context_param_names = [
            "paths.input.params",
            "systems.git.host",
            # "systems.git.username",
            # "systems.git.password",
        ]
        return self._has_all_args(argument_names) and self.context.validate(context_param_names)

    def _execute(self):
        git = GitClient(self.context.input_param_get("systems.git.host"), "", "")
                        #self.context.input_param_get("systems.git.username"),
                        #self.context.input_param_get("systems.git.password"))
        # just an example
        file_content = git.get_file_content(self.input["project"], self.input["branch"], self.input["path"])
        result_dict = {
            "result": file_content
        }
        return result_dict


class SaveResultToFile(QuberCommand):

    def _validate(self):
        argument_names = ["data", "result_path"]
        return self._has_all_args(argument_names)

    def _execute(self):
        UtilsFile.write_text_utf8(self.input["result_path"], self.input["data"])
        return self.input
