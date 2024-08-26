<style>
  table {
    width: 100%;
    table-layout: fixed;
  }
  th, td {
    text-align: left;
    padding: 5px;
    vertical-align: top;
  }
  th {
    width: 25%;
  }
</style>

<table>
  <thead>
    <tr>
      <th>**Sine Wave**</th>
      <th>**Bit Rate and Baud Rate**</th>
      <th>**Shannon-Hartley Theorem**</th>
      <th>**Power and Loss**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <strong>Formula</strong><br>
        $y(t) = A \sin(2\pi ft + \phi)$<br>
        $T = \frac{1}{f}$<br>
        $f = \frac{1}{T}$<br>
        $\Delta \phi = 2\pi f \Delta t$<br>
        $V_{\text{rms}} = \frac{V_m}{\sqrt{2}}$<br>
        <strong>Description</strong><br>
        General Form<br>
        Period<br>
        Frequency<br>
        Phase Shift<br>
        RMS Voltage
      </td>
      <td>
        <strong>Formula</strong><br>
        $R = B \log_2(M)$<br>
        $\text{Baud} = \frac{\text{Bit Rate}}{\log_2(\text{Number of Levels})}$<br>
        <strong>Description</strong><br>
        Bit Rate<br>
        Baud Rate
      </td>
      <td>
        <strong>Formula</strong><br>
        $C = B \log_2(1 + \text{SNR}_{\text{linear}})$<br>
        $\text{SNR}_{\text{linear}} = 10^{\frac{\text{SNR}_{\text{dB}}}{10}}$<br>
        <strong>Description</strong><br>
        Channel Capacity<br>
        SNR (linear)
      </td>
      <td>
        <strong>Formula</strong><br>
        $L = a \times d$<br>
        $P_{\text{received}} = P_{\text{transmitted}} - L_{\text{total}}$<br>
        $P_{\text{W}} = 10^{\frac{P_{\text{dBm}}}{10}} \times 10^{-3}$<br>
        <strong>Description</strong><br>
        Power Loss<br>
        Received Power<br>
        dBm to Watts
      </td>
    </tr>
    <tr>
      <th>**Antenna**</th>
      <th>**Signal Types**</th>
      <th>**Modulation Schemes**</th>
      <th>**Line Coding Schemes**</th>
    </tr>
    <tr>
      <td>
        <strong>Formula</strong><br>
        $A_{\text{eff}} = \frac{\lambda^2 G_{\text{lin}}}{4\pi}$<br>
        $G_{\text{lin}} = 10^{\frac{G_{\text{dBi}}}{10}}$<br>
        <strong>Description</strong><br>
        Effective Area<br>
        Gain (linear)
      </td>
      <td>
        <strong>Type</strong><br>
        Analog Signal<br>
        Digital Signal<br>
        <strong>Description</strong><br>
        Continuous signal that varies over time (e.g., sine wave, voice signal)<br>
        Discrete signal with distinct levels (e.g., binary data)
      </td>
      <td>
        <strong>Scheme</strong><br>
        ASK (Amplitude Shift Keying)<br>
        FSK (Frequency Shift Keying)<br>
        PSK (Phase Shift Keying)<br>
        QAM (Quadrature Amplitude Modulation)<br>
        <strong>Description</strong><br>
        Varies amplitude<br>
        Varies frequency<br>
        Varies phase<br>
        Combines amplitude and phase variations
      </td>
      <td>
        <strong>Scheme</strong><br>
        NRZ-L (Non-Return to Zero-Level)<br>
        Manchester<br>
        AMI (Alternate Mark Inversion)<br>
        <strong>Description</strong><br>
        Binary 1 is high, 0 is low<br>
        Binary 1 is low-to-high transition, 0 is high-to-low transition<br>
        Binary 1 alternates polarity, 0 is zero voltage
      </td>
    </tr>
    <tr>
      <th colspan="2">**Constellation Diagrams**</th>
      <th colspan="2">**Frequency Spectrum**</th>
    </tr>
    <tr>
      <td colspan="2">
        <strong>Scheme</strong><br>
        QPSK<br>
        8-QAM<br>
        <strong>Points</strong><br>
        Four points at $0^\circ$, $90^\circ$, $180^\circ$, $270^\circ$<br>
        Eight points with different amplitudes and phases
      </td>
      <td colspan="2">
        <strong>Signal</strong><br>
        Sine Wave<br>
        Square Wave<br>
        NRZ Data Stream<br>
        <strong>Spectrum</strong><br>
        Single frequency component<br>
        Fundamental frequency and odd harmonics<br>
        DC component and harmonics of the bit rate
      </td>
    </tr>
  </tbody>
</table>
