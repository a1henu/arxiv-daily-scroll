---
layout: default
title: Layer-wise Positional Bias in Short-Context Language Modeling
---

# Layer-wise Positional Bias in Short-Context Language Modeling
**arXiv**：[2601.04098v1](https://arxiv.org/abs/2601.04098) · [PDF](https://arxiv.org/pdf/2601.04098.pdf)  
**作者**：Maryam Rahimi, Mahdi Nouri, Yadollah Yaghoobzadeh  

**一句话要点**：提出基于归因的框架分析短上下文语言建模中的层间位置偏好

**关键词**：位置偏好, 层间分析, 短上下文建模, 归因框架, 语言模型架构

## 3 点简述
- 研究语言模型输入位置偏好，关注层间与位置演化，独立于任务复杂度
- 采用层传导与滑动窗口方法，量化各层对输入位置的重要性分布
- 发现架构特异性、输入稳定性、词序不变性，以及深度相关的近因与首因偏好

## 摘要（原文）

> Language models often show a preference for using information from specific positions in the input regardless of semantic relevance. While positional bias has been studied in various contexts, from attention sinks to task performance degradation in long-context settings, prior work has not established how these biases evolve across individual layers and input positions, or how they vary independent of task complexity. We introduce an attribution-based framework to analyze positional effects in short-context language modeling. Using layer conductance with a sliding-window approach, we quantify how each layer distributes importance across input positions, yielding layer-wise positional importance profiles. We find that these profiles are architecture-specific, stable across inputs, and invariant to lexical scrambling. Characterizing these profiles, we find prominent recency bias that increases with depth and subtle primacy bias that diminishes through model depth. Beyond positional structure, we also show that early layers preferentially weight content words over function words across all positions, while later layers lose this word-type differentiation.

