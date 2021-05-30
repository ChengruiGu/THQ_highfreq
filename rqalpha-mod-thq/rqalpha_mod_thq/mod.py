from rqalpha.interface import AbstractMod
from .thq_datasource import THQDataSource

class thqDataMod(AbstractMod):
    def start_up(self, env, mod_config):
        print(">>> HelloWorldMod.start_up")
        env.set_data_source(THQDataSource(env.config.base.data_bundle_path, {}))

    def tear_down(self, success, exception=None):
        print(">>> HelloWorldMod.tear_down")
