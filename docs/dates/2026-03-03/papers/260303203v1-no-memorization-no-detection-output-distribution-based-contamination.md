---
layout: default
title: No Memorization, No Detection: Output Distribution-Based Contamination Detection in Small Language Models
---

# No Memorization, No Detection: Output Distribution-Based Contamination Detection in Small Language Models
**arXiv**：[2603.03203v1](https://arxiv.org/abs/2603.03203) · [PDF](https://arxiv.org/pdf/2603.03203.pdf)  
**作者**：Omer Sela  

**一句话要点**：提出基于输出分布的污染检测方法，揭示小语言模型中记忆化阈值对检测效果的影响

**关键词**：数据污染检测, 输出分布分析, 小语言模型, 记忆化阈值, 参数高效微调

## 3 点简述
- 研究基于输出分布峰值检测数据污染的方法在小语言模型中的有效性
- 发现检测效果取决于微调是否导致逐字记忆，低秩适应可避免记忆化
- 通过GSM8K等数据集实验，显示参数高效微调可能产生不可检测的污染

## 摘要（原文）

> CDD, or Contamination Detection via output Distribution, identifies data contamination by measuring the peakedness of a model's sampled outputs. We study the conditions under which this approach succeeds and fails on small language models ranging from 70M to 410M parameters. Using controlled contamination experiments on GSM8K, HumanEval, and MATH, we find that CDD's effectiveness depends critically on whether fine-tuning produces verbatim memorization. With low-rank adaptation, models can learn from contaminated data without memorizing it, and CDD performs at chance level even when the data is verifiably contaminated. Only when fine-tuning capacity is sufficient to induce memorization does CDD recover strong detection accuracy. Our results characterize a memorization threshold that governs detectability and highlight a practical consideration: parameter-efficient fine-tuning can produce contamination that output-distribution methods do not detect. Our code is available at https://github.com/Sela-Omer/Contamination-Detection-Small-LM

