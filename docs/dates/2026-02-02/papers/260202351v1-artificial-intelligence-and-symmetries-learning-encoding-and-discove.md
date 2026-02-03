---
layout: default
title: Artificial Intelligence and Symmetries: Learning, Encoding, and Discovering Structure in Physical Data
---

# Artificial Intelligence and Symmetries: Learning, Encoding, and Discovering Structure in Physical Data
**arXiv**：[2602.02351v1](https://arxiv.org/abs/2602.02351) · [PDF](https://arxiv.org/pdf/2602.02351.pdf)  
**作者**：Veronica Sanz  

**一句话要点**：综述机器学习在物理数据中识别、编码和诊断对称性结构的方法与局限

**关键词**：对称性学习, 表示学习, 变分自编码器, 物理数据, 潜在空间, 数据驱动方法

## 3 点简述
- 核心问题：对称性如何降低物理数据的内在维度，机器学习能否数据驱动地推断对称性约束
- 方法要点：聚焦变分自编码器等表示学习技术，分析潜在空间自组织以平衡重构与压缩
- 实验或效果：回顾几何系统和粒子物理案例，讨论无显式归纳偏置下推断对称性的理论实践限制

## 摘要（原文）

> Symmetries play a central role in physics, organizing dynamics, constraining interactions, and determining the effective number of physical degrees of freedom. In parallel, modern artificial intelligence methods have demonstrated a remarkable ability to extract low-dimensional structure from high-dimensional data through representation learning. This review examines the interplay between these two perspectives, focusing on the extent to which symmetry-induced constraints can be identified, encoded, or diagnosed using machine learning techniques.
>   Rather than emphasizing architectures that enforce known symmetries by construction, we concentrate on data-driven approaches and latent representation learning, with particular attention to variational autoencoders. We discuss how symmetries and conservation laws reduce the intrinsic dimensionality of physical datasets, and how this reduction may manifest itself through self-organization of latent spaces in generative models trained to balance reconstruction and compression. We review recent results, including case studies from simple geometric systems and particle physics processes, and analyze the theoretical and practical limitations of inferring symmetry structure without explicit inductive bias.

