---
layout: default
title: Benchmarking Post-Training Quantization of Large Language Models under Microscaling Floating Point Formats
---

# Benchmarking Post-Training Quantization of Large Language Models under Microscaling Floating Point Formats
**arXiv**：[2601.09555v1](https://arxiv.org/abs/2601.09555) · [PDF](https://arxiv.org/pdf/2601.09555.pdf)  
**作者**：Manyi Zhang, Ji-Fu Li, Zhongao Sun, Haoli Bai, Hui-Ling Zhen, Zhenhua Dong, Xianzhi Yu  

**一句话要点**：系统评估大语言模型在微缩放浮点格式下的后训练量化，提供实用指导

**关键词**：后训练量化, 微缩放浮点格式, 大语言模型, 低精度计算, 量化敏感性, 预缩放优化

## 3 点简述
- 核心问题：微缩放浮点格式下后训练量化的适用性和行为未知
- 方法要点：涵盖7种以上算法、15个基准和3个模型家族的系统研究
- 实验或效果：MXFP8近无损，MXFP4挑战大，量化敏感性由语言模型主导

## 摘要（原文）

> Microscaling Floating-Point (MXFP) has emerged as a promising low-precision format for large language models (LLMs). Despite various post-training quantization (PTQ) algorithms being proposed, they mostly focus on integer quantization, while their applicability and behavior under MXFP formats remain largely unexplored. To address this gap, this work conducts a systematic investigation of PTQ under MXFP formats, encompassing over 7 PTQ algorithms, 15 evaluation benchmarks, and 3 LLM families. The key findings include: 1) MXFP8 consistently achieves near-lossless performance, while MXFP4 introduces substantial accuracy degradation and remains challenging; 2) PTQ effectiveness under MXFP depends strongly on format compatibility, with some algorithmic paradigms being consistently more effective than others; 3) PTQ performance exhibits highly consistent trends across model families and modalities, in particular, quantization sensitivity is dominated by the language model rather than the vision encoder in multimodal LLMs; 4) The scaling factor of quantization is a critical error source in MXFP4, and a simple pre-scale optimization strategy can significantly mitigate its impact. Together, these results provide practical guidance on adapting existing PTQ methods to MXFP quantization.

