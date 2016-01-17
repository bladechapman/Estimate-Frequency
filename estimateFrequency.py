import wave
import struct
import numpy

# reference:
# http://stackoverflow.com/questions/604453/analyze-audio-using-fast-fourier-transform

# data:
# http://www.mediacollege.com/audio/tone/download/

VECTORIZED_MAGNITUDE = numpy.vectorize(lambda x: x.real**2 + x.imag**2)

def estimateFrequency(fname, nframes):
    (wav_info, wav_data) = wavLoad(fname)
    total_frames = wav_info[3]
    frequency_spacing = float(wav_info[2]) / nframes
    frequencies = []
    for i in range(nframes, total_frames, nframes):
        fft = numpy.fft.fft(wav_data[(i - nframes):i])
        frequency_magnitudes = VECTORIZED_MAGNITUDE(fft)
        estimated_index = findMaxIndex(frequency_magnitudes[0: nframes/2])
        estimated_frequency = estimated_index * frequency_spacing
        frequencies.append(estimated_frequency)
    return frequencies

def wavLoad(fname):
   wav = wave.open(fname, "r")
   params = (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
   frames = wav.readframes(nframes * nchannels)
   return (params, struct.unpack_from("%dh" % (nframes * nchannels), frames))

def findMaxIndex(array):
    current_max_value = float('-inf')
    current_max_index = 0
    for i in range(0, len(array)):
        num = array[i]
        if num > current_max_value:
            current_max_value = num
            current_max_index = i
    return current_max_index

if __name__ == '__main__':
    import profile
    import matplotlib.pyplot as plt

    plt.plot(estimateFrequency('./data/range.wav', 3000))
    plt.show()