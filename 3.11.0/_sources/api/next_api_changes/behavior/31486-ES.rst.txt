New environment variable to ignore system fonts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System fonts may be ignored by setting the :envvar:`MPL_IGNORE_SYSTEM_FONTS`; this
suppresses searching for system fonts (in known directories or via some
platform-specific subprocess) as well as limiting the results from `.FontManager.findfont`.
