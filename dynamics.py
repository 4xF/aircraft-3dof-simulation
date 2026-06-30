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
  

@dataclass
class AircraftState:
    """
    Using NED (North-East-Down) flat-Earth frame.
    Velocity is expressed in the body frame (u forward, v right, w down)
    and also cached in NED for convenience.
 
    Attitude is stored as a unit quaternion q = [q0, q1, q2, q3]
    (scalar-first convention) and derived Euler angles (roll φ, pitch θ,
    yaw ψ) in radians.
    """
 
    # Position (NED, metres)
    north: float = 0.0
    east: float = 0.0
    down: float = 0.0          # positive downward; altitude = -down
 
    # Body-frame velocity (m s-1)
    u: float = 0.0             # forward
    v: float = 0.0             # right (side-slip component)
    w: float = 0.0             # down
 
    # Euler angles (rad)
    phi: float = 0.0           # roll
    theta: float = 0.0         # pitch
    psi: float = 0.0           # yaw / heading
 
    # Quaternion (scalar-first)
    q0: float = 1.0
    q1: float = 0.0
    q2: float = 0.0
    q3: float = 0.0
 
    # Angular rates (rad s-1, body frame)
    p: float = 0.0             # roll rate
    q_ang: float = 0.0         # pitch rate  (q_ang to avoid clash with quaternion q)
    r: float = 0.0             # yaw rate
