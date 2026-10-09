# 3. Preliminary Research Gap and Proposed Title

## Proposed title
**A Comparative Evaluation of Traditional Machine Learning and Large Language Models for Phishing Email Detection**

This narrower title focuses on email detection, which may be easier to compare fairly than mixing email, URLs and website screenshots. If the final paper set or project scope is broader, revise the title accordingly.

## What the initial review suggests
The reviewed literature covers several different tasks:
- detecting phishing websites using blacklists, similarity checks and machine learning;
- detecting phishing emails with NLP and text classification;
- deep-learning and transformer-based approaches;
- LLM use in cybersecurity, including both attack generation and defensive detection;
- feature engineering, datasets, evaluation and generalisation.

These are **themes observed in the reviewed publisher records**, not yet a proof that no previous study has done a particular comparison.

## Candidate gap to investigate
A potentially useful gap is the need for a **carefully controlled, reproducible comparison** of a traditional ML baseline and an LLM-based detector on the same held-out phishing-email dataset, with consistent label definitions and metrics beyond accuracy.

Before claiming this is a genuine gap:
1. Read the full 10–12 papers.
2. Search their related-work and future-work sections for comparisons of ML and LLMs on the same data.
3. Check if newer 2025–2026 studies already fill this gap.
4. Narrow the gap if prior work already performs that exact comparison.

## Draft problem statement
Phishing-email detection research uses a range of text-processing and model approaches. However, reported results can be difficult to compare when papers use different datasets, preprocessing, train/test splits and metrics. This proposed study will investigate how a traditional machine-learning baseline and a selected LLM-based method compare under a common evaluation setup.

## Proposed objectives
1. Select a legally usable, documented phishing-email dataset and define consistent labels.
2. Implement one traditional baseline, such as TF–IDF with Logistic Regression.
3. Evaluate a selected LLM-based classification method using the same test examples where feasible.
4. Compare precision, recall, F1-score, false-positive rate, latency and approximate cost, in addition to accuracy.
5. Document reproducibility, privacy and limitations.

## Proposed hypotheses (optional; refine with mentor)
- H1: The evaluated methods will show different precision/recall trade-offs on the same test set.
- H2: The LLM-based method may provide richer explanations, but may have higher latency or cost than a small traditional baseline.

These are hypotheses to test, not findings.

## Why the title is justified
The title connects a current cybersecurity problem with a measurable research comparison. It is feasible for a student study if the dataset, model access and evaluation procedure are kept manageable. It may provide practical evidence about the trade-off between detection quality, runtime and interpretability.

## Limitations and ethics
- Use only public/licensed datasets and do not collect real credentials.
- Do not send confidential emails or personal data to public LLM services.
- Avoid claiming generalisation beyond the tested dataset.
- Report false positives and false negatives because both can harm legitimate users.
- Record model/version, prompt, date, dataset version and evaluation settings for reproducibility.
