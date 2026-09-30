# Lab 3: Parsing Messy Genomic Data

This repository contains my Lab 3 work using the `messy_sequences.fasta` dataset.

The goal of the lab was to clean inconsistent FASTA headers using two approaches:
1. a Python regular-expression parser
2. AI-assisted extraction

The two outputs were then compared for agreement, edge cases, and failure modes.

## Repository structure

- `data/messy_sequences.fasta`  
  Original messy FASTA input file.

- `src/clean_regex.py`  
  Python script that reads the FASTA file, parses the inconsistent headers with regular expressions, standardizes the fields, calculates actual sequence length, and writes a cleaned CSV file.

- `src/compare_outputs.py`  
  Python script that compares the regex-cleaned output with the AI-assisted output field by field.

- `output/regex_cleaned_sequences.csv`  
  Structured output produced by the regex script.

- `output/ai_cleaned_sequences.csv`  
  Structured output produced using AI-assisted extraction.

- `output/comparison_results.csv`  
  Field-by-field comparison of the regex and AI outputs.

- `comparison.md`  
  Written comparison of the two approaches, including agreement, edge cases, failure modes, and time/effort.

- `AI_USAGE.md`  
  Documents the AI tool and prompt used.

## How to run the regex cleaning script

From the repository root, run:

```bash
python src/clean_regex.py
