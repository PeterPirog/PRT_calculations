import pyvisa
import numpy as np


class HP34401():
    def __init__(self, address):
        self.address = address
        self.resource_manager = pyvisa.ResourceManager()
        self.current_res = None  # current measured resistance
        self.range = None  # number of multimeter  range for measured resistance, first range=0

        # data from service manual to calculate resistance uncertainty
        self.R_ranges = np.array([100.0, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9])  # ranges
        self.pct_of_read = np.array([0.01, 0.01, 0.01, 0.01, 0.012, 0.04, 0.8, 8])
        self.pct_of_range = np.array([0.004, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001])

        try:
            self.inst = self.resource_manager.open_resource(self.address)
            self.instrument_detected = True
            print(f'Connected with the instrument {self.idn()} at address: {self.address}')
        except:
            self.instrument_detected = False
            print(f"Can't connect with the instrument at address: {self.address}. Check if address and connection is "
                  f"correct")

        if self.instrument_detected:
            self.reset()

    def reset(self):
        self.inst.write("*RST")
        self.inst.write('CONFigure:FRESistance DEF,MIN')
        print(self.inst.query('CONFigure?'))

    def idn(self):
        return self.inst.query("*IDN?")

    def measure_4R(self):
        self.current_res = float(self.inst.query('MEASure:FRESistance?'))
        return self.current_res

    def error_for_R(self, R):
        if R <= 100:
            self.range = 0
        else:
            self.range = np.argmax(self.R_ranges > R)

        return R * 0.01 * self.pct_of_read[self.range] + 0.01 * self.pct_of_range[self.range] * self.R_ranges[
            self.range]

    def std_unc_for_R(self, R):
        return self.error_for_R(R) / np.sqrt(3)


class PT100():
    def __init__(self, address, coef_R0=100, coef_A=3.9083e-3, coef_B=-5.775e-7, coef_C=-4.183e-12):
        self.address = address
        self.multimeter = HP34401(address=self.address)

        self.coef_R0 = coef_R0
        self.coef_A = coef_A
        self.coef_B = coef_B
        self.coef_C = coef_C

        self.current_Rt = None
        self.current_Rt_std_unc = None  # standard uncertainty of resistance
        self.current_Rt_ext_unc = None  # extended uncertainty of resistance

        self.current_t = None  # calculated temperature
        self.current_t_std_unc = None  # standard uncertainty of temperature
        self.current_t_ext_unc = None  # extended uncertainty of temperature

        self.k = 2  # expanded uncertainty factor

    def meas_temp(self, verbose=True):
        self.current_Rt = self.multimeter.measure_4R()
        self.current_Rt_std_unc = self.multimeter.std_unc_for_R(self.current_Rt)  #########0.13
        self.current_Rt_ext_unc = self.k * self.current_Rt_std_unc

        self.current_t, self.current_t_std_unc = self.convert_R_to_t(self.current_Rt, self.current_Rt_std_unc)
        self.current_t_ext_unc = self.k * self.current_t_std_unc

        if verbose:
            print(f'Resistance {self.current_Rt}+/-{self.current_Rt_std_unc} ohm,'
                  f' temperature:{self.current_t} C, std unc:{self.current_t_std_unc} C')

        return self.current_t, self.current_t_std_unc

    def __R2t__(self, R):
        """
        Function to convert Pt100 resistance to temperature
        :param R: resistance
        :return: temperature
        """
        coef_minus = [self.coef_R0 * self.coef_C,
                      -100 * self.coef_R0 * self.coef_C,
                      self.coef_R0 * self.coef_B,
                      self.coef_R0 * self.coef_A,
                      self.coef_R0 - R]

        coef_plus = [self.coef_R0 * self.coef_B,
                     self.coef_R0 * self.coef_A,
                     self.coef_R0 - R]

        if np.real(np.roots(coef_plus))[1] >= 0:
            t = np.real(np.roots(coef_plus)[1])
        else:
            t = np.real(np.roots(coef_minus)[3])
        return t

    def convert_R_to_t(self, R_value, R_std_unc=0.0, N=1000):
        # Rx_list - list of resistances generated for assumed standard uncertainty
        # tx_list - list of temperatures generated for assumed standard uncertainty

        if R_std_unc == 0.0:
            return self.__R2t__(R_value), 0.0
        else:
            mu, sigma = R_value, R_std_unc  # mean and standard deviation
            Rx_list = np.random.normal(mu, sigma, N)
            t_list = [self.__R2t__(Rx_list[i]) for i in range(N)]
            return np.mean(t_list), np.std(t_list)


if __name__ == "__main__":
    pt = PT100(address='GPIB0::21::INSTR')

    print(pt.meas_temp())
    # print(pt.convert_R_to_t(120,0.1))
    # mul=HP34401(address='GPIB0::21::INSTR')
    # print(mul.std_unc_for_R(313.7))
