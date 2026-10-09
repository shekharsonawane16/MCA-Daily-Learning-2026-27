# 1. Topic, Problem Statement and Objectives

## Proposed topic
**AI-Based Phishing Detection: A Comparative Study of Traditional Machine Learning and Large Language Models**

### Why this topic?
Phishing uses deceptive emails, messages, or websites to persuade people to reveal sensitive information or visit harmful links. Existing research explores blacklists, URL features, traditional machine-learning classifiers, deep learning, natural-language processing and, more recently, large language models (LLMs). The topic is suitable for a research-methodology assignment because there are papers across 2021–2026 and a clear way to compare approaches.

## Preliminary problem statement
Phishing techniques change over time. A detector that performs well on one dataset may not perform equally well on newer or differently sourced examples. Traditional machine-learning methods can be efficient when appropriate features and labelled datasets are available, while LLM-based approaches may interpret message context but can have different cost, latency, privacy and reproducibility characteristics. A comparison must therefore consider more than accuracy alone.

This is a **preliminary** problem statement. Revise it after reading the full papers and confirming what remains unresolved.

## Aim
To review recent research on phishing detection and formulate a fair comparison framework for traditional machine-learning approaches and LLM-based approaches.

## Objectives
1. Classify phishing-detection approaches reported in research published from 2021 to 2026.
2. Identify datasets, input types, evaluation metrics and limitations reported in the selected papers.
3. Compare the reported strengths and weaknesses of traditional ML, deep learning and LLM-based approaches without treating results from different datasets as directly equivalent.
4. Identify a research gap supported by the reviewed papers and propose a feasible future study.

## Preliminary research questions
- RQ1: Which input types are used in recent phishing-detection research (URL, webpage, email text, or multimodal content)?
- RQ2: Which model families and evaluation metrics are reported?
- RQ3: What limitations recur, such as dataset age, dataset imbalance, generalisation, false positives, explainability, privacy, latency or compute cost?
- RQ4: What controlled comparison could fairly evaluate a traditional ML baseline against an LLM-based method?

## Scope
- Primary focus: phishing email/message and phishing URL/website detection.
- Time window: papers published in 2021–2026 inclusive.
- Evidence types: peer-reviewed journal and conference papers, systematic reviews and surveys.
- Exclude unverified blogs, generic web pages and papers whose publication details cannot be confirmed.

## Important comparison rule
Do not claim that model A is “better” than model B merely because one paper reports higher accuracy. A fair comparison requires compatible datasets, train/test procedures, class balance and metrics. Prefer precision, recall, F1-score, false-positive rate, latency and resource requirements alongside accuracy.
