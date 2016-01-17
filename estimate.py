import wave
import struct
import numpy

# reference:
# http://stackoverflow.com/questions/604453/analyze-audio-using-fast-fourier-transform

# data:
# http://www.mediacollege.com/audio/tone/download/

def estimateFrequency(fname, nframes):
    (wav_info, wav_data) = wavLoad(fname)

    data_256 = wav_data[0:nframes]
    data_256_np = numpy.array(data_256)
    data_256_fft = numpy.fft.fft(data_256_np)

    frequency_magnitudes = resolveMagnitudes(data_256_fft)
    frequency_spacing = float(wav_info[2]) / nframes

    estimated_index = findMaxIndex(frequency_magnitudes[0: nframes/2])
    print 'estimated frequency: %dHz' % (frequency_spacing * estimated_index)

def wavLoad(fname):
   wav = wave.open(fname, "r")
   (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
   frames = wav.readframes(nframes * nchannels)
   return (wav.getparams(), struct.unpack_from("%dh" % (nframes * nchannels), frames))

def resolveMagnitudes(carray):
    vectorized_magnitude = numpy.vectorize(lambda x: numpy.sqrt(x.real**2 + x.imag**2))
    return vectorized_magnitude(carray)

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
    estimateFrequency('./data/10000.wav', 3000)