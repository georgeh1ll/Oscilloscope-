import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
from typing import Tuple
from scipy import signal
from math import pi
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation


# Function that plots sine
def sinf(t:np.ndarray, sin_freq:float) -> np.ndarray:
    """Generates sine values at the supplied points x with supplied frequency  

    Args:
        t (np.ndarray): Time sequence to generate values (t=1 is end of first oscillation at 1 Hz).
        sin_freq (float): The frequency required (in Hz).


    Returns:
        np.ndarray: The amplitude of a sine wave at the supplied times, with frequency sin_freq
    """
    sinewave=np.sin(2*np.pi*sin_freq*t)

    return(sinewave)

    pass

def fourier_func(signal_amplitude:np.ndarray, t_max:float) -> Tuple[np.ndarray, np.ndarray]:
    """Calculates the power and equivalent frequency for the first half of the k-modes for the supplied signal amplitude.  

    Args:
        signal_amplitude (np.ndarray): The supplied signal amplitudes, uniformly sampled from t = 0 to t = t_max
        t_max (float): The maximum time

    Returns:
        (np.ndarray, np.ndarray): A tuple of numpy arrays, the first being the power values and the second being the freqencies corresponding to the power.
    """
    n=len(signal_amplitude)

    f_min=1/t_max
    f_max=(n/2)*(1/t_max)
    
    
    frequencies=np.linspace(0,f_max,n)
    frequencies=np.round((frequencies*3))
    frequencies=frequencies/3
    frequencies =frequencies[0::2]
    
    fourier_transform=np.fft.fft(signal_amplitude)
    fourier_transform_conj=np.conjugate(fourier_transform)
    
    power=(fourier_transform*fourier_transform_conj)/n
    power=np.abs(power)
    power = power[:len(power)//2]

    return(power,frequencies)
pass
    

"""Basic oscilloscope figure layout with signal window, Fourier power window, 
    frequency slider and exit button
"""

# Event when exit button is pressed
def exit_button(event):
    plt.close('all')

# Update the signal and power plots when the frequency slider is moved    
def freq_slider(val):
    global t, signal_line_handle, fourier_line_handle
    signal_amplitude = sinf(t, val)
    signal_line_handle.set_ydata(signal_amplitude)
    power, freq = fourier_func(signal_amplitude,t_max)
    fourier_line_handle.set_ydata(power)
    fourier_line_handle.set_xdata(freq)
    plt.draw()
    
if __name__ == "__main__":
    # Creates oscilloscope figure window 
    fig = plt.figure(figsize = (12,8))
    signal_ax = plt.axes([.05, .7, 0.25, 0.2])
    # Labels axes and title signal graph
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.title('Sinewave Signal with Additional Signal in Red',fontsize=10)
    # Sets initial axis limits
    signal_ax.set_xlim([0, 3])
    signal_ax.set_ylim([-2, 2])

    # Initial values for no. of points, frequency and time (t_max)
    initial_points = 300
    initial_sin_freq = 1.
    t_max = 3.

    # Creates initial time value array
    t = np.linspace(0, t_max, initial_points)
    """
    Remove the line below and uncomment the next one when you have a signal return from the sinf function above
    """
    signal_amplitude = np.zeros(initial_points)
    # signal_amplitude = sinf(t , initial_sin_freq)
    signal_line_handle, = signal_ax.plot(t , signal_amplitude)

    # Create Exit Button
    exit_ax = plt.axes([0.95, .95, 0.05, 0.05])
    close_button = widgets.Button(exit_ax, 'Exit')
    close_button.on_clicked(exit_button)

    # Create Frequency Slider
    # Placement of frequency slider
    freq_slider_ax = plt.axes([0.08, 0.5, 0.2, 0.03])
    # Widget for frequency slider
    frequency_slider = widgets.Slider(freq_slider_ax, 'Sine 1 Frequency', 0.1, 5, \
                    valinit= initial_sin_freq)
    frequency_slider.label.set_size(7.5)

    # Calls function to change plot when frequency slider is changed
    frequency_slider.on_changed(freq_slider)

    #sets up power spectrum plot
    fourier_ax = plt.axes([0.375, 0.7, 0.25, 0.2])
    plt.xlabel('Frequency (per sec)')
    plt.ylabel('Amplitude')
    plt.title('Sine 1 Power Spectrum')


    """
    Remove the line below and uncomment the following two lines when you have 
    a power return from fourier_func function.
    """
    fourier_line_handle, = plt.plot([0.,0.])
    # power, freq = fourier_func(signal_amplitude,t_max)
    # fourier_line_handle, = plt.plot(freq, power)
    fourier_ax.set_xlim([0, 7])
    fourier_ax.set_ylim([0, 150])



##varying phase addition 
    
    phase_slider_ax = plt.axes([0.08, 0.3, 0.2, 0.03])

    #Adding title to oscilloscope
    
    plt.text(14,22,"George Hill's Oscilloscope",fontsize=18)
    phase_min = 0    
    phase_max = 10  
    phase_init = 0  

    x = np.linspace(0, 2*pi, 300)

    phase_ax = plt.axes([.7, .7, 0.25, 0.2])


    plt.axes(phase_ax) 

    phase_plot, = plt.plot(x, np.sin(phase_init+4*x), color='purple')
    plt.xlim(0, pi)
    plt.ylim(-2,2)
    plt.title("Phase Shifted Sinewave")
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')


    a_slider = Slider(phase_slider_ax,      
                    'Phase',           
                    phase_min,          
                    phase_max,          
                    valinit=phase_init,
                    color='purple' 
                    )

    
    def update(phase):
        phase_plot.set_ydata(np.sin(phase+(4*x))) 
        fig.canvas.draw_idle()          

    
    a_slider.on_changed(update)



#Noise
    
    noise_min = 0   
    noise_max = 3  
    noise_init = 0.01   

    xnoise = np.linspace(0, 2*pi, 300)
    y=np.sin(4*x)
    
    noise_ax = plt.axes([0.7, 0.4, 0.25, 0.2])
    noise_slider_ax = plt.axes([0.08, 0.2, 0.2, 0.03])

    plt.axes(noise_ax) 
    plt.plot(x,y,color='black')

    noise_plot, = plt.plot(x, 2*np.sin(x), 'pink')
    plt.xlim(0, pi)

    plt.title("Sinewave with Noise")
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    noise=np.random.normal(0,0.5,300)

    noise_slider = Slider(noise_slider_ax,      
                    'Noise',            
                    noise_min,          
                    noise_max,         
                    valinit=noise_init,
                    color='pink'
                    )

    def update(noiselevel):
        noise_plot.set_ydata(np.sin(2*x)+(noiselevel*noise)) 
        fig.canvas.draw_idle()          


    noise_slider.on_changed(update)

  

#Sawtooth   
    saw_ax=plt.axes([0.375,0.1,.25,.2])
    plt.title("Sawtooth Wave")
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(0,np.pi)

    def sawf(x, omega):
        return signal.sawtooth(omega*x) 

    def sawsliderCallback(valsaw):
        """ 'val' is the current value selected by the slider
            Recalculate sine values with val as the frequency """
        saw_ax.set_ydata(sawf(x, valsaw)) 
        plt.draw() # Redraw the axes   

    x = np.linspace(0, 4*np.pi, 300)
    saw_ax, = plt.plot(x, sawf((x*4), 1), color='orange')
    
    sawfreqslider_ax = plt.axes([0.08, 0.01, 0.2, 0.03])

    sawfreqslider = widgets.Slider(sawfreqslider_ax, 'Saw Frequency', 0.15, 10.0, valinit=2.0,color='orange')
    sawfreqslider.label.set_size(8)
    sawfreqslider.on_changed(sawsliderCallback)
    

#Squarewave

    square_ax=plt.axes([0.375,0.4,.25,.2])
    plt.title("Squarewave")
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(0,np.pi)

    def squaref(x, omega):
        return signal.square(omega*x) 

    def squaresliderCallback(val):
        """ 'val' is the current value selected by the slider
            Recalculate sine values with val as the frequency """
        square_ax.set_ydata(squaref(x, val)) 
        plt.draw() # Redraw the axes   

    x = np.linspace(0, 4*np.pi, 300)
    square_ax, = plt.plot(x, squaref((x*4), 1), color='green')
    
    squarefreqslider_ax = plt.axes([0.08, 0.1, 0.2, 0.03])

    squarefreqslider = widgets.Slider(squarefreqslider_ax, 'Square Frequency', 0.15, 10.0, valinit=2.0,color='green')
    squarefreqslider.label.set_size(7)
    squarefreqslider.on_changed(squaresliderCallback)

#Second sine wave

    x2 = np.linspace(0, 2*np.pi, 300)
    signal2_ax = plt.axes([.05, .7, 0.25, 0.2])
    def sin2(x2, omega):
        return np.sin((omega*2*np.pi)*x2) 

    def sine2sliderCallback(val2):
        """ 'val' is the current value selected by the slider
            Recalculate sine values with val as the frequency """
        signal2_ax.set_ydata(sin2(x2, val2)) 
        
        plt.draw() # Redraw the axes   


    signal2_ax, =plt.plot(x2, sin2(x2, 1), color='red')
    
    sine2_ax = plt.axes([0.08, 0.4, 0.2, 0.03])

    sine2freqslider = widgets.Slider(sine2_ax, 'Sine 2 Frequency', 0.1, 5.0, valinit=1,color='red')
    sine2freqslider.label.set_size(7)
    sine2freqslider.on_changed(sine2sliderCallback)
    
    # Animation extra

    ani_ax=plt.axes([0.7,0.1,.25,.2])
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title("Windowing a Sinewave")

    def sinewave_ani(xani, tani, wavelength, vel):
        return np.sin((2*np.pi)*(xani-vel*tani)/wavelength)
    
    def coswave_ani(xani,tani,wavelength,vel):
        return np.cos((2*np.pi)*(xani-vel*tani)/wavelength)

    xani = np.arange(0,4,0.01)[np.newaxis,:]
    tani = np.arange(0,2,0.01)[:,np.newaxis]
    wavelength = 1
    vel = 1
    ysin = sinewave_ani(xani, tani, wavelength, vel) 
    ycos = coswave_ani(xani,tani,wavelength,vel)

    
    def init_func():
        ani_ax.clear()

    
    def update_plot(i):
        ani_ax.clear()
        ani_ax.plot(xani[0,:], ysin[i,:], color='red',label="Sine Curve")
        ani_ax.plot(xani[0,:],ycos[i,:],color='blue',label="Cosine Curve")
        ani_ax.legend(loc=1)
        plt.title("Sine and Cosine Animation")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")

    
    anim = FuncAnimation(fig,
                        update_plot,
                        frames=np.arange(0, len(tani[:,0])),
                        init_func=init_func)



   
plt.show()
