y_n = scipy.signal.convolve(x_n,h_n)
y_n_file_name = "echo.wav"
scipy.io.wavfile.write(y_n_file_name,sample_rate,
                       y_n[:no_of_samples].astype(np.int16))