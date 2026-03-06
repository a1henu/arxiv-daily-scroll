---
layout: default
title: Differentially Private Multimodal In-Context Learning
---

# Differentially Private Multimodal In-Context Learning
**arXiv**：[2603.04894v1](https://arxiv.org/abs/2603.04894) · [PDF](https://arxiv.org/pdf/2603.04894.pdf)  
**作者**：Ivoline C. Ngong, Zarreen Reza, Joseph P. Near  

**一句话要点**：提出DP-MTV框架，实现差分隐私下的多模态上下文学习，支持大规模演示数据。

**关键词**：差分隐私, 多模态学习, 上下文学习, 任务向量, 视觉语言模型, 隐私保护

## 3 点简述
- 核心问题：现有差分隐私方法局限于少样本文本场景，隐私成本随令牌数增加。
- 方法要点：通过激活空间聚合演示为任务向量，采用分层裁剪和单次噪声添加。
- 实验或效果：在八个基准测试中，ε=1.0时，VizWiz准确率达50%，接近非私有性能。

## 摘要（原文）

> Vision-language models are increasingly applied to sensitive domains such as medical imaging and personal photographs, yet existing differentially private methods for in-context learning are limited to few-shot, text-only settings because privacy cost scales with the number of tokens processed. We present Differentially Private Multimodal Task Vectors (DP-MTV), the first framework enabling many-shot multimodal in-context learning with formal $(\varepsilon, δ)$-differential privacy by aggregating hundreds of demonstrations into compact task vectors in activation space. DP-MTV partitions private data into disjoint chunks, applies per-layer clipping to bound sensitivity, and adds calibrated noise to the aggregate, requiring only a single noise addition that enables unlimited inference queries. We evaluate on eight benchmarks across three VLM architectures, supporting deployment with or without auxiliary data. At $\varepsilon=1.0$, DP-MTV achieves 50% on VizWiz compared to 55% non-private and 35% zero-shot, preserving most of the gain from in-context learning under meaningful privacy constraints.

