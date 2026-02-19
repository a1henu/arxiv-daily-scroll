---
layout: default
title: Knowledge-Embedded Latent Projection for Robust Representation Learning
---

# Knowledge-Embedded Latent Projection for Robust Representation Learning
**arXiv**：[2602.16709v1](https://arxiv.org/abs/2602.16709) · [PDF](https://arxiv.org/pdf/2602.16709.pdf)  
**作者**：Weijing Tang, Ming Yuan, Zongqi Xia, Tianxi Cai  

**一句话要点**：提出知识嵌入潜在投影模型，利用语义信息正则化表示学习以处理不平衡数据矩阵。

**关键词**：潜在空间模型, 表示学习, 知识嵌入, 核方法, 电子健康记录分析, 不平衡数据

## 3 点简述
- 核心问题：高维离散数据矩阵在维度不平衡时，潜在空间模型估计困难，如电子健康记录中患者少而特征多。
- 方法要点：通过再生核希尔伯特空间映射，将列嵌入建模为语义嵌入的平滑函数，结合核主成分分析和投影梯度下降进行高效估计。
- 实验或效果：理论分析误差界和局部收敛性，仿真和真实电子健康记录应用验证方法有效性。

## 摘要（原文）

> Latent space models are widely used for analyzing high-dimensional discrete data matrices, such as patient-feature matrices in electronic health records (EHRs), by capturing complex dependence structures through low-dimensional embeddings. However, estimation becomes challenging in the imbalanced regime, where one matrix dimension is much larger than the other. In EHR applications, cohort sizes are often limited by disease prevalence or data availability, whereas the feature space remains extremely large due to the breadth of medical coding system. Motivated by the increasing availability of external semantic embeddings, such as pre-trained embeddings of clinical concepts in EHRs, we propose a knowledge-embedded latent projection model that leverages semantic side information to regularize representation learning. Specifically, we model column embeddings as smooth functions of semantic embeddings via a mapping in a reproducing kernel Hilbert space. We develop a computationally efficient two-step estimation procedure that combines semantically guided subspace construction via kernel principal component analysis with scalable projected gradient descent. We establish estimation error bounds that characterize the trade-off between statistical error and approximation error induced by the kernel projection. Furthermore, we provide local convergence guarantees for our non-convex optimization procedure. Extensive simulation studies and a real-world EHR application demonstrate the effectiveness of the proposed method.

