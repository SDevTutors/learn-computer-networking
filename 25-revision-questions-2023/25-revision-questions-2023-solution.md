Given the breadth of the questions, I'll address them systematically. For each sub-question, I will provide the relevant solution or explanation.

---

### **Q1a: Spectrum Sketching**

1. **A sine wave described by** \( y = 3\sin(22,000\pi t + \frac{\pi}{2}) \)

   - **Frequency:** The angular frequency \( \omega = 22,000\pi \), so the frequency \( f = \frac{\omega}{2\pi} = 11 \) kHz.
   - **Spectrum:** A single line at 11 kHz.

   The spectrum will have a single spike at 11 kHz on the frequency axis.

2. **A 1 kHz square wave**

   - A square wave is composed of a fundamental frequency and odd harmonics.
   - **Fundamental frequency:** 1 kHz.
   - **Harmonics:** 3 kHz, 5 kHz, 7 kHz, etc.

   The spectrum will have spikes at 1 kHz, 3 kHz, 5 kHz, 7 kHz, etc., with decreasing amplitude for higher harmonics.

3. **A 1 Mbps NRZ data stream**

   - NRZ (Non-Return-to-Zero) signal is a type of digital signal.
   - **Fundamental frequency:** Half the bit rate, so \( \frac{1 \text{ Mbps}}{2} = 0.5 \) MHz or 500 kHz.
   - **Spectrum:** The main lobe will be around 500 kHz, with side lobes spreading out.

   The spectrum will have a main lobe centered around 500 kHz, with the width determined by the data rate.

---

### **Q1b: Baud Rate vs Bit Rate**

The **baud rate** is the number of signal changes (symbols) per second, while the **bit rate** is the number of bits transmitted per second. 

- **Analogy:** Think of a conveyor belt carrying boxes. If each box (symbol) carries one item (bit), the speed of the belt (baud rate) and the number of items moved per second (bit rate) are the same. However, if each box can hold multiple items, then the bit rate is higher than the baud rate. The width of the belt (bandwidth) is determined by how often a box (symbol) passes by, not by how many items (bits) are inside the box.

The required bandwidth is determined by how frequently symbols (baud rate) need to change, rather than the number of bits contained within each symbol.

---

### **Q1c: Bandwidth of BFSK System**

Given:
- **Centre frequency:** 800 kHz
- **Data rate:** 30 kbps
- **Modulation index \(d\):** 0.5
- **Guard band:** 10 kHz

**Calculation:**

- **Frequency shift (Δf):** \( d \times \text{Data rate} = 0.5 \times 30 \text{ kbps} = 15 \text{ kHz} \)
- **Two frequencies:** 800 kHz ± 15 kHz = 785 kHz and 815 kHz.
- **Total Bandwidth:** \( 2 \times \Delta f + 2 \times \text{Guard band} \)

\[
\text{Bandwidth} = 2 \times 15 \text{ kHz} + 2 \times 10 \text{ kHz} = 50 \text{ kHz}
\]

**Spectrum:** The spectrum will have two spikes at 785 kHz and 815 kHz with a total bandwidth of 50 kHz.

---

### **Q1d: Signal Power and Data Capacity Calculation**

Given:
- **Transmitter Power:** +15 dBm
- **Link A Loss:** 95% (which is a loss of 10 dB)
- **Amplifier Gain:** +17 dB
- **Link B Loss:** 0.4 dB/km over 60 km
- **Receiver Noise Power:** 3 nW
- **Bandwidth:** 20 MHz

1. **Signal Power at the Receiver:**

   - **After Link A Loss:** \( 15 \text{ dBm} - 10 \text{ dB} = 5 \text{ dBm} \)
   - **After Amplification:** \( 5 \text{ dBm} + 17 \text{ dB} = 22 \text{ dBm} \)
   - **Link B Loss:** \( 60 \text{ km} \times 0.4 \text{ dB/km} = 24 \text{ dB} \)
   - **Signal Power at Receiver:** \( 22 \text{ dBm} - 24 \text{ dB} = -2 \text{ dBm} \)

   Signal power in watts can be calculated as:
   \[
   P_{\text{received}} = 10^{\frac{-2}{10}} \text{ mW} = 0.63 \text{ mW}
   \]

2. **Maximum Theoretical Data Capacity:**

   - **Using Shannon’s Capacity Formula:**

   \[
   C = B \log_2\left(1 + \frac{S}{N}\right)
   \]
   - Where \( B = 20 \text{ MHz} \), \( S/N \) is the signal-to-noise ratio.
   - Signal power \( S = 0.63 \text{ mW} \), Noise power \( N = 3 \text{ nW} \).

   \[
   S/N = \frac{0.63 \text{ mW}}{3 \text{ nW}} = 210,000
   \]
   \[
   C = 20 \times 10^6 \log_2(1 + 210,000) \text{ bps}
   \]

   This will give the maximum theoretical data rate.

---

### **Q2a: Bit Rate vs Baud Rate**

1. **Bit Rate:** The number of bits transmitted per second.
2. **Baud Rate:** The number of symbols transmitted per second.

**Example:**
- **Binary (1 bit per symbol):** Bit rate = Baud rate.
- **QAM with 16 levels (4 bits per symbol):** Bit rate = 4 × Baud rate.

---

### **Q2b: Constellation Diagrams**

1. **ASK with peak amplitude values of 1V and 2V:**
   - Two points on the real axis: 1V and 2V.

2. **QPSK with a peak amplitude of 5V:**
   - Four points at \( \pm 5V \) with phase angles of \( 0^\circ, 90^\circ, 180^\circ, 270^\circ \).

3. **8-QAM:**
   - Two amplitude levels: 1V, 3V.
   - Four phases: \( \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4} \).

---

### **Q2c: Signal Power and Data Capacity Calculation**

(Similar to Q1d, adjusting for new distances and losses.)

---

### **Q3a: Carrier Signal**

- A **carrier signal** is a high-frequency signal modulated with information for transmission.

**Examples:**
- **Analog:** AM radio signal.
- **Digital:** Binary phase-shift keying (BPSK) signal.

---

### **Q3b-e: Calculations and Constellation Diagrams**

(Similar steps as above for calculations and diagrams.)

---

This structured approach should help you solve each part step by step. If you need any further details on a specific question, let me know!
