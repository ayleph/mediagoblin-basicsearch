=======================
mediagoblin-basicsearch
=======================

This plugin adds support for displaying media in Gnu MediaGoblin based on simple search queries. In its current state, the search function will query the title and description fields of processed media entries for the exact input phrase (case-insensitive). Multiple search terms are not supported at this time.

Set up the search plugin
========================

1. Clone the search plugin repository from GitHub::

    git clone https://github.com/ayleph/mediagoblin-basicsearch.git

2. Copy the basicsearch folder to your MediaGoblin plugin path::

    cp -r basicsearch /path/to/mediagoblin/mediagoblin/plugins/
    
3. Add the following entry to your mediagoblin_local.ini file in the ``[plugins]`` section::

    [[mediagoblin.plugins.basicsearch]]

Configure the search plugin
===========================

The search plugin adds a search link to the top header bar of the MediaGoblin instance. You may specify the display style of the search link in your mediagoblin config file. There are three options for the search link display style.

* ``link`` displays a normal text link next to the Log In link. This is the default display style.
* ``button`` displays an action button link next to the Log In link.
* ``none`` does not display a link. This is useful if you want to create your own search link in a user_dev template or custom theme.

If you choose to specify the display style, add it to your mediagoblin_local.ini like this::

    [[mediagoblin.plugins.basicsearch]]
    SEARCH_LINK_STYLE = 'link'

If you choose style ``none`` and wish to create your own search link, use the syntax below as a guide::

    <a href="{{ request.urlgen('mediagoblin.plugins.basicsearch') }}">
    {%- trans %}Search{% endtrans -%}
    </a>
