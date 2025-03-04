import math


class BankingWithFriction:
    def __init__(self, r, theta, mu):
        self.r = r
        self.theta = theta
        self.mu = mu

    def calculate_speeds(self):
        theta_rad = math.radians(self.theta)
        g = 9.8
        v_max = math.sqrt(
            (self.r * g * (math.tan(theta_rad) + self.mu))
            / (1 - self.mu * math.tan(theta_rad))
        )
        v_min = math.sqrt(
            (self.r * g * (math.tan(theta_rad) - self.mu))
            / (1 + self.mu * math.tan(theta_rad))
        )
        return v_max, v_min


r = float(input("Enter the radius of the road (in meters): "))
theta = float(input("Enter the banking angle (in degrees): "))
mew = float(input("Enter the coefficient of friction: "))
banking = BankingWithFriction(r, theta, mew)
v_max, v_min = banking.calculate_speeds()
print(f"The maximum speed is {v_max:.2f} m/s")
print(f"The minimum speed is {v_min:.2f} m/s")
