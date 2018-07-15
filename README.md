# WaterAudio
Adds a watermark to an audio clip
## Introduction

This module uses pydub, therefore requires that it is succesfully installed before being used.

[Download PyDub from here](https://github.com/jiaaro/pydub "Pydub's git")

### How to use

1) Successfully import the module into your own module

```python
from . import audio_lib as AudioLib
```

2) Choose what audio you want to be covered in an watermark

```python
AudioLib.assign_music("Music.mp3")
```

3) Choose what audio you want to be your watermark and how long it will pause in between loops (default 500 milliseconds)

```python
 AudioLib.assign_watermark("Watermark.mp3")
```
4) Export the file

```python
 file = AudioLib.export("export.mp3","mp3")
```

#### Everything together
```python
from . import audio_lib as AudioLib
if __name__ == "__main__":
  AudioLib.assign_music("Music.mp3")
  AudioLib.assign_watermark("Watermark.mp3")
  file = AudioLib.export("export.mp3","mp3")
```
