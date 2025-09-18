import numpy as np

def calculate_barrier(k, T=300):
    """
    Calculate activation barrier (ΔG‡) in kcal/mol from rate constant (k) at temperature T (K).
    
    Parameters:
    k : float or array-like
        Rate constant(s) in 1/s
    T : float, optional
        Temperature in Kelvin (default is 300 K)
    
    Returns:
    float or np.ndarray
        Activation barrier(s) in kcal/mol
    """
    R = 1.987e-3  # kcal/(mol*K)
    k_B = 1.381e-23  # J/K
    h = 6.626e-34  # J*s
    prefactor = (k_B * T) / h  # in s^-1
    
    return -R * T * np.log(k / prefactor)

# Example usage
rate_constants = [5.7, 6.5, 12.82, 0.64]  # Example rate constants in 1/s
names = ['WT', 'WT', 'N308D', 'Q506P']
for i, rate in enumerate(rate_constants):
	barrier = calculate_barrier(rate, T=300)
	print(names[i], barrier)


