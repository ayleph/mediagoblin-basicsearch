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

from mediagoblin.plugins.basicsearch import forms as search_forms
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

    form = search_forms.SearchForm(request.form)

    if (request.GET.get('query') != None and
        request.GET.get('query') != ''):
        terms = []
        skipterms = [ 'a', 'an', 'the', 'of' ]
        for query in request.GET.get('query').split():
            lquery = query.lower()
            if lquery not in skipterms:
                terms.append('%' + lquery + '%')

        media_entry_statements = []
        media_tag_statements = []
        if len(terms) == 0:
           media_entry_statements.append(True)
           media_tag_statements.append(True)
        else:
           for term in terms:
              media_entry_statements.append(MediaEntry.title.ilike(term))
              media_entry_statements.append(MediaEntry.description.ilike(term))
              media_tag_statements.append(MediaTag.name.ilike(term))

        matches = MediaEntry.query.filter(
            and_(
                MediaEntry.state == u'processed',
                or_(
                    and_(
                        MediaEntry.id==MediaTag.media_entry,
                        *media_tag_statements
                    ),
                    *media_entry_statements
                )
            )).order_by(MediaEntry.title)

        pagination = Pagination(page, matches)
        media_entries = pagination()

    return render_to_response(
        request,
        'mediagoblin/plugins/basicsearch/results.html',
        {'media_entries': media_entries,
         'pagination': pagination,
         'form': form})
