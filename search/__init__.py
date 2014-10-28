# GNU MediaGoblin -- federated, autonomous media hosting
# Copyright (C) 2011, 2012 MediaGoblin contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import logging
import os
from pkg_resources import resource_filename

from mediagoblin.tools.pluginapi import (register_template_path,
                                        register_routes,
                                        register_template_hooks)
#from mediagoblin.plugins.search.views import (get_root_view)
from mediagoblin.tools.staticdirect import PluginStatic


_log = logging.getLogger(__name__)


_setup_plugin_called = 0

def setup_plugin():
    global _setup_plugin_called
    _log.info('Setting up search...')

    my_plugin_dir = os.path.dirname(__file__)
    template_dir = os.path.join(my_plugin_dir, 'templates')
    register_template_path(template_dir)
    register_routes([
        ('search-results', '/search',
        'mediagoblin.plugins.search.views:search_results_view')])

hooks = {
    'setup': setup_plugin,
    'static_setup': lambda: PluginStatic(
        'search',
        resource_filename('mediagoblin.plugins.search', 'static')
     ),
}
