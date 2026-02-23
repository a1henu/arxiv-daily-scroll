---
layout: default
title: Assigning Confidence: K-partition Ensembles
---

# Assigning Confidence: K-partition Ensembles
**arXiv**：[2602.18435v1](https://arxiv.org/abs/2602.18435) · [PDF](https://arxiv.org/pdf/2602.18435.pdf)  
**作者**：Aggelos Semoglou, John Pavlopoulos  

**一句话要点**：提出CAKE框架以解决聚类中个体分配置信度量化问题

**关键词**：聚类集成, 置信度评估, 分配稳定性, 几何拟合, 无监督学习

## 3 点简述
- 核心问题：聚类算法缺乏对个体分配可靠性的评估，影响准确性和鲁棒性
- 方法要点：通过聚类集成计算分配稳定性和局部几何拟合一致性，结合为可解释置信度分数
- 实验或效果：在合成和真实数据集上有效识别模糊点和稳定核心成员，提升聚类质量

## 摘要（原文）

> Clustering is widely used for unsupervised structure discovery, yet it offers limited insight into how reliable each individual assignment is. Diagnostics, such as convergence behavior or objective values, may reflect global quality, but they do not indicate whether particular instances are assigned confidently, especially for initialization-sensitive algorithms like k-means. This assignment-level instability can undermine both accuracy and robustness. Ensemble approaches improve global consistency by aggregating multiple runs, but they typically lack tools for quantifying pointwise confidence in a way that combines cross-run agreement with geometric support from the learned cluster structure. We introduce CAKE (Confidence in Assignments via K-partition Ensembles), a framework that evaluates each point using two complementary statistics computed over a clustering ensemble: assignment stability and consistency of local geometric fit. These are combined into a single, interpretable score in [0,1]. Our theoretical analysis shows that CAKE remains effective under noise and separates stable from unstable points. Experiments on synthetic and real-world datasets indicate that CAKE effectively highlights ambiguous points and stable core members, providing a confidence ranking that can guide filtering or prioritization to improve clustering quality.

