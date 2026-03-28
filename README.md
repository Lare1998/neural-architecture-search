# Neural Architecture Search (NAS)

Research implementation of efficient Neural Architecture Search (NAS) techniques, specifically tailored for deployment on mobile and edge devices. This project explores various search strategies and performance estimation methods to discover optimal neural network architectures under resource constraints.

## Features
- **Efficient Search Algorithms:** Implementations of popular NAS algorithms (e.g., DARTS, ENAS, ProxylessNAS).
- **Mobile-Friendly Architectures:** Focus on generating models with low latency and memory footprint.
- **Performance Prediction:** Utilize meta-learning and surrogate models to quickly estimate architecture performance.
- **Hardware-Aware Design:** Incorporate hardware constraints (e.g., FLOPs, latency) directly into the search objective.
- **JAX Integration:** Leverage JAX for high-performance numerical computation and automatic differentiation.

## Getting Started

### Installation

```bash
pip install jax jaxlib tensorflow_datasets
```

### Running a Search Experiment

```python
import jax
import jax.numpy as jnp
from nas_framework import NASController, MobileNetV3SearchSpace

# Define search space and controller
search_space = MobileNetV3SearchSpace()
nas_controller = NASController(search_space, num_epochs=50, population_size=10)

# Run the search
best_architecture = nas_controller.search()
print(f"Best architecture found: {best_architecture}")

# Evaluate the best architecture
# ... (code for training and evaluation)
```

## Contributing

We welcome research contributions and collaborations! Please see `CONTRIBUTING.md` for details.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
