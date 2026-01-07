---
layout: default
title: Window-based Membership Inference Attacks Against Fine-tuned Large Language Models
---

# Window-based Membership Inference Attacks Against Fine-tuned Large Language Models
**arXiv**：[2601.02751v1](https://arxiv.org/abs/2601.02751) · [PDF](https://arxiv.org/pdf/2601.02751.pdf)  
**作者**：Yuetian Chen, Yuntao Du, Kaiyuan Zhang, Ashish Kundu, Charles Fleming, Bruno Ribeiro, Ninghui Li  

**一句话要点**：提出基于窗口比较的成员推理攻击方法，以提升微调大语言模型的隐私泄露检测效果。

**关键词**：成员推理攻击, 大语言模型, 隐私泄露, 滑动窗口, 微调模型, 局部信号

## 3 点简述
- 核心问题：传统成员推理攻击依赖全局平均损失，忽略局部记忆信号，导致攻击效果受限。
- 方法要点：采用滑动窗口和基于符号的聚合，通过不同窗口大小捕捉从令牌到短语级的记忆模式。
- 实验或效果：在11个数据集上验证，WBC显著优于基线，AUC更高，低误报率下检测率提升2-3倍。

## 摘要（原文）

> Most membership inference attacks (MIAs) against Large Language Models (LLMs) rely on global signals, like average loss, to identify training data. This approach, however, dilutes the subtle, localized signals of memorization, reducing attack effectiveness. We challenge this global-averaging paradigm, positing that membership signals are more pronounced within localized contexts. We introduce WBC (Window-Based Comparison), which exploits this insight through a sliding window approach with sign-based aggregation. Our method slides windows of varying sizes across text sequences, with each window casting a binary vote on membership based on loss comparisons between target and reference models. By ensembling votes across geometrically spaced window sizes, we capture memorization patterns from token-level artifacts to phrase-level structures. Extensive experiments across eleven datasets demonstrate that WBC substantially outperforms established baselines, achieving higher AUC scores and 2-3 times improvements in detection rates at low false positive thresholds. Our findings reveal that aggregating localized evidence is fundamentally more effective than global averaging, exposing critical privacy vulnerabilities in fine-tuned LLMs.

