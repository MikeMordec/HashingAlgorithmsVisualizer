HashingAlgorithmsVisualizer

HashingAlgorithmsVisualizer is a Python tool designed to visualize and compare different hashing techniques. It includes implementations for linear probing, quadratic probing, and double hashing methods. The tool processes data from input files to analyze and compare collision behavior and performance across different hashing strategies.
Features

    Implements linear probing, quadratic probing, and double hashing algorithms.
    Analyzes and compares collision counts for each hashing method.
    Processes data in random, ascending, and descending orders.
    Outputs detailed collision information and hash table contents.

Usage

    Prepare Input Files: Ensure you have input files named in<n>.txt where <n> represents a numeric identifier (e.g., in150.txt). Each file should contain numbers to be processed.

    Run the Script: Execute the script using Python. The script will read from the input files, process the data using different hashing methods, and write results to output files.

    bash

    python your_script_name.py

    Output Files: The script generates output files named out<n>_collisions_actual.txt and out<n>_tables_actual.txt. These files contain:
        Collision statistics for each hashing method.
        Details of hash table contents after processing.

Example

To run the script and analyze hashing algorithms for a specific set of input files, place the required files in the working directory and execute:

bash

python HashingAlgorithmsVisualizer.py

The script will produce results comparing collisions and hash table contents for the input data.
Files

    HashingAlgorithmsVisualizer.py: Main script for processing and visualizing hash table algorithms.
    LinearProbingHash.py: Module containing the linear probing hash table implementation.
    in<n>.txt: Input files with numbers for hashing analysis.
    out<n>_collisions_actual.txt: Output file with collision statistics.
    out<n>_tables_actual.txt: Output file with hash table contents.
