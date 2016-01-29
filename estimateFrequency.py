import wave
import struct
import numpy

# reference:
# http://stackoverflow.com/questions/604453/analyze-audio-using-fast-fourier-transform

# data:
# http://www.mediacollege.com/audio/tone/download/
# http://www.classicgaming.cc/classics/pacman/sounds.php

VECTORIZED_MAGNITUDE = numpy.vectorize(lambda x: x.real**2 + x.imag**2)

def estimateFrequency(fname):
    ((_, _, framerate, total_frames, _, _), wav_data) = wavLoad(fname)
    nframes = int(framerate / 20)
    frequency_spacing = float(framerate) / nframes
    frequencies = []

    for i in range(nframes, total_frames, nframes):
        fft = numpy.fft.fft(wav_data[(i - nframes):i])
        frequency_magnitudes = VECTORIZED_MAGNITUDE(fft)
        estimated_index = findMaxIndex(frequency_magnitudes[1: nframes/2])
        estimated_frequency = (estimated_index + 1) * frequency_spacing
        frequencies.append(estimated_frequency)
    return frequencies

def wavLoad(fname):
    wav = wave.open(fname, "r")
    params = (nchannels, sampwidth, _, nframes, _, _) = wav.getparams()
    frames = wav.readframes(nframes * nchannels)
    fmt = "%dB" % (nframes * nchannels) if sampwidth == 1 else "%dH" % (nframes * nchannels)

    return (params, struct.unpack_from(fmt, frames))

def findMaxIndex(array):
    m = max(array)
    return [i for i, j in enumerate(array) if j == m][0]

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-source', default='./data/range.wav', help='wav file to be analyzed; defaults to ./data/range.wav')
    args = parser.parse_args()

    data = estimateFrequency(args.source)
    plt.scatter(range(0, len(data)), data)
    plt.show()