---
layout: default
title: Up to 36x Speedup: Mask-based Parallel Inference Paradigm for Key Information Extraction in MLLMs
---

# Up to 36x Speedup: Mask-based Parallel Inference Paradigm for Key Information Extraction in MLLMs
**arXiv**：[2601.19613v1](https://arxiv.org/abs/2601.19613) · [PDF](https://arxiv.org/pdf/2601.19613.pdf)  
**作者**：Xinzhong Wang, Ya Guo, Jing Li, Huan Chen, Yi Tu, Yijie Hong, Gongshen Liu, Huijia Zhu  

**一句话要点**：提出基于掩码的并行推理范式PIP，以解决多模态大语言模型在关键信息提取中的效率瓶颈。

**关键词**：关键信息提取, 并行推理, 掩码预训练, 多模态大语言模型, 视觉丰富文档

## 3 点简述
- 核心问题：传统自回归推理在提取多字段时效率低下，成为关键信息提取的瓶颈。
- 方法要点：使用掩码令牌作为占位符，实现目标值的单次前向并行生成，并开发掩码预训练策略。
- 实验或效果：PIP模型在保持高精度的同时，实现5-36倍推理加速，适用于实际场景。

## 摘要（原文）

> Key Information Extraction (KIE) from visually-rich documents (VrDs) is a critical task, for which recent Large Language Models (LLMs) and Multi-Modal Large Language Models (MLLMs) have demonstrated strong potential. However, their reliance on autoregressive inference, which generates outputs sequentially, creates a significant efficiency bottleneck, especially as KIE tasks often involve extracting multiple, semantically independent fields. To overcome this limitation, we introduce PIP: a Parallel Inference Paradigm for KIE. Our approach reformulates the problem by using "[mask]" tokens as placeholders for all target values, enabling their simultaneous generation in a single forward pass. To facilitate this paradigm, we develop a tailored mask pre-training strategy and construct large-scale supervised datasets. Experimental results show that our PIP-models achieve a 5-36x inference speedup with negligible performance degradation compared to traditional autoregressive base models. By substantially improving efficiency while maintaining high accuracy, PIP paves the way for scalable and practical real-world KIE solutions.

