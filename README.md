# SCOSignalProcessing
![Tests](https://github.com/UoNPhysics/SignalProcessing-georgeh1ll/actions/workflows/classroom.yml/badge.svg)

A project to build a signal processing oscilloscope. The main code of the project is in python. This code contains functions that generate a signal, Fourier transform that signal and then display both the original signal and the Fourier power.

The idea of this task is to process a generated signal and recover the Fourier power with correctly attributed frequencies. Once this is achieved the basic display can be extended in a variety of ways.

You should only need to modify `main.py`, and you do not need to change any of the tests.

# Tasks

1. Download the repository to your local machine using Github Desktop or another Git client.
2. Change this file (`README.md`), inserting your GitHub username into the URL at the top, replacing where it says `USERNAME`. This will display whether you have passed the unit tests for this project.
3. Read through the `main.py` file in the `signalprocessing` folder. You will need to add code to this file. 
4. Check you can run the tests. If you can't revisit the 'version control' section.
5. Create and switch to a new branch **before** making any changes.
6. Insert code to generate a sine wave. Use the first test to check your function.
7. When you have finished implementing your function, commit your code along with a description of what you have done.
8. Push this commit to the Github repository and create a pull request to merge in your changes to the main branch. 
9. Insert code to Fourier transform your signal, returning the power and associated frequencies as specified. Use the second test to check your function.
10. When you have finished implementing your function, commit, push and merge your changes.
11. Uncomment the plotting section within `main.py`. You should now see your signal and the Fourier transform power plotted. The slider will allow you to change the input frequency. Check Moodle for more details.
12. Check that the returned maximum power frequency corresponds with your input frequency by moving the slider.
13. Getting this far correctly gets 40\% of the marks. Higher marks are obtained by adding functionality to your oscilloscope. 

