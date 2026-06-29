# Libraries
import numpy as np
from dataclasses import dataclass, field
from typing import Tuple

# Constants
g_0 = 9.80665         # acceleration due to gravity, m s-2
rho_sl = 1.225        # ISA sea-level air density, kg m-3
t_sl = 288.15         # ISA sea-level temperature, K
l_rate = 0.0065       # ISA lapse rate, K m-1
r_air = 287.05        # specific gas constant (dry air), J kg-1 K-1
gamma = 1.4           # ratio of specific heats

def isa_atmosphere(altitude_m: float) -> Tuple[float, float]:
    altitude_m = np.clip(altitude_m, 0.0, 11_000.0)
    T = t_sl - l_rate * altitude_m
    p = 101_325.0 * (T / t_sl) ** (G0 / (l_rate * r_air))
    rho = p / (r_air * T)
    return rho, p
  
