### Dataset 

There are two breathing datasets. 

- ```breathing.pickle``` contains three activities corrsponding to breathing motion, static environment and random motion (such as human limb movement) at distances of 1 and 2 meters from the surveillance antenna.
- ```breathing_labelled.pickle``` contains labelled breathing data. This dataset is currently limited but will be expanded in the future.

### Setup

The passive sensing system used while collecting the datasets utilizes USRP B200 software defined radio with an omni-directional antenna as an access point. The access point transmits orthogonal frequency division multiplexed symbols at a data rate of 3 Mb/s with a code rate of 12 and quadrature phase shift keying modulation. With this configuration, the transmit power of the WiFi source is estimated to be around -30 dBm. At the receiver end, we have log-periodic directional antennas with 6dBi gain and 60 degree beam-width. The signals received at these antennas are digitized through a Spartan 6 XC6SLX75 FPGA and 61.44 MS/s, 12 bit ADC.
