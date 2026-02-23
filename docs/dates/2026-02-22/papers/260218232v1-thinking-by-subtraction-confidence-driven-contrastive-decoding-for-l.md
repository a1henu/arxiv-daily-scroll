---
layout: default
title: Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning
---

# Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning
**arXiv**：[2602.18232v1](https://arxiv.org/abs/2602.18232) · [PDF](https://arxiv.org/pdf/2602.18232.pdf)  
**作者**：Lexiang Tang, Weihao Gao, Bingchen Zhao, Lu Ma, Qiao jin, Bang Yang, Yuexian Zou  

**一句话要点**：提出置信驱动对比解码方法，通过针对性低置信度干预提升大语言模型推理可靠性

**关键词**：大语言模型推理, 对比解码, 置信度估计, 推理可靠性, 训练无关方法

## 3 点简述
- 核心问题：推理不确定性高度局部化，少量低置信度令牌导致错误和输出冗余
- 方法要点：检测低置信度令牌，构建对比参考分布，在低置信位置进行减法解码
- 实验或效果：在数学推理基准上显著提升准确性，同时大幅减少输出长度，计算开销小

## 摘要（原文）

> Recent work on test-time scaling for large language model (LLM) reasoning typically assumes that allocating more inference-time computation uniformly improves correctness. However, prior studies show that reasoning uncertainty is highly localized: a small subset of low-confidence tokens disproportionately contributes to reasoning errors and unnecessary output expansion. Motivated by this observation, we propose Thinking by Subtraction, a confidence-driven contrastive decoding approach that improves reasoning reliability through targeted token-level intervention. Our method, Confidence-Driven Contrastive Decoding, detects low-confidence tokens during decoding and intervenes selectively at these positions. It constructs a contrastive reference by replacing high-confidence tokens with minimal placeholders, and refines predictions by subtracting this reference distribution at low-confidence locations. Experiments show that CCD significantly improves accuracy across mathematical reasoning benchmarks while substantially reducing output length, with minimal KV-cache overhead. As a training-free method, CCD enhances reasoning reliability through targeted low-confidence intervention without computational redundancy. Our code will be made available at: https://github.com/bolo-web/CCD.

