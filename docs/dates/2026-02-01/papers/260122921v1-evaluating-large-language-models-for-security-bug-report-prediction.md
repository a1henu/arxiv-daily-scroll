---
layout: default
title: Evaluating Large Language Models for Security Bug Report Prediction
---

# Evaluating Large Language Models for Security Bug Report Prediction
**arXiv**：[2601.22921v1](https://arxiv.org/abs/2601.22921) · [PDF](https://arxiv.org/pdf/2601.22921.pdf)  
**作者**：Farnaz Soltaniani, Shoaib Razzaq, Mohammad Ghafari  

**一句话要点**：评估大语言模型在安全漏洞报告预测中的提示工程与微调方法

**关键词**：安全漏洞报告预测, 大语言模型评估, 提示工程, 微调方法, 性能权衡

## 3 点简述
- 核心问题：早期检测安全漏洞报告对及时缓解漏洞至关重要，需高效预测方法。
- 方法要点：比较基于提示的工程和微调方法，分析两者在敏感度、精确度和召回率上的权衡。
- 实验或效果：提示方法平均G-measure达77%，但精确度仅22%；微调方法精确度75%，但召回率36%，推理速度更快。

## 摘要（原文）

> Early detection of security bug reports (SBRs) is critical for timely vulnerability mitigation. We present an evaluation of prompt-based engineering and fine-tuning approaches for predicting SBRs using Large Language Models (LLMs). Our findings reveal a distinct trade-off between the two approaches. Prompted proprietary models demonstrate the highest sensitivity to SBRs, achieving a G-measure of 77% and a recall of 74% on average across all the datasets, albeit at the cost of a higher false-positive rate, resulting in an average precision of only 22%. Fine-tuned models, by contrast, exhibit the opposite behavior, attaining a lower overall G-measure of 51% but substantially higher precision of 75% at the cost of reduced recall of 36%. Though a one-time investment in building fine-tuned models is necessary, the inference on the largest dataset is up to 50 times faster than that of proprietary models. These findings suggest that further investigations to harness the power of LLMs for SBR prediction are necessary.

