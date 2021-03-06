#########################################################################
# Copyright 2011 Cloud Sidekick
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#########################################################################

import catoclient.catocommand
from catoclient.param import Param

class GetEcotemplate(catoclient.catocommand.CatoCommand):

    Description = 'Gets an Ecotemplate object.'
    Options = [Param(name='ecotemplate', short_name='e', long_name='ecotemplate',
                     optional=False, ptype='string',
                     doc='Value can be either an Ecotemplate id or Ecotemplate name.')]

    def main(self):

        return self.call_api('ecoMethods/get_ecotemplate', ['ecotemplate'])

    def main_cli(self):
        results = self.main()
        print(results)

