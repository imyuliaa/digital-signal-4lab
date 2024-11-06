import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, IntegrationWarning
import warnings
warnings.filterwarnings("ignore", category=IntegrationWarning)


def f(t):
    return abs(t)*((2 * 22 + 1) / 7)


# Функція для обчислення дійсної та уявної частин інтегралу Фур’є
def compute_fourier_component(w_k, N=2200):
    Re_F, _ = quad(lambda t: f(t) * np.cos(-w_k * t), -N, N)
    Im_F, _ = quad(lambda t: f(t) * np.sin(-w_k * t), -N, N)
    return Re_F, Im_F

# Функція для обчислення спектру амплітуд
def amplitude_spectrum(Re_F, Im_F):
    return np.sqrt(Re_F ** 2 + Im_F ** 2)


# Функція для побудови графіку дійсної частини Re F(w_k) для всіх T на одному графіку
def plot_real_part_all_periods(T_values, k_max=20, N=2200):
    plt.figure(figsize=(12, 8))

    for T in T_values:
        w_k_values = [(2 * np.pi * k) / T for k in range(k_max)]
        Re_F_values = []

        for w_k in w_k_values:
            Re_F, _ = compute_fourier_component(w_k, N)
            Re_F_values.append(Re_F)

        # Додаємо лінію для кожного T на одному графіку
        plt.plot(w_k_values, Re_F_values, label=f'T = {T}')

    # Налаштування графіку
    plt.xlabel('w_k')
    plt.ylabel('Re F(w_k)')
    plt.title('Дійсна частина F(w_k) для різних періодів T')
    plt.legend(title="Періоди T")
    plt.grid(True)
    plt.show()


# Функція для побудови графіку спектра амплітуд |F(w_k)| для всіх T на одному графіку
def plot_amplitude_spectrum_all_periods(T_values, k_max=20, N=2200):
    plt.figure(figsize=(12, 8))

    for T in T_values:
        w_k_values = [(2 * np.pi * k) / T for k in range(k_max)]
        amplitude_values = []

        for w_k in w_k_values:
            Re_F, Im_F = compute_fourier_component(w_k, N)
            amplitude = amplitude_spectrum(Re_F, Im_F)
            amplitude_values.append(amplitude)

        # Додаємо лінію для кожного T на одному графіку
        plt.plot(w_k_values, amplitude_values, label=f'T = {T}')

    # Налаштування графіку
    plt.xlabel('w_k')
    plt.ylabel('|F(w_k)|')
    plt.title('Спектр амплітуд |F(w_k)| для різних періодів T')
    plt.legend(title="Періоди T")
    plt.grid(True)
    plt.show()


# Виклик функцій для побудови графіків з потрібними значеннями T
T_values = [4, 8, 16, 32, 64, 128]
plot_real_part_all_periods(T_values)
plot_amplitude_spectrum_all_periods(T_values)
