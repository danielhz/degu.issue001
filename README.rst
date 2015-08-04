.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
danielhz.issue001
==============================================================================

This addon reproduce an issue that I first documented in the Plone forum at
https://community.plone.org/t/dexterity-content-types-does-not-appear-in-the-portal-globalnav/849

To reproduce this issue you must:

1. Run bootstrap/buildout.
2. Create a new plone site activating the add-ons:
   - plone.app.multilingual
   - danielhz.issue001
3. Go to "Site Setup" > "Multilingual Settings" and set two languages.
   I set English and Español.
4. Create a new Task "Task" inside "/en/"
5. Create a new TaskFolder "Task folder" inside "/en/"

After these steps, the elements "Task" and "Task folder" does not appear in
the portal.globalnav.

License
-------

The project is licensed under the GPLv2.
