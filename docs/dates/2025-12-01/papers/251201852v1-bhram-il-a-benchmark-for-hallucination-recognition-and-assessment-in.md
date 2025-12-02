---
layout: default
title: BHRAM-IL: A Benchmark for Hallucination Recognition and Assessment in Multiple Indian Languages
---

# BHRAM-IL: A Benchmark for Hallucination Recognition and Assessment in Multiple Indian Languages
**arXiv**：[2512.01852v1](https://arxiv.org/abs/2512.01852) · [PDF](https://arxiv.org/pdf/2512.01852.pdf)  
**作者**：Hrishikesh Terdalkar, Kirtan Bhojani, Aryan Dongare, Omm Aditya Behera  

**一句话要点**：提出BHRAM-IL基准，用于评估多印度语言中的幻觉识别与评估。

**关键词**：幻觉检测, 多语言基准, 印度语言, 大语言模型评估, 事实性任务

## 3 点简述
- 核心问题：大语言模型在多语言应用中常产生幻觉，印度语言研究不足。
- 方法要点：构建涵盖印地语等语言的基准，包含36,047个问题，覆盖九类任务。
- 实验或效果：评估14个多语言模型，提供标准化分数，支持未来研究。

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed in multilingual applications but often generate plausible yet incorrect or misleading outputs, known as hallucinations. While hallucination detection has been studied extensively in English, under-resourced Indian languages remain largely unexplored. We present BHRAM-IL, a benchmark for hallucination recognition and assessment in multiple Indian languages, covering Hindi, Gujarati, Marathi, Odia, along with English. The benchmark comprises 36,047 curated questions across nine categories spanning factual, numerical, reasoning, and linguistic tasks. We evaluate 14 state-of-the-art multilingual LLMs on a benchmark subset of 10,265 questions, analyzing cross-lingual and factual hallucinations across languages, models, scales, categories, and domains using category-specific metrics normalized to (0,1) range. Aggregation over all categories and models yields a primary score of 0.23 and a language-corrected fuzzy score of 0.385, demonstrating the usefulness of BHRAM-IL for hallucination-focused evaluation. The dataset, and the code for generation and evaluation are available on GitHub (https://github.com/sambhashana/BHRAM-IL/) and HuggingFace (https://huggingface.co/datasets/sambhashana/BHRAM-IL/) to support future research in multilingual hallucination detection and mitigation.

