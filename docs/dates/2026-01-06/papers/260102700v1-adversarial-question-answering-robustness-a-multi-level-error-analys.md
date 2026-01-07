---
layout: default
title: Adversarial Question Answering Robustness: A Multi-Level Error Analysis and Mitigation Study
---

# Adversarial Question Answering Robustness: A Multi-Level Error Analysis and Mitigation Study
**arXiv**：[2601.02700v1](https://arxiv.org/abs/2601.02700) · [PDF](https://arxiv.org/pdf/2601.02700.pdf)  
**作者**：Agniv Roy Choudhury, Vignesh Ponselvan Rajasingh  

**一句话要点**：提出基于NER引导对比学习的对抗缓解策略，以提升问答系统在AddSent数据集上的鲁棒性。

**关键词**：对抗问答鲁棒性, 多级错误分析, 实体感知对比学习, 对抗微调, 数据增强, ELECTRA模型

## 3 点简述
- 核心问题：问答系统在标准基准上表现优异，但对AddSent对抗样本脆弱。
- 方法要点：通过多级错误分析识别主要失败模式，并评估对抗微调与数据增强策略。
- 实验或效果：ELECTRA-base模型消除鲁棒性-准确性权衡，实体感知对比学习实现94.9%对抗差距闭合。

## 摘要（原文）

> Question answering (QA) systems achieve impressive performance on standard benchmarks like SQuAD, but remain vulnerable to adversarial examples. This project investigates the adversarial robustness of transformer models on the AddSent adversarial dataset through systematic experimentation across model scales and targeted mitigation strategies. We perform comprehensive multi-level error analysis using five complementary categorization schemes, identifying negation confusion and entity substitution as the primary failure modes. Through systematic evaluation of adversarial fine-tuning ratios, we identify 80% clean + 20% adversarial data as optimal. Data augmentation experiments reveal a capacity bottleneck in small models. Scaling from ELECTRA-small (14M parameters) to ELECTRA-base (110M parameters) eliminates the robustness-accuracy trade-off, achieving substantial improvements on both clean and adversarial data. We implement three targeted mitigation strategies, with Entity-Aware contrastive learning achieving best performance: 89.89% AddSent Exact Match (EM) and 90.73% SQuAD EM, representing 94.9% closure of the adversarial gap. To our knowledge, this is the first work integrating comprehensive linguistic error analysis with Named Entity Recognition (NER)-guided contrastive learning for adversarial QA, demonstrating that targeted mitigation can achieve near-parity between clean and adversarial performance.

