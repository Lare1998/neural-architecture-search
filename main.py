
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

# Update on 2023-01-02 00:00:00
# Update on 2023-01-03 00:00:00
# Update on 2023-01-04 00:00:00
# Update on 2023-01-05 00:00:00
# Update on 2023-01-06 00:00:00
# Update on 2023-01-09 00:00:00
# Update on 2023-01-09 00:00:00
# Update on 2023-01-11 00:00:00
# Update on 2023-01-11 00:00:00
# Update on 2023-01-16 00:00:00
# Update on 2023-01-18 00:00:00