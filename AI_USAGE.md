# AI Usage

## Lab 3: AI-assisted FASTA cleaning

Tool used: ChatGPT (GPT-5.6 Sol)

Prompt used:

> Clean the following messy FASTA records into a structured table. For each record, extract and standardize these fields: sample_id, organism, gene, reported_length, actual_sequence_length, and sequence.
>
> Standardize sample IDs to the format sample_001, sample_002, etc. Standardize all organism variants such as Homo_sapiens, Homo sapiens, H.sapiens, and Hsapiens to "Homo sapiens". Standardize gene names to uppercase. Preserve a reported sequence length only when it is explicitly given in the FASTA header; if it is missing or listed as NA, return NA rather than inferring it. Calculate actual_sequence_length directly from the sequence. Return the result as a CSV-compatible structured table, not free-form prose.
>
> Input file: messy_sequences.fasta

I used the AI-generated structured output as the comparison dataset for the regex-based cleaning approach. I reviewed the output against the original FASTA records before comparing it with the regex output.