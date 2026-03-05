---
layout: default
title: Nearest-Neighbor Density Estimation for Dependency Suppression
---

# Nearest-Neighbor Density Estimation for Dependency Suppression
**arXiv**：[2603.04224v1](https://arxiv.org/abs/2603.04224) · [PDF](https://arxiv.org/pdf/2603.04224.pdf)  
**作者**：Kathleen Anderson, Thomas Martinetz  

**一句话要点**：提出基于最近邻密度估计的编码器方法，以消除数据中的敏感依赖，应用于公平性、鲁棒学习和隐私保护。

**关键词**：依赖抑制, 最近邻密度估计, 变分自编码器, 公平学习, 无监督表示学习, 隐私保护

## 3 点简述
- 核心问题：从数据中移除不希望的依赖，如敏感变量，同时保留关键数据特征。
- 方法要点：结合变分自编码器和最近邻密度估计损失，直接优化独立性，避免依赖去相关或对抗学习。
- 实验或效果：在多个数据集上评估，优于现有无监督方法，在信息移除与效用平衡上媲美有监督方法。

## 摘要（原文）

> The ability to remove unwanted dependencies from data is crucial in various domains, including fairness, robust learning, and privacy protection. In this work, we propose an encoder-based approach that learns a representation independent of a sensitive variable but otherwise preserving essential data characteristics. Unlike existing methods that rely on decorrelation or adversarial learning, our approach explicitly estimates and modifies the data distribution to neutralize statistical dependencies. To achieve this, we combine a specialized variational autoencoder with a novel loss function driven by non-parametric nearest-neighbor density estimation, enabling direct optimization of independence. We evaluate our approach on multiple datasets, demonstrating that it can outperform existing unsupervised techniques and even rival supervised methods in balancing information removal and utility.

