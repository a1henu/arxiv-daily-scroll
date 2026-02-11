---
layout: default
title: Clarifying Shampoo: Adapting Spectral Descent to Stochasticity and the Parameter Trajectory
---

# Clarifying Shampoo: Adapting Spectral Descent to Stochasticity and the Parameter Trajectory
**arXiv**：[2602.09314v1](https://arxiv.org/abs/2602.09314) · [PDF](https://arxiv.org/pdf/2602.09314.pdf)  
**作者**：Runa Eschenhagen, Anna Cai, Tsung-Hsien Lee, Hao-Jun Michael Shi  

**一句话要点**：澄清Shampoo优化器：将谱下降适应随机性与参数轨迹，提升语言模型数据效率

**关键词**：优化器, 谱下降, 数据效率, 语言模型, 矩阵结构, 随机优化

## 3 点简述
- 核心问题：Shampoo和Muon等矩阵结构优化器与Adam等逐元素算法的关系及数据效率在受控设置下不明确
- 方法要点：通过实验证明Shampoo比Muon具有更高标记效率，其更新可分解为适应Muon更新，且优势仅源于权重矩阵应用
- 实验或效果：在语言模型上广泛实验，Shampoo的更新在期望上是时间平均半正交的，避免基于方差适应和白化的解释缺陷

## 摘要（原文）

> Optimizers leveraging the matrix structure in neural networks, such as Shampoo and Muon, are more data-efficient than element-wise algorithms like Adam and Signum. While in specific settings, Shampoo and Muon reduce to spectral descent analogous to how Adam and Signum reduce to sign descent, their general relationship and relative data efficiency under controlled settings remain unclear. Through extensive experiments on language models, we demonstrate that Shampoo achieves higher token efficiency than Muon, mirroring Adam's advantage over Signum. We show that Shampoo's update applied to weight matrices can be decomposed into an adapted Muon update. Consistent with this, Shampoo's benefits can be exclusively attributed to its application to weight matrices, challenging interpretations agnostic to parameter shapes. This admits a new perspective that also avoids shortcomings of related interpretations based on variance adaptation and whitening: rather than enforcing semi-orthogonality as in spectral descent, Shampoo's updates are time-averaged semi-orthogonal in expectation.

