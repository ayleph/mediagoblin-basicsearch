=======================
mediagoblin-basicsearch
=======================

This plugin adds support for displaying media in GNU MediaGoblin based 
on simple search queries. In its current state, the search function 
will query the title and description fields of processed media entries 
for the exact input phrase (case-insensitive). Multiple search terms 
are searched with a match on any term included in the results.

This plugin relies on the ``header_extra`` template hook which was 
introduced in the MediaGoblin 0.7.2-dev codebase. If you're running a 
previous version of GNU MediaGoblin, the search link will not appear on 
your instance unless you apply the change in commit aa50cab_.

Set up the search plugin
========================

1. Clone the search plugin repository from GitHub.

::

   $ git clone https://github.com/ayleph/mediagoblin-basicsearch.git

2. Copy the basicsearch folder to your MediaGoblin plugin path.

::

  $ cp -r mediagoblin-basicsearch/basicsearch /path/to/mediagoblin/mediagoblin/plugins/
    
3. Enable the mediagoblin-basicsearch plugin by adding the following 
   line to the ``[plugins]`` section of your mediagoblin.ini file (or 
   mediagoblin_local.ini file if you're using an older release).

::

    [[mediagoblin.plugins.basicsearch]]
    
4. Restart your MediaGoblin instance for the config file changes to be  
   effective.

Configure the search plugin
===========================

The search plugin adds a search link to the top header bar of the 
MediaGoblin instance. You may specify the display style of the search 
link in your mediagoblin config file. There are three options for the 
search link display style.

* ``link`` displays a normal text link next to the Log In link. This is 
  the default display style.

* ``button`` displays an action button link next to the Log In link.

* ``none`` does not display a link. This is useful if you want to 
  create your own search link in a user_dev template or custom theme.

If you choose to specify the display style, add it to your 
mediagoblin.ini file like this.

::

  [[mediagoblin.plugins.basicsearch]]
  SEARCH_LINK_STYLE = 'link'

If you choose style ``none`` and wish to create your own search link, 
use the syntax below as a guide.

::

  <a href="{{ request.urlgen('mediagoblin.plugins.basicsearch') }}">
  {%- trans %}Search{% endtrans -%}
  </a>

.. external links

.. _aa50cab: http://git.savannah.gnu.org/gitweb/?p=mediagoblin.git;a=commitdiff;h=aa50cab0dcfcdc3606893b6cbded4227190f8980
