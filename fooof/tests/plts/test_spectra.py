"""Tests for fooof.plts.spectra."""

from pytest import raises

import numpy as np

from fooof.tests.tutils import plot_test
from fooof.tests.settings import TEST_PLOTS_PATH

from fooof.plts.spectra import *

###################################################################################################
###################################################################################################

@plot_test
def test_plot_spectrum(tfm, skip_if_no_mpl):

    plot_spectrum(tfm.freqs, tfm.power_spectrum)

    # Test with logging both axes
    plot_spectrum(tfm.freqs, tfm.power_spectrum, True, True, save_fig=True,
                  file_path=TEST_PLOTS_PATH, file_name='test_plot_spectrum.png')

@plot_test
def test_plot_spectra(tfg, skip_if_no_mpl):

    # Test with 1d inputs - 1d freq array and list of 1d power spectra
    plot_spectra(tfg.freqs, [tfg.power_spectra[0, :], tfg.power_spectra[1, :]],
                 save_fig=True, file_path=TEST_PLOTS_PATH, file_name='test_plot_spectra_1d.png')

    # Test with multiple freq inputs - list of 1d freq array and list of 1d power spectra
    plot_spectra([tfg.freqs, tfg.freqs], [tfg.power_spectra[0, :], tfg.power_spectra[1, :]],
                 save_fig=True, file_path=TEST_PLOTS_PATH,
                 file_name='test_plot_spectra_list_of_1d.png')

    # Test with 2d array inputs
    plot_spectra(np.vstack([tfg.freqs, tfg.freqs]),
                 np.vstack([tfg.power_spectra[0, :], tfg.power_spectra[1, :]]),
                 save_fig=True, file_path=TEST_PLOTS_PATH, file_name='test_plot_spectra_2d.png')

    # Test with labels
    plot_spectra(tfg.freqs, [tfg.power_spectra[0, :], tfg.power_spectra[1, :]], labels=['A', 'B'],
                 save_fig=True, file_path=TEST_PLOTS_PATH, file_name='test_plot_spectra_labels.png')

@plot_test
def test_plot_spectrum_shading(tfm, skip_if_no_mpl):

    plot_spectrum_shading(tfm.freqs, tfm.power_spectrum, shades=[8, 12], add_center=True,
                          save_fig=True, file_path=TEST_PLOTS_PATH,
                          file_name='test_plot_spectrum_shading.png')

@plot_test
def test_plot_spectra_shading(tfg, skip_if_no_mpl):

    plot_spectra_shading(tfg.freqs, [tfg.power_spectra[0, :], tfg.power_spectra[1, :]],
                         shades=[8, 12], add_center=True, save_fig=True, file_path=TEST_PLOTS_PATH,
                         file_name='test_plot_spectra_shading.png')

    # Test with **kwargs that pass into plot_spectra
    plot_spectra_shading(tfg.freqs, [tfg.power_spectra[0, :], tfg.power_spectra[1, :]],
                         shades=[8, 12], add_center=True, log_freqs=True, log_powers=True,
                         labels=['A', 'B'], save_fig=True, file_path=TEST_PLOTS_PATH,
                         file_name='test_plot_spectra_shading_kwargs.png')

@plot_test
def test_plot_spectra_yshade(skip_if_no_mpl, tfg):

    freqs = tfg.freqs
    powers = tfg.power_spectra

    # Invalid 1d array, without shade
    with raises(ValueError):
        plot_spectra_yshade(freqs, powers[0])

    # Valid 1d array with shade
    plot_spectra_yshade(freqs, np.mean(powers, axis=0), shade=np.std(powers, axis=0),
                        save_fig=True, file_path=TEST_PLOTS_PATH,
                        file_name='test_plot_spectra_yshade1.png')

    # 2d array
    plot_spectra_yshade(freqs, powers, save_fig=True, file_path=TEST_PLOTS_PATH,
                        file_name='test_plot_spectra_yshade2.png')
