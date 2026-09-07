import numpy as np
import matplotlib.pyplot as plt

V0 = 5.0
C = 22e-12
R_main = 10e3
R_others = [22e3, 47e3, 100e3]

def charging(t, R):
    tau = R * C
    return V0 * (1 - np.exp(-t / tau))

tau_max = max([R_main] + R_others) * C
t = np.linspace(0, 5 * tau_max, 500)

styles = ["--", "-.", (0, (3, 1, 1, 1, 1, 1))]

fig, ax = plt.subplots()

ax.plot(
    t,
    charging(t, R_main),
    color="black",
    linewidth=2.5,
    label=f"R = {R_main/1e3:.0f} k$\\Omega$ (main)"
)

for R, style in zip(R_others, styles):
    ax.plot(
        t,
        charging(t, R),
        color="black",
        linestyle=style,
        linewidth=1.3,
        label=f"R = {R/1e3:.0f} k$\\Omega$"
    )

V_tau = V0 * (1 - np.exp(-1))
ax.axhline(V_tau, linestyle=":", color="0.4")

ax.grid(False)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title(f"Capacitor charging for varying R (C = {C*1e12:.0f} pF)")
ax.legend()

fig.savefig("figures/generated/rc_charging.pdf")
