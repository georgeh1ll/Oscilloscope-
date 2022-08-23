from signalprocessor import sinf
import numpy as np

from signalprocessor.main import fourier_func

def test_signal_generation():
    t_max=3
    n_points = 300
    sig_freq = 1

    test_points = [0, 50, 100, 150, 200, 250]
    test_answers = [0., -0.0105068055189361, 0.02101245112847523, -0.03151577704726979, 0.04201562375005677, -0.05251083209566474 ]
    tolerance = 1.e-6

    t = np.linspace(0, t_max, n_points)
    signal_amplitude = sinf(t,sig_freq)

    for (point, answer) in zip(test_points, test_answers):
        calculated_amp = signal_amplitude[point]
        assert np.abs(calculated_amp-answer) < tolerance, f"The amplitude of point {point} was expected to be {answer}, but was calculated to be {calculated_amp}."

def test_power_and_freq():
    t_max=3
    n_points = 300
    sig_freq = 1

    test_points = [1, 2, 3, 4]
    test_answers_power = [0.00046456552344201386, 0.004715246604514724, 74.724873693238, 0.010032901044703203]
    test_answers_freq = [1./3.,2./3.,1.,4./3.]
    tolerance = 1.e-6

    t = np.linspace(0, t_max, n_points)
    signal_amplitude = sinf(t,sig_freq)
    power,freq = fourier_func(signal_amplitude,t_max)

    for (point, answerp, answerf) in zip(test_points, test_answers_power, test_answers_freq):
        calculated_power = power[point]
        assert np.abs(calculated_power - answerp) < tolerance, f"The power of point {point} was expected to be {answerp}, but was calculated to be {calculated_power}."
        calculated_freq = freq[point]
        assert np.abs(calculated_freq - answerf) < tolerance, f"The frequency of point {point} was expected to be {answerf}, but was calculated to be {calculated_freq}."