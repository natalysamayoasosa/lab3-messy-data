# Lab 3 Comparison: Regex vs. AI-Assisted FASTA Cleaning

## Agreement and disagreement

The regex-based and AI-assisted approaches produced the same structured output for all eight FASTA records. Across the six fields included in the comparison, there were 48 out of 48 matches and no disagreements. Both approaches successfully standardized the sample IDs, organism names, and gene names, while also preserving missing reported lengths as NA.

Both methods also handled the different FASTA header styles successfully. For example, sample_004 used `species=H.sapiens` and `target=BRCA1`, while sample_006 used the shorter format `seq6|Hsapiens|EGFR`. Even though these headers used different labels and separators, both methods standardized them to the same organism, gene, and sample ID values.

## Edge cases and failure modes

Even though the final outputs agreed, some records showed why messy metadata can still create problems. In sample_003, the FASTA header reported a sequence length of 150 bp, but the actual sequence contained 157 bases. Similarly, sample_005 reported 130 bp in the header, while the sequence itself contained 144 bases. If either cleaning approach trusted only the reported metadata, these records would contain incorrect sequence-length information.

Another possible failure mode is inconsistent naming. Sample_006 used `Hsapiens` instead of a more standard form such as `Homo_sapiens`, and its sample ID was written as `seq6` rather than `sample_006`. The regex solution required specific patterns to recognize these variants. If a new spelling appeared that was not included in the regular expression, the regex approach could fail to standardize it. The AI approach was more flexible with wording, but its output still needed to be checked because an AI system could infer or standardize a value incorrectly.

## Time and effort comparison

The AI-assisted method was faster to produce because I could describe the desired standardized fields and formatting in one prompt. The regex method took more time because I had to inspect the different header formats, write patterns for each type of variation, and debug the sequence-length extraction. However, I would trust the regex script more for repeatedly processing a known dataset because its rules are explicit and reproducible. For unfamiliar or highly variable text, the AI approach may be faster initially, but I would still verify its output before using it for analysis.