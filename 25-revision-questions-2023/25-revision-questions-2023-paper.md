**Question 1 topics**

**Bit rate, baud rate, channel capacity, SNR, bandwidth, Modulation, Signals, waveforms, Analogue modulation, digital modulation, ASK, FSK, PSK, QAM, bandwidth, spectra, constellation diagrams.**

# Summer 2023

## Question 1

### Q1a

Sketch the spectrum of the following signals

1. A sine wave described by $y = 3\sin(22,000\pi + \frac{\pi}{2})$

2. A 1kHz square wave

3. A 1Mbps NRZ data stream

In each case ensure that the frequency axis of the spectrum is clearly labelled.

**(6 marks)**

**b)**	Why does the baud rate and not the bit rate determine the required bandwidth for a digital signal? Use an analogy to support your answer.

**(4 marks)**

**c)**	A wireless data transmission system uses BFSK and a centre frequency at 800 kHz.  What bandwidth will be used to carry a data stream at 30kbps? Assume d = 0.5 and a guard band of 10 kHz is used between frequencies.   Draw the spectrum of the system output. 

**(5 marks)**

**d)**	Consider the following data transmission system

![1724666405539](images/25-revision-questions-2023/1724666405539.png)

The transmitter transmits +15dBm of signal power into link A.  Link A suffers a 95% power loss.  At the end of link A an amplifier with a gain of +17dB is used to boost the signal power before sending it on to link B.  Link B is 60km long with a loss of 0.4dB per km.  A receiver, which suffers from 3nW of noise at its input, is used to recover the signal at the end of link B.  Than bandwidth of the system is 20MHz.  

`	`i)	What is the expected signal power at the receiver?

ii)	What is the maximum theoretical data transmission capacity of the system?

**2012 Summer**

**Q. 1**

**a)**	Distinguish between the bit rate and the baud rate of a telecommunications system								**(6 marks)**

**b)**		Draw the constellation diagram for the following modulation schemes

`	`i)	ASK with peak amplitude values of 1V and 2V

`	`ii)	QPSK with a peak amplitude value of 5V and any suitable phases

iii)	8-QAM with 2 different amplitude values 1V and 3V and four different phases, π/4, 3π/4, 5π/4, 7π/4,

`	`Ensure that the axes of all diagrams are labelled to show signal amplitudes

`									`**(9 marks)**

**c)**	Consider the following data transmission system

![1724666405539](images/25-revision-questions-2023/1724666405539.png)



The transmitter transmits +15dBm of signal power into link A.  Link A is 45km long with a power loss of 0.6dB per km.  At the end of link A an amplifier with a gain of +17dB is used to boost the signal power before sending it on to link B.  Link B is 60km long with a loss of 0.4dB per km.  A receiver, which suffers from 3nW of noise at its input, is used to recover the signal at the end of link B.  Than bandwidth of the system is 20MHz.  

`	`i)	What is the expected signal power at the receiver?

ii)	What is the maximum theoretical data transmission capacity of the system?

**(10 marks)**

**(Total 25 Marks)**
**


Question 2

a)	Explain the difference between an analog and a digital signal.  Give two examples of each.

b)	Explain the difference between a periodic and a nonperiodic signal.  Give two examples of each.

c)	A sine wave is described by $y(t) = 4.5\sin(100t + \frac{\pi}{2})$.  Sketch the sine wave, clearly labelling each axis with appropriate units.

d)	A sine wave has a period of 0.65µs.  What is its frequency?

e)	A 260MHz sine wave is delayed by 120ps.  By how much is the phase shifted due to the delay?  Give your answer in both radians and degrees.

Question 3

a)		What is a carrier signal in the context of a wireless communications system?

b)	A radio wave has a wavelength of 25cm.  What is its frequency?

c)	A wireless channel has a bandwidth of 0.7MHz and a Signal to noise ratio of 35dB.  What type of QAM would you recommend using if you wanted to get the maximum possible data rate through the channel?

d)	Draw a constellation diagram for the following

`	`32 QAM

`	`QPSK

`	`ASK

e)	A 16QAM signal is running at 1.5MBaud.  Estimate the bandwidth assuming d = 1.

Question 4

a)		Draw the constellation diagram for the following modulation schemes

`	`i)	ASK with peak amplitude values of 1V and 3V

`	`ii)	QPSK with a peak amplitude value of 5V and any suitable phases

iii)	8-QAM with 2 different amplitude values 1V and 3V and four different phases, π/4, 3π/4, 5π/4, 7π/4,

`	`Ensure that the axes of all diagrams are labelled to show signal amplitudes

b)	Sketch the modulator output waveform for two of the 8-QAM constellation points in Question 2 part (a) above.  You must choose two points with different phases and sketch the two waveforms on the one set of axes.  Clearly label the axes and clearly identify the constellation point that each waveform represents.  Use a carrier frequency of 750MHz. 

c)	A telephone line has a 4kHz Bandwidth.  What is the maximum number of bits we can send using the following techniques.  Assume that the line has a sufficiently low noise level to carry the data without error.

`	`i)	ASK where d = 1

`	`ii)	QPSK where d = 0.5

`	`iii)	64-QAM where d = 1

Question 5

a)	Explain the difference between a baseband and a passband signal.  Give two examples of each.

b)	A periodic signal with period 23ps is travelling at a speed of 3 x 10<sup>8</sup> m/sec.  What is the wavelength of the signal?

c)	A system generates a square wave with a period of 3ms.  Sketch the frequency spectrum of the system output.

d)	An audio signal contains a band of frequencies from 20Hz to 20 kHz.  Sketch the signal in the frequency domain.

e)	A system generates a square wave with a period of 0.75ns.  All harmonics above the third harmonic are filtered out.  What is the bandwidth of the system output?


Question 6

a)	Define the bit rate and the baud rate for a system

b)	A system transmits at a bit rate of 1Gbps using 16 signalling levels per symbol.  What is the baud rate?

c)	A low pass channel has a bandwidth of 200kHz.  What is the maximum bit rate of this channel?

d)	What are the main sources of transmission impairment.

e)	A data transmission system launches 45mW of power into a cable.  The cable is 22km in length and has a loss of 2.5dB/km.  What is the power level at the end of the cable?  

Practice Questions

Question 7

a)	Consider the following data transmission system

TX

15mW

+20dB

Splitter

30%        70%






![](Aspose.Words.ac4770eb-c9b2-4646-b285-f1239799c7aa.010.png)

a)	Determine the power at the 30% output arm of the splitter.

b)	What causes a signal to become distorted in a data communications system?  Use a diagram to illustrate your answer.

c)	If a receiver was connected to the 30% output arm of the splitter and the receiver noise level was 2nW what would be the maximum theoretical data transmission capacity of the system?

d)	A data communications system uses 16 QAM to send data through a noiseless channel with a bandwidth of 200kHz.  What is the maximum practical capacity of the channel if the system is using 16QAM?

e)	How many signalling levels would be required to send a 2Mbps data stream through a channel with a bandwidth of 400kHz?


Question 8

1) A telephone line has a bandwidth of 3500Hz and a Signal to Noise Ratio of 28dB.  What is the capacity of the channel?

   b)	What signal to noise ratio would be required to send a 1MB/sec data stream through a channel with a bandwidth of 100kHz?	  

   c)	A channel has a bandwidth of 2.5MHz and a Signal to noise ratio of 200,000.  How many signalling levels should be used to achieve the maximum data rate through this channel?  What is this maximum data rate?

   d)	What is the difference between the bandwidth and the throughput of a data communications system?

   e)	A 3kByte message is sent at 2Gbps through a 5,000km cable.  The propagation speed is 2.4 x 10<sup>8</sup> m/sec.  How long will it take for the entire message to arrive at the receiver?



Question 9

a)	How many bits can fit on a 1.5km link if the propagation speed is 2.4 x 10<sup>8</sup> m/sec and the bit rate is 25MB/sec?

b)	What is line coding?

c)	Why are the data rate and the signal rate sometimes different in a baseband communications system?

d)	Digital receivers can suffer from baseline wandering.  What is baseline wandering and how can it be avoided?

e)	Explain why synchronisation between the sender and receiver is important in a baseband communications system.  What can happen if synchronisation is lost?

Question 10

a)	Compare NRZ, NRZ-L and NRZ-I line coding schemes in terms of base line wandering and synchronisation.

b)	Why do some line coding schemes result in DC components whereas others do not?

c)	What would be the effect of a loss of synchronisation between a transmitter and receiver in a digital transmission system?

d)	A data transmission scheme is to transmit the following data stream.

`		`011100101000

`	`Assume the last signal level has been positive.  Draw the graph of the output signal for the following coding schemes

`		`NRZ-L

`		`NRZ-I

`		`Manchester

`		`Differential Manchester

`		`AMI

`		`Pseudoternary

Question 11

a)	Why does a Manchester coded data stream occupy more bandwidth than an NRZ-L data stream of the same data rate?

b)	What advantages do multilevel coding schemes offer over simple polar or bipolar schemes?

c)	How many levels does the 2B1Q coding scheme have?

d)	Given the following transition table, draw the graph of the output signal for the data stream 1100100001.  Assume the last signal level has been negative.


[ref1]: Aspose.Words.ac4770eb-c9b2-4646-b285-f1239799c7aa.006.png

Let’s continue solving the questions step by step.

### **Q3b: Wavelength and Frequency Relationship**

A radio wave has a wavelength of 25 cm. What is its frequency?

- **Formula:** The relationship between wavelength ($\lambda$) and frequency ($f$) is given by:
  $$f = \frac{c}{\lambda}$$
  where $c$ is the speed of light ($3 \times 10^8$ m/s).

- **Calculation:**
  $$f = \frac{3 \times 10^8 \text{ m/s}}{0.25 \text{ m}} = 1.2 \times 10^9 \text{ Hz} = 1.2 \text{ GHz} $$

**Answer:** The frequency of the radio wave is 1.2 GHz.

---

### **Q3c: Maximum Possible Data Rate for a Wireless Channel**

Given:
- **Bandwidth:** 0.7 MHz
- **Signal-to-Noise Ratio (SNR):** 35 dB

1. **Convert SNR from dB to linear scale:**
   $$\text{SNR (linear)} = 10^{\frac{\text{SNR (dB)}}{10}} = 10^{\frac{35}{10}} = 3162.28$$

2. **Shannon Capacity Formula:**
   $$C = B \log_2(1 + \text{SNR})$$
   where $B$ is the bandwidth.

   $$C = 0.7 \times 10^6 \log_2(1 + 3162.28) \text{ bps}$$
   $$C \approx 0.7 \times 10^6 \times 11.62 \text{ bps} \approx 8.134 \text{ Mbps} $$

**Recommended QAM:**
To achieve this data rate efficiently, using a 64-QAM (which carries 6 bits per symbol) is recommended. This modulation scheme is suitable as it balances complexity, data rate, and bandwidth usage.

---

### **Q3d: Constellation Diagrams**

- **32 QAM:**
  - 32 QAM has 32 points, arranged in a grid pattern, with different amplitude and phase combinations. Typically, it’s a combination of four amplitude levels and eight phase levels.

- **QPSK:**
  - QPSK (Quadrature Phase Shift Keying) has four points, each 90° apart on the constellation diagram. These points are typically located on the unit circle in the complex plane.

- **ASK:**
  - ASK (Amplitude Shift Keying) has points on the real axis, with each point representing a different amplitude. For binary ASK, there are typically two points, one at 0V and one at the maximum amplitude.

---

### **Q3e: Estimating Bandwidth for 16-QAM Signal**

Given:
- **Baud rate:** 1.5 MBaud
- **Modulation:** 16-QAM
- **Modulation Index $d$:** 1

1. **Bandwidth Estimation:**
   - The bandwidth ($BW$) for a signal can be estimated using:
   $$BW \approx \text{Baud rate} \times (1 + d)$$
   $$BW \approx 1.5 \times 10^6 \times 2 = 3 \text{ MHz}$$

**Answer:** The estimated bandwidth is 3 MHz.

---

### **Q4a: Constellation Diagrams**

- **i) ASK with peak amplitude values of 1V and 3V:**
  - Two points on the real axis at $1V$ and $3V$.

- **ii) QPSK with a peak amplitude value of 5V:**
  - Four points at $5V$ magnitude with phases of $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$.

- **iii) 8-QAM with two amplitude values 1V and 3V and four different phases $\pi/4$, $3\pi/4$, $5\pi/4$, $7\pi/4$:**
  - Eight points, combining the two amplitudes with the four phases.

---

### **Q4b: Modulator Output Waveform**

For the given 8-QAM points with different phases:
- **Example Points:** $1V$ at $\pi/4$ and $3V$ at $5\pi/4$.
  
The waveform would show two sinusoidal signals modulated at 750 MHz, with one having a lower amplitude and phase shift corresponding to $\pi/4$ and the other with a higher amplitude and phase shift corresponding to $5\pi/4$.

---

### **Q4c: Maximum Number of Bits for a Telephone Line**

Given:
- **Bandwidth:** 4 kHz

1. **ASK (d = 1):**
   - **Maximum bits per second:** $2 \times \text{Bandwidth}$
   $$\text{Max Bits} = 2 \times 4000 \text{ bps} = 8 \text{ kbps}$$

2. **QPSK (d = 0.5):**
   - **Maximum bits per second:** $2 \times \text{Bandwidth} \times \log_2 4$
   $$\text{Max Bits} = 4 \times 4000 \text{ bps} = 16 \text{ kbps}$$

3. **64-QAM (d = 1):**
   - **Maximum bits per second:** $2 \times \text{Bandwidth} \times \log_2 64$
   $$\text{Max Bits} = 12 \times 4000 \text{ bps} = 48 \text{ kbps}$$

---

### **Q5a: Baseband vs Passband Signal**

- **Baseband Signal:** A signal that occupies the frequency range from near 0 Hz up to a cutoff frequency. Example: Digital data signals, Ethernet signals.

- **Passband Signal:** A signal that has been modulated to shift its frequency spectrum to higher frequencies. Example: AM and FM radio signals.

---

### **Q5b: Wavelength of a Signal**

Given:
- **Period:** 23 ps
- **Speed of Light:** $3 \times 10^8$ m/s

1. **Wavelength Calculation:**
   $$\lambda = \text{Period} \times \text{Speed} = 23 \times 10^{-12} \times 3 \times 10^8 = 6.9 \times 10^{-3} \text{ meters} = 6.9 \text{ mm}$$

---

### **Q5c-e: Spectrum Sketches and Bandwidth Calculations**

1. **Square Wave Spectrum:**
   - Fundamental frequency and odd harmonics.
   - Spikes at odd harmonics with decreasing amplitude.

2. **Audio Signal Frequency Domain Sketch:**
   - Continuous band from 20 Hz to 20 kHz.

3. **Square Wave with Period 0.75 ns:**
   - Bandwidth includes the first three harmonics.

---

### **Q6a: Bit Rate and Baud Rate Definition**

- **Bit Rate:** Number of bits transmitted per second.
- **Baud Rate:** Number of symbols transmitted per second.

---

### **Q6b-e: Calculations for Data Rates and Transmission Losses**

1. **Baud Rate Calculation:**
   $$\text{Baud rate} = \frac{\text{Bit rate}}{\log_2 \text{Signal levels}} = \frac{1 \times 10^9}{4} = 250 \text{ MBaud}$$

2. **Maximum Bit Rate:**
   $$C = 2 \times B \times \log_2(1 + S/N)$$

3. **Transmission Impairments:**
   - **Attenuation, Noise, Distortion.**

4. **Power Level after Loss:**
   - Calculate using the formula for power loss across a distance with given attenuation.

---

The questions cover a wide range of topics in communication systems. If further details or clarifications are needed, feel free to ask!
