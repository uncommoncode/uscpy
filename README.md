# About uscpy
uscpy (pronounced Microscopy) is a collection of command line tools and a library useful for common microscopy image processing tasks.

The command line tools are located in the root directory, and the library is provided in the ```uscpy``` directory.


# Dependencies
This code has several dependencies:

 * Python 2.7
 * numpy
 * OpenCV 2.4+

Other versions may work but have not been tested.

## Suggested Mac OS X Installation
While a good linux distro makes it trivial to install open source tools, things can be slightly more difficult on Mac OS X.

There are many ways to perform these steps but the following combination of homebrew and pip typically makes the steps repeatable and condensed across computers.

The recommended way to install dependencies on Mac OS X is with [homebrew](http://brew.sh/). After installing homebrew, which requires [XCode](https://developer.apple.com/xcode/downloads/), install homebrew's version of python and then use [pip](http://pip.readthedocs.org/en/latest/) to install numpy.

At this point, install ffmpeg with homebrew:

```
brew install ffmpeg
```

After ffmpeg ins installed, install OpenCV:

```
brew install opencv --with-ffmpeg
```

Additional References:

 * <https://trac.ffmpeg.org/wiki/CompilationGuide/MacOSX>
 * <http://joernhees.de/blog/2014/02/25/scientific-python-on-mac-os-x-10-9-with-homebrew/>
 * <https://groups.google.com/forum/#!topic/pupil-discuss/wGRr7P9nvKc>


# Command Line Tools
The command line tools are located in the root directory, and are described in the following sections.

## Image Stabilization
Given an input video, create an output mp4 video:

```
python stabilizer.py input-video.avi output-video.m4v
```

Further usage is described with the --help flag:

```
python stabilizer.py --help
```

For a 956px x 900px 115 frame video the stabilizer takes about 10 seconds to complete on a 1.7 GHz i7 MacBook Air.
