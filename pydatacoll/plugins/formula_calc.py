from pydatacoll.plugins import BaseModule
import pydatacoll.utils.logger as my_logger

logger = my_logger.get_logger('FormulaCalc')


class FormulaCalc(BaseModule):
    not_implemented = True

    async def stop(self):
        pass

    async def start(self):
        pass
