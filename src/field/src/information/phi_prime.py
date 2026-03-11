```python
"""
Φ' (Phi-prime) Calculation Module
FTCoE Computational Framework - Version 3.2

Modified Integrated Information metric for Ψ-CE field coupling.
"""

import numpy as np

class PhiPrime:
    """
    Calculate modified integrated information (Φ') for neural systems.
    """
    
    def __init__(self, network_size=10):
        self.n = network_size
        
    def random_network(self, connection_prob=0.3):
        """Generate random neural network connectivity."""
        # Random connectivity matrix
        W = np.random.rand(self.n, self.n) * 0.1
        mask = np.random.rand(self.n, self.n) < connection_prob
        W = W * mask
        np.fill_diagonal(W, 0)  # No self-connections
        
        return W
    
    def integrated_information(self, W, partition=None):
        """
        Calculate standard integrated information (Φ).
        
        Parameters:
        - W: Connectivity matrix
        - partition: Optional bipartition of system
        """
        if partition is None:
            # Simple bipartition: first half vs second half
            k = self.n // 2
            partition = [list(range(k)), list(range(k, self.n))]
            
        # Calculate effective information between parts
        # This is a simplified approximation
        W_part = W.copy()
        
        # Mutual information approximation
        corr = np.corrcoef(W_part)
        mi = -0.5 * np.log(1 - corr**2 + 1e-10)
        mi = np.nan_to_num(mi)
        
        phi = np.sum(mi) / (self.n ** 2)
        
        return phi
    
    def resonance_factor(self, W, field_coupling=1.0):
        """
        Calculate resonance factor R for field coupling.
        """
        # Measure of global synchrony
        eigenvals = np.linalg.eigvals(W)
        synchrony = np.max(np.abs(eigenvals)) / (np.sum(np.abs(eigenvals)) + 1e-10)
        
        R = 1.0 + field_coupling * synchrony
        return R
    
    def phi_prime(self, W, field_coupling=1.0):
        """
        Calculate Φ' = Φ * R
        """
        phi = self.integrated_information(W)
        R = self.resonance_factor(W, field_coupling)
        
        return phi * R
    
    def demonstrate(self):
        """Run demonstration."""
        print("\n📊 Φ' (Phi-prime) Calculator")
        print("="*40)
        
        # Create random network
        W = self.random_network()
        print(f"Network size: {self.n} nodes")
        print(f"Connection density: {np.sum(W>0)/(self.n**2):.3f}")
        
        # Calculate Φ
        phi = self.integrated_information(W)
        print(f"\nΦ (Integrated Information): {phi:.4f}")
        
        # Calculate Φ' for different field couplings
        for coupling in [0, 0.5, 1.0, 2.0]:
            phi_p = self.phi_prime(W, coupling)
            print(f"Φ' (coupling={coupling:.1f}): {phi_p:.4f}")
```
