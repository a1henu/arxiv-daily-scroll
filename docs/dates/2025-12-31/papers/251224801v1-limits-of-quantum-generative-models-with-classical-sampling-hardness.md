---
layout: default
title: Limits of quantum generative models with classical sampling hardness
---

# Limits of quantum generative models with classical sampling hardness
**arXiv**：[2512.24801v1](https://arxiv.org/abs/2512.24801) · [PDF](https://arxiv.org/pdf/2512.24801.pdf)  
**作者**：Sabrina Herbst, Ivona Brandić, Adrián Pérez-Salinas  

**一句话要点**：揭示量子生成模型在经典采样困难分布上的训练限制与优势来源

**关键词**：量子生成模型, 采样任务, 反集中性, 经典可模拟性, 量子优势, 训练限制

## 3 点简述
- 核心问题：量子生成模型在输出反集中分布时平均不可训练，与量子优势关联
- 方法要点：分析输出分布特性，区分稀疏分布可训练，反集中分布不可训练
- 实验或效果：考虑特例提升可训练性，但可能引入经典替代采样算法路径

## 摘要（原文）

> Sampling tasks have been successful in establishing quantum advantages both in theory and experiments. This has fueled the use of quantum computers for generative modeling to create samples following the probability distribution underlying a given dataset. In particular, the potential to build generative models on classically hard distributions would immediately preclude classical simulability, due to theoretical separations. In this work, we study quantum generative models from the perspective of output distributions, showing that models that anticoncentrate are not trainable on average, including those exhibiting quantum advantage. In contrast, models outputting data from sparse distributions can be trained. We consider special cases to enhance trainability, and observe that this opens the path for classical algorithms for surrogate sampling. This observed trade-off is linked to verification of quantum processes. We conclude that quantum advantage can still be found in generative models, although its source must be distinct from anticoncentration.

