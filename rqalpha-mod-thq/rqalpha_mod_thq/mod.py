from rqalpha.interface import AbstractMod
from .thq_datasource import THQDataSource

class thqDataMod(AbstractMod):
    def start_up(self, env, mod_config):
        print(">>> THQ_Mod.start_up")
        env.set_data_source(THQDataSource(env.config.base.data_bundle_path, {}))

    def tear_down(self, success, exception=None):
        print(">>> THQ_Mod.tear_down")
