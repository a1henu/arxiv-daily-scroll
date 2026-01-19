---
layout: default
title: Hierarchical Orthogonal Residual Spread for Precise Massive Editing in Large Language Models
---

# Hierarchical Orthogonal Residual Spread for Precise Massive Editing in Large Language Models
**arXiv**：[2601.11441v1](https://arxiv.org/abs/2601.11441) · [PDF](https://arxiv.org/pdf/2601.11441.pdf)  
**作者**：Xiaojie Gu, Guangxu Chen, Yuheng Yang, Jingxin Han, Andi Zhang  

**一句话要点**：提出HORSE方法，通过分层正交残差扩展实现大语言模型中的精确大规模编辑

**关键词**：大语言模型编辑, 分层正交残差, 信息矩阵优化, 模型安全, 梯度噪声减少

## 3 点简述
- 核心问题：大语言模型存在安全风险，现有编辑方法计算成本高且易引发知识冲突
- 方法要点：采用分层正交残差扩展信息矩阵，减少噪声梯度，提升编辑稳定性
- 实验或效果：在多个大语言模型和数据集上验证，HORSE能保持精确的大规模编辑效果

## 摘要（原文）

> Large language models (LLMs) exhibit exceptional performance across various domains, yet they face critical safety concerns. Model editing has emerged as an effective approach to mitigate these issues. Existing model editing methods often focus on optimizing an information matrix that blends new and old knowledge. While effective, these approaches can be computationally expensive and may cause conflicts. In contrast, we shift our attention to Hierarchical Orthogonal Residual SprEad of the information matrix, which reduces noisy gradients and enables more stable edits from a different perspective. We demonstrate the effectiveness of our method HORSE through a clear theoretical comparison with several popular methods and extensive experiments conducted on two datasets across multiple LLMs. The results show that HORSE maintains precise massive editing across diverse scenarios. The code is available at https://github.com/XiaojieGu/HORSE

