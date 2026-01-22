---
layout: default
title: What Makes Low-Bit Quantization-Aware Training Work for Reasoning LLMs? A Systematic Study
---

# What Makes Low-Bit Quantization-Aware Training Work for Reasoning LLMs? A Systematic Study
**arXiv**：[2601.14888v1](https://arxiv.org/abs/2601.14888) · [PDF](https://arxiv.org/pdf/2601.14888.pdf)  
**作者**：Keyu Lv, Manyi Zhang, Xiaobo Xia, Jingchen Ni, Shannan Yan, Xianzhi Yu, Lu Hou, Chun Yuan, Haoli Bai  

**一句话要点**：提出系统化量化感知训练方法以提升推理大语言模型的低比特量化效率

**关键词**：量化感知训练, 推理大语言模型, 知识蒸馏, 低比特量化, 强化学习, 域对齐

## 3 点简述
- 核心问题：推理模型在低比特量化后精度下降显著，影响推理效率。
- 方法要点：通过知识蒸馏、PTQ初始化、强化学习和域对齐优化QAT流程。
- 实验效果：在多个模型和数据集上超越现有PTQ方法，如Qwen3-0.6B在MATH-500上提升44.53%。

## 摘要（原文）

> Reasoning models excel at complex tasks such as coding and mathematics, yet their inference is often slow and token-inefficient. To improve the inference efficiency, post-training quantization (PTQ) usually comes with the cost of large accuracy drops, especially for reasoning tasks under low-bit settings. In this study, we present a systematic empirical study of quantization-aware training (QAT) for reasoning models. Our key findings include: (1) Knowledge distillation is a robust objective for reasoning models trained via either supervised fine-tuning or reinforcement learning; (2) PTQ provides a strong initialization for QAT, improving accuracy while reducing training cost; (3) Reinforcement learning remains feasible for quantized models given a viable cold start and yields additional gains; and (4) Aligning the PTQ calibration domain with the QAT training domain accelerates convergence and often improves the final accuracy. Finally, we consolidate these findings into an optimized workflow (Reasoning-QAT), and show that it consistently outperforms state-of-the-art PTQ methods across multiple LLM backbones and reasoning datasets. For instance, on Qwen3-0.6B, it surpasses GPTQ by 44.53% on MATH-500 and consistently recovers performance in the 2-bit regime.

