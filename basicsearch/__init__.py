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
from pkg_resources import resource_filename
import os
import logging

from mediagoblin.tools import pluginapi
from mediagoblin.tools.staticdirect import PluginStatic
_log = logging.getLogger(__name__)


PLUGIN_DIR = os.path.dirname(__file__)


def setup_plugin():
    _log.info('Setting up basic search...')
    config = pluginapi.get_config('mediagoblin.plugins.basicsearch')

    routes = [
        ('mediagoblin.plugins.basicsearch',
         '/search/',
         'mediagoblin.plugins.basicsearch.views:search_results_view')]

    pluginapi.register_routes(routes)
    pluginapi.register_template_path(os.path.join(PLUGIN_DIR, 'templates'))

    search_link_style = config.get('SEARCH_LINK_STYLE')
    _log.debug("Search link style was specified as: %r", search_link_style)
    if search_link_style == 'button':
        header_template = '/mediagoblin/plugins/basicsearch/search_link_button.html'
    elif search_link_style == 'none':
        header_template = '/mediagoblin/plugins/basicsearch/search_link_none.html'
    else:
        header_template = '/mediagoblin/plugins/basicsearch/search_link_default.html'

    pluginapi.register_template_hooks(
        {'header_extra': header_template})

hooks = {
    'setup': setup_plugin
}
