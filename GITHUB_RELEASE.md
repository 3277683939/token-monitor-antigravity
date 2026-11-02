# Antigrative Dashboard v0.8.19

Fix extra icons and misaligned selection when an auxiliary pane narrows the composer.

- Compact mode now shows one glyph per control. Hidden warning and collection-progress icons no longer appear alongside the normal cache icon.
- The cache glyph stays centered in its button; the keyboard focus outline is inset so it is not clipped.
- Warning and processing states replace the cache glyph instead of adding extra controls. This fixes shared App/IDE inline UI; CLI behavior is unchanged.
- Add browser coverage for three languages, two themes, four collection states, compact/full transitions, popup anchoring and animation cleanup. The bug existed before the Argon integration.

## Install or update

- App: context details → **⋯ → Check for updates**, or extract `antigrative-dashboard-0.8.19.zip` and run `python manage.py install` (`python3` on Linux/macOS).
- Standalone IDE: install `antigrative-dashboard-ide-0.8.19.vsix` using **Install from VSIX…**.
- Fully quit and reopen the relevant host after updating. Existing statistics and preferences are retained. SHA-256 files accompany both packages.

[Compatibility](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard/blob/v0.8.19/COMPATIBILITY.md)
