from gnuradio import analog, channels, gr, blocks, uhd
import time
from matplotlib import pyplot as plt

class Radio(object):
    def __init__(self):
        self.total_time = 10            # Time in seconds to run flowgraph
        self.samp_rate  = 64000         # Sampling rate of source/sinks
        self.freq       = 3e9           # Carrier frequency
        self.gain       = 64
        self.antenna    = 'RX2'         
        self.bandwidth  = 10e6
        
        self.src        = analog.sig_source_c(self.samp_rate, 
                                              analog.GR_SIN_WAVE, 1000, 1, 0)
        self.snk        = blocks.vector_sink_c()
        self.snk_ref    = blocks.vector_sink_c()
        
        # Initialise USRP sources and sinks. We are using one transmitter and two receivers
        # ; one for reference and other for surveillance.
        self.usrp_ref   = uhd.usrp_source(",".join(("", "serial=F4F57F")),
                                          uhd.stream_args(cpu_format="fc32", channels=range(1),),)
        self.usrp_rx    = uhd.usrp_source(",".join(("", "serial=F4F59F")),
                                          uhd.stream_args(cpu_format="fc32", channels=range(1),),)
        self.usrp_tx    = uhd.usrp_sink(",".join(("", "serial=F4F597")),
                                          uhd.stream_args(cpu_format="fc32", channels=range(1),),)
        
        self._set_properties(self.usrp_ref)
        self._set_properties(self.usrp_rx)
        self._set_properties(self.usrp_tx)

        self.usrp_ref.set_antenna(self.antenna, 0)
        self.usrp_rx.set_antenna(self.antenna, 0)

    def _set_properties(self, usrp):
        usrp.set_samp_rate(self.samp_rate)
        usrp.set_center_freq(self.freq, 0)
        usrp.set_gain(self.gain, 0)

    def track(self):
        # Start tracking time
        self.t_start = time.time()
        self.t_end = self.t_start + self.total_time

        # Connect blocks
        self.tb = gr.top_block()
        self.tb.connect(self.src, self.usrp_tx)
        self.tb.connect(self.usrp_rx, self.snk)
        self.tb.connect(self.usrp_ref, self.snk_ref)

        # Run simulation for a specified time
        self.tb.start()
        while time.time() < self.t_end:
            pass
        self.tb.stop()
        
        # Plot collected data
        plt.plot(self.snk.data(), 'r')
        plt.plot(self.snk_ref.data(), 'g')
        plt.show()

if __name__ == "__main__":
    radio = Radio()
    radio.track()
