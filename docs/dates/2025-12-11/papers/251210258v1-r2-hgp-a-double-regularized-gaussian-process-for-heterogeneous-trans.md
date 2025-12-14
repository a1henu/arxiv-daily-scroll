---
layout: default
title: R^2-HGP: A Double-Regularized Gaussian Process for Heterogeneous Transfer Learning
---

# R^2-HGP: A Double-Regularized Gaussian Process for Heterogeneous Transfer Learning
**arXiv**：[2512.10258v1](https://arxiv.org/abs/2512.10258) · [PDF](https://arxiv.org/pdf/2512.10258.pdf)  
**作者**：Duo Wang, Xinming Wang, Chao Wang, Xiaowei Yue, Jianguo Wu  

**一句话要点**：提出双正则化高斯过程框架以解决异构输入和负迁移的转移学习问题

**关键词**：异构转移学习, 高斯过程, 条件变分自编码器, 正则化, 负迁移抑制, 多源知识共享

## 3 点简述
- 核心问题：异构输入空间和负迁移阻碍传统多输出高斯过程在转移学习中的应用
- 方法要点：通过可训练先验映射对齐输入，结合物理正则化和稀疏惩罚优化知识共享
- 实验或效果：模拟和工程案例验证了R^2-HGP在多种指标上优于现有基准

## 摘要（原文）

> Multi-output Gaussian process (MGP) models have attracted significant attention for their flexibility and uncertainty-quantification capabilities, and have been widely adopted in multi-source transfer learning scenarios due to their ability to capture inter-task correlations. However, they still face several challenges in transfer learning. First, the input spaces of the source and target domains are often heterogeneous, which makes direct knowledge transfer difficult. Second, potential prior knowledge and physical information are typically ignored during heterogeneous transfer, hampering the utilization of domain-specific insights and leading to unstable mappings. Third, inappropriate information sharing among target and sources can easily lead to negative transfer. Traditional models fail to address these issues in a unified way. To overcome these limitations, this paper proposes a Double-Regularized Heterogeneous Gaussian Process framework (R^2-HGP). Specifically, a trainable prior probability mapping model is first proposed to align the heterogeneous input domains. The resulting aligned inputs are treated as latent variables, upon which a multi-source transfer GP model is constructed and the entire structure is integrated into a novel conditional variational autoencoder (CVAE) based framework. Physical insights is further incorporated as a regularization term to ensure that the alignment results adhere to known physical knowledge. Next, within the multi-source transfer GP model, a sparsity penalty is imposed on the transfer coefficients, enabling the model to adaptively select the most informative source outputs and suppress negative transfer. Extensive simulations and real-world engineering case studies validate the effectiveness of our R^2-HGP, demonstrating consistent superiority over state-of-the-art benchmarks across diverse evaluation metrics.

