---
layout: default
title: FairFS: Addressing Deep Feature Selection Biases for Recommender System
---

# FairFS: Addressing Deep Feature Selection Biases for Recommender System
**arXiv**：[2602.20001v1](https://arxiv.org/abs/2602.20001) · [PDF](https://arxiv.org/pdf/2602.20001.pdf)  
**作者**：Xianquan Wang, Zhaocheng Du, Jieming Zhu, Qinglin Jia, Zhenhua Dong, Kai Zhang  

**一句话要点**：提出FairFS算法以解决推荐系统中深度特征选择的三种偏差问题

**关键词**：推荐系统, 特征选择, 深度学习, 偏差缓解, 工业应用

## 3 点简述
- 核心问题：特征重要性估计存在层偏差、基线偏差和近似偏差，导致估计不准确
- 方法要点：通过正则化所有非线性层、引入平滑基线特征和聚合近似方法缓解偏差
- 实验或效果：实验表明FairFS有效减轻偏差，实现先进的特征选择性能

## 摘要（原文）

> Large-scale online marketplaces and recommender systems serve as critical technological support for e-commerce development. In industrial recommender systems, features play vital roles as they carry information for downstream models. Accurate feature importance estimation is critical because it helps identify the most useful feature subsets from thousands of feature candidates for online services. Such selection enables improved online performance while reducing computational cost. To address feature selection problems in deep learning, trainable gate-based and sensitivity-based methods have been proposed and proven effective in industrial practice. However, through the analysis of real-world cases, we identified three bias issues that cause feature importance estimation to rely on partial model layers, samples, or gradients, ultimately leading to inaccurate importance estimation. We refer to these as layer bias, baseline bias, and approximation bias. To mitigate these issues, we propose FairFS, a fair and accurate feature selection algorithm. FairFS regularizes feature importance estimated across all nonlinear transformation layers to address layer bias. It also introduces a smooth baseline feature close to the classifier decision boundary and adopts an aggregated approximation method to alleviate baseline and approximation biases. Extensive experiments demonstrate that FairFS effectively mitigates these biases and achieves state-of-the-art feature selection performance.

