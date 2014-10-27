=====================
mediagoblin-search
=====================

This plugin adds support for displaying media in Gnu MediaGoblin based on simple search queries.

Set up the search plugin
===========================

1. Clone the search plugin repository from GitHub::

    git clone https://github.com/ayleph/mediagoblin-search.git

2. Copy the search folder to your MediaGoblin plugin path::

    cp -r search /path/to/mediagoblin/mediagoblin/plugins/
    
3. Add the following entry to your mediagoblin_local.ini file in the ``[plugins]`` section::

    [[mediagoblin.plugins.search]]
