---
layout: default
title: Questioning the Stability of Visual Question Answering
---

# Questioning the Stability of Visual Question Answering
**arXiv**：[2511.11206v1](https://arxiv.org/abs/2511.11206) · [PDF](https://arxiv.org/pdf/2511.11206.pdf)  
**作者**：Amir Rosenfeld, Neta Glazer, Ethan Fetaya  

**一句话要点**：揭示视觉语言模型对微小语义不变扰动的脆弱性，并利用稳定性预测模型正确性。

**关键词**：视觉语言模型, 鲁棒性评估, 语义不变扰动, 稳定性分析, 模型预测

## 3 点简述
- 核心问题：现代视觉语言模型对像素级变换、重述等语义不变扰动高度敏感，影响可靠性。
- 方法要点：系统评估多种扰动类型，分析稳定性与模型、问题类别的关系。
- 实验效果：稳定样本更可能正确，小模型稳定性可预测大模型正确性，精度高。

## 摘要（原文）

> Visual Language Models (VLMs) have achieved remarkable progress, yet their reliability under small, meaning-preserving input changes remains poorly understood. We present the first large-scale, systematic study of VLM robustness to benign visual and textual perturbations: pixel-level shifts, light geometric transformations, padded rescaling, paraphrasing, and multilingual rewrites that do not alter the underlying semantics of an image-question pair. Across a broad set of models and datasets, we find that modern VLMs are highly sensitive to such minor perturbations: a substantial fraction of samples change their predicted answer under at least one visual or textual modification. We characterize how this instability varies across perturbation types, question categories, and models, revealing that even state-of-the-art systems (e.g., GPT-4o, Gemini 2.0 Flash) frequently fail under shifts as small as a few pixels or harmless rephrasings. We further show that sample-level stability serves as a strong indicator of correctness: stable samples are consistently far more likely to be answered correctly. Leveraging this, we demonstrate that the stability patterns of small, accessible open-source models can be used to predict the correctness of much larger closed-source models with high precision. Our findings expose a fundamental fragility in current VLMs and highlight the need for robustness evaluations that go beyond adversarial perturbations, focusing instead on invariances that models should reliably uphold.

