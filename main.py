
from nas.search_algorithm import NASSearcher

if __name__ == "__main__":
    print("Starting Neural Architecture Search application...")

    search_space = {
        "layer_types": ["conv", "dense"],
        "filters": [16, 32, 64],
        "kernel_sizes": [(3,3), (5,5)],
        "units": [64, 128, 256],
        "activations": ["relu", "tanh", "sigmoid"]
    }

    nas_searcher = NASSearcher(search_space, num_iterations=50)
    best_arch = nas_searcher.search()
    print(f"Final Best Architecture: {best_arch}")

    print("Neural Architecture Search application finished.")
