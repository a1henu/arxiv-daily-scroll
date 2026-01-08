---
layout: default
title: Reasoning Pattern Alignment Merging for Adaptive Reasoning
---

# Reasoning Pattern Alignment Merging for Adaptive Reasoning
**arXiv**：[2601.03506v1](https://arxiv.org/abs/2601.03506) · [PDF](https://arxiv.org/pdf/2601.03506.pdf)  
**作者**：Zhaofeng Zhong, Wei Yuan, Tong Chen, Xiangyu Zhao, Quoc Viet Hung Nguyen, Hongzhi Yin  

**一句话要点**：提出推理模式对齐合并框架，以轻量级方式实现自适应推理并降低计算成本。

**关键词**：模型合并, 自适应推理, 特征对齐, 推理效率, 层间优化

## 3 点简述
- 核心问题：大型推理模型生成冗长推理路径，导致计算开销和延迟过高。
- 方法要点：通过层间特征对齐合并长链推理模型与短链指令模型，无需从头训练。
- 实验或效果：在七个推理基准上显著减少推理成本，同时保持强性能。

## 摘要（原文）

> Recent large reasoning models (LRMs) have made substantial progress in complex reasoning tasks, yet they often generate lengthy reasoning paths for every query, incurring unnecessary computation and latency. Existing speed-up approaches typically rely on retraining the model or designing sophisticated prompting, which are either prohibitively expensive or highly sensitive to the input and prompt formulation. In this work, we study model merging as a lightweight alternative for efficient reasoning: by combining a long chain-of-thought (Long-CoT) reasoning model with a Short-CoT instruction model, we obtain an adaptive reasoner without training from scratch or requiring large-scale additional data. Building on this idea, we propose Reasoning Pattern Alignment Merging (RPAM), a layer-wise model merging framework based on feature alignment to facilitate query-adaptive reasoning. RPAM first constructs a small pattern-labeled calibration set that assigns each query an appropriate reasoning pattern. It then optimizes layer-wise merging coefficients by aligning the merged model's intermediate representations with those of the selected model, while a contrastive objective explicitly pushes them away from the non-selected model. Experiments on seven widely used reasoning benchmarks show that RPAM substantially reduces inference cost while maintaining strong performance. Upon article acceptance, we will provide open-source code to reproduce experiments for RPAM.

