---
layout: default
title: Causal Discovery for Explainable AI: A Dual-Encoding Approach
---

# Causal Discovery for Explainable AI: A Dual-Encoding Approach
**arXiv**：[2601.21221v1](https://arxiv.org/abs/2601.21221) · [PDF](https://arxiv.org/pdf/2601.21221.pdf)  
**作者**：Henry Salgado, Meagan R. Kendall, Martine Ceberio  

**一句话要点**：提出双编码因果发现方法以解决分类变量在可解释AI中的因果推断问题

**关键词**：因果发现, 可解释AI, 分类变量, 约束基算法, 双编码策略

## 3 点简述
- 核心问题：传统因果发现方法在处理分类变量时，因条件独立性测试数值不稳定而受限
- 方法要点：采用互补编码策略运行约束基算法，并通过多数投票合并结果
- 实验或效果：在泰坦尼克数据集上应用，识别出与现有可解释方法一致的因果结构

## 摘要（原文）

> Understanding causal relationships among features is fundamental for explaining machine learning model decisions. However, traditional causal discovery methods face challenges with categorical variables due to numerical instability in conditional independence testing. We propose a dual-encoding causal discovery approach that addresses these limitations by running constraint-based algorithms with complementary encoding strategies and merging results through majority voting. Applied to the Titanic dataset, our method identifies causal structures that align with established explainable methods.

