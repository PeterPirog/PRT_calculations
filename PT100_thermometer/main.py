import pyvisa
import numpy as np


class HP34401():
    def __init__(self, address):
        self.address = address
        self.resource_manager = pyvisa.ResourceManager()
        self.current_res = None

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


class PT100():
    def __init__(self, address, coef_R0=100, coef_A=3.9083e-3, coef_B=-5.775e-7, coef_C=-4.183e-12):
        self.address = address
        self.multimeter = HP34401(address=self.address)

        self.coef_R0 = coef_R0
        self.coef_A = coef_A
        self.coef_B = -coef_B
        self.coef_C = coef_C

        self.current_Rt = None
        self.current_t = None

    def meas_temp(self):
        self.current_Rt = self.multimeter.measure_4R()

        coef = [self.coef_R0 * self.coef_C,
                -100 * self.coef_R0 * self.coef_C,
                self.coef_R0 * self.coef_B,
                self.coef_R0 * self.coef_A,
                self.coef_R0 - self.current_Rt]

        coef2 = [self.coef_R0 * self.coef_B,
                 self.coef_R0 * self.coef_A,
                 self.coef_R0 - self.current_Rt]

        if np.real(np.roots(coef2))[1] >= 0:
            self.current_t = np.real(np.roots(coef2)[1])
            print(f'Resistance {self.current_Rt}, {np.roots(coef2)} \n')
        else:
            self.current_t = np.real(np.roots(coef)[3])
            print(f'Resistance {self.current_Rt}, {np.roots(coef)}\n')

        print(f'Resistance {self.current_Rt} ohm, temperature:{self.current_t} C')

        return self.current_t


if __name__ == "__main__":
    pt = PT100(address='GPIB0::21::INSTR')

    print(pt.meas_temp())
