
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
# Update on 2023-01-19 00:00:00
# Update on 2023-01-19 00:00:00
# Update on 2023-01-19 00:00:00
# Update on 2023-01-20 00:00:00
# Update on 2023-01-20 00:00:00
# Update on 2023-01-25 00:00:00
# Update on 2023-01-25 00:00:00
# Update on 2023-01-30 00:00:00
# Update on 2023-02-03 00:00:00
# Update on 2023-02-03 00:00:00
# Update on 2023-02-03 00:00:00
# Update on 2023-02-06 00:00:00
# Update on 2023-02-06 00:00:00
# Update on 2023-02-06 00:00:00
# Update on 2023-02-13 00:00:00
# Update on 2023-02-16 00:00:00
# Update on 2023-02-17 00:00:00
# Update on 2023-02-17 00:00:00
# Update on 2023-02-17 00:00:00
# Update on 2023-02-23 00:00:00
# Update on 2023-02-27 00:00:00
# Update on 2023-02-27 00:00:00
# Update on 2023-03-02 00:00:00
# Update on 2023-03-06 00:00:00
# Update on 2023-03-06 00:00:00
# Update on 2023-03-06 00:00:00
# Update on 2023-03-07 00:00:00
# Update on 2023-03-07 00:00:00
# Update on 2023-03-08 00:00:00
# Update on 2023-03-09 00:00:00
# Update on 2023-03-09 00:00:00
# Update on 2023-03-10 00:00:00
# Update on 2023-03-13 00:00:00
# Update on 2023-03-13 00:00:00
# Update on 2023-03-14 00:00:00
# Update on 2023-03-14 00:00:00
# Update on 2023-03-15 00:00:00
# Update on 2023-03-17 00:00:00
# Update on 2023-03-20 00:00:00
# Update on 2023-03-21 00:00:00
# Update on 2023-03-24 00:00:00
# Update on 2023-03-27 00:00:00
# Update on 2023-03-27 00:00:00
# Update on 2023-03-28 00:00:00
# Update on 2023-03-29 00:00:00
# Update on 2023-03-29 00:00:00
# Update on 2023-03-31 00:00:00
# Update on 2023-04-04 00:00:00
# Update on 2023-04-05 00:00:00
# Update on 2023-04-06 00:00:00
# Update on 2023-04-07 00:00:00
# Update on 2023-04-10 00:00:00
# Update on 2023-04-11 00:00:00
# Update on 2023-04-12 00:00:00
# Update on 2023-04-13 00:00:00
# Update on 2023-04-13 00:00:00
# Update on 2023-04-17 00:00:00
# Update on 2023-04-18 00:00:00
# Update on 2023-04-19 00:00:00
# Update on 2023-04-19 00:00:00
# Update on 2023-04-26 00:00:00
# Update on 2023-04-27 00:00:00
# Update on 2023-04-27 00:00:00
# Update on 2023-04-28 00:00:00
# Update on 2023-04-28 00:00:00
# Update on 2023-05-03 00:00:00
# Update on 2023-05-05 00:00:00
# Update on 2023-05-05 00:00:00
# Update on 2023-05-09 00:00:00
# Update on 2023-05-11 00:00:00
# Update on 2023-05-15 00:00:00
# Update on 2023-05-15 00:00:00
# Update on 2023-05-17 00:00:00
# Update on 2023-05-18 00:00:00
# Update on 2023-05-19 00:00:00
# Update on 2023-05-23 00:00:00
# Update on 2023-05-25 00:00:00
# Update on 2023-05-31 00:00:00
# Update on 2023-06-02 00:00:00
# Update on 2023-06-06 00:00:00
# Update on 2023-06-06 00:00:00
# Update on 2023-06-08 00:00:00
# Update on 2023-06-09 00:00:00
# Update on 2023-06-12 00:00:00
# Update on 2023-06-13 00:00:00
# Update on 2023-06-15 00:00:00
# Update on 2023-06-16 00:00:00
# Update on 2023-06-16 00:00:00
# Update on 2023-06-20 00:00:00
# Update on 2023-06-21 00:00:00
# Update on 2023-06-22 00:00:00
# Update on 2023-06-23 00:00:00
# Update on 2023-06-23 00:00:00
# Update on 2023-06-26 00:00:00
# Update on 2023-06-27 00:00:00
# Update on 2023-06-27 00:00:00
# Update on 2023-06-30 00:00:00
# Update on 2023-07-03 00:00:00
# Update on 2023-07-03 00:00:00
# Update on 2023-07-04 00:00:00
# Update on 2023-07-07 00:00:00
# Update on 2023-07-20 00:00:00
# Update on 2023-07-20 00:00:00
# Update on 2023-07-21 00:00:00
# Update on 2023-07-24 00:00:00
# Update on 2023-07-24 00:00:00
# Update on 2023-07-25 00:00:00
# Update on 2023-07-26 00:00:00
# Update on 2023-07-27 00:00:00
# Update on 2023-07-28 00:00:00
# Update on 2023-07-31 00:00:00
# Update on 2023-08-01 00:00:00
# Update on 2023-08-03 00:00:00
# Update on 2023-08-04 00:00:00
# Update on 2023-08-08 00:00:00
# Update on 2023-08-08 00:00:00
# Update on 2023-08-09 00:00:00
# Update on 2023-08-09 00:00:00
# Update on 2023-08-09 00:00:00