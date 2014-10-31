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
from mediagoblin import mg_globals
from mediagoblin.db.base import Session
from mediagoblin.db.models import (MediaEntry, MediaTag, Collection,
                                   CollectionItem, User)
from mediagoblin.decorators import uses_pagination
from mediagoblin.tools.response import render_to_response
from mediagoblin.tools.pagination import Pagination

from mediagoblin.plugins.search import forms as search_forms
from mediagoblin.tools.translate import lazy_pass_to_ugettext as _
from mediagoblin.meddleware.csrf import csrf_exempt
from sqlalchemy import and_, or_

import logging
_log = logging.getLogger(__name__)

@csrf_exempt
@uses_pagination
def search_results_view(request, page):

    media_entries = None
    pagination = None
    query = None

    form = search_forms.SearchForm(
        request.form)

    #if request.method == 'GET':
    if request.GET.get('query') != None:
        if request.GET.get('query') != '':
            query = '%' + request.GET.get('query') + '%'

        #cursor = MediaEntry.query.filter(MediaEntry.uploader==1).\

            matches = MediaEntry.query.filter(
                and_(
                    MediaEntry.state == u'processed',
                    or_(
                        MediaEntry.title.ilike(query),
                        MediaEntry.description.ilike(query)
                    )
                )).order_by(MediaEntry.created.desc())

            #_log.info(matches)

            pagination = Pagination(page, matches)
            media_entries = pagination()

    return render_to_response(
        request,
        'mediagoblin/plugins/search/results.html',
        {'media_entries': media_entries,
         'pagination': pagination,
         'form': form})
