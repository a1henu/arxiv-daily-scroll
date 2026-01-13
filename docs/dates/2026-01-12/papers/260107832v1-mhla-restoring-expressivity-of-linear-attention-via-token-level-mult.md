---
layout: default
title: MHLA: Restoring Expressivity of Linear Attention via Token-Level Multi-Head
---

# MHLA: Restoring Expressivity of Linear Attention via Token-Level Multi-Head
**arXiv**：[2601.07832v1](https://arxiv.org/abs/2601.07832) · [PDF](https://arxiv.org/pdf/2601.07832.pdf)  
**作者**：Kewei Zhang, Ye Huang, Yufan Deng, Jincheng Yu, Junsong Chen, Huan Ling, Enze Xie, Daquan Zhou  

**一句话要点**：提出MHLA以解决线性注意力全局上下文坍缩问题，恢复表达力并保持线性复杂度。

**关键词**：线性注意力, 多头注意力, 全局上下文坍缩, 表达力恢复, 线性复杂度, 多领域应用

## 3 点简述
- 核心问题：线性注意力导致全局上下文坍缩，降低模型表达多样性。
- 方法要点：通过令牌维度多头划分计算注意力，保持多样性且维持线性复杂度。
- 实验或效果：在图像分类、NLP、图像生成和视频生成任务中验证性能提升。

## 摘要（原文）

> While the Transformer architecture dominates many fields, its quadratic self-attention complexity hinders its use in large-scale applications. Linear attention offers an efficient alternative, but its direct application often degrades performance, with existing fixes typically re-introducing computational overhead through extra modules (e.g., depthwise separable convolution) that defeat the original purpose. In this work, we identify a key failure mode in these methods: global context collapse, where the model loses representational diversity. To address this, we propose Multi-Head Linear Attention (MHLA), which preserves this diversity by computing attention within divided heads along the token dimension. We prove that MHLA maintains linear complexity while recovering much of the expressive power of softmax attention, and verify its effectiveness across multiple domains, achieving a 3.6\% improvement on ImageNet classification, a 6.3\% gain on NLP, a 12.6\% improvement on image generation, and a 41\% enhancement on video generation under the same time complexity.

