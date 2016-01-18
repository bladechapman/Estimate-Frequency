# Estimate Frequency
A quick script to estimate the primary frequencies of wav files. Operates by taking 20 frequency 'windows' per second, and performing a Fast Fourier Transform on these windows to extract the primary frequencies. The frequency with the highest magnitude is deemed the primary frequency, and plotted.

# Usage
```
usage: estimateFrequency.py [-h] [-source SOURCE]

optional arguments:
  -h, --help      show this help message and exit
  -source SOURCE  wav file to be analyzed; defaults to ./data/range.wav
```

# Dependencies
```
pip install -r requirements.txt
```
Requires numpy and matplotlib

# References
[data source (tones)](http://www.mediacollege.com/audio/tone/download/)<br>
[data source (pacman)](http://www.classicgaming.cc/classics/pacman/sounds.php)<br>
[reference](http://stackoverflow.com/questions/604453/analyze-audio-using-fast-fourier-transform)
