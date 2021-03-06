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

class GetEcosystemActions(catoclient.catocommand.CatoCommand):

    Description = 'Gets the Actions for an Ecosystem.'
    Options = [Param(name='ecosystem', short_name='e', long_name='ecosystem',
                     optional=False, ptype='string',
                     doc='Value can be either an ecosystem id or ecosystem name.')]
    def main(self):

        results = self.call_api('ecoMethods/get_ecosystem_actions', ['ecosystem'])
        print(results)

