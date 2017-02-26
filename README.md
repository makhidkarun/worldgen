# worldgen
World generation for the Cepheus Engine and similar OGL 2d6 Sci-Fi games.
v1.3, February 26, 2017.
Generates old-school SEC files compatible with various Traveller-type applications.
This is open source code, feel free to use it for any purpose.
Contact the author at golan2072@gmail.com.

v1.3 changelog:
- Added Linux support. Tested on Linux Lite 3.2.

v1.2 changelog:
- Fixed the formatting bug. Output SEC file should now be perfectly formatted.
- The savefile function is no longer case-sensitive in recognizing existing files for over-writing.
- Improved code for the Pseudo Hex Converter function.
- Thanks to Leam Hall and other very kind people for their input!

v1.1 changelog:
- Fixed a major bug where an empty string would have been generated instead of a trade code when there was a single trade code.
- Population numbers can no longer be negative.

v1.05 changelog:
- Error message now shows correctly on wrong input on the main menu.
- Fixed a bug in the definition of the "Ba" ("Barren") trade code. Should now appear correctly.

v1.0 notes:
- First full-scale stable release
- Tested on Windows 7 64bit
- This is a remake of an old script I built in 2010. I tried writing a much clearer, readable, better-documented code and avoid the programming mistakes I commited in my old script.
