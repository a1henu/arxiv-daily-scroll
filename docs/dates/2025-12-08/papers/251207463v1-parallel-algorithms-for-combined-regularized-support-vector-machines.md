---
layout: default
title: Parallel Algorithms for Combined Regularized Support Vector Machines: Application in Music Genre Classification
---

# Parallel Algorithms for Combined Regularized Support Vector Machines: Application in Music Genre Classification
**arXiv**：[2512.07463v1](https://arxiv.org/abs/2512.07463) · [PDF](https://arxiv.org/pdf/2512.07463.pdf)  
**作者**：Rongmei Liang, Zizheng Liu, Xiaofei Wu, Jingwen Tu  

**一句话要点**：提出基于共识结构的并行ADMM算法以解决分布式存储大数据中组合正则化支持向量机的计算效率问题

**关键词**：组合正则化支持向量机, 并行ADMM算法, 分布式计算, 音乐流派分类, 高斯回代法, 稀疏组套索支持向量机

## 3 点简述
- 核心问题：组合正则化支持向量机在分布式存储大数据中缺乏高效算法
- 方法要点：开发分布式并行ADMM算法，引入高斯回代法确保收敛，并扩展至非凸正则化
- 实验或效果：在合成和音乐档案数据集上验证算法的可靠性、稳定性和效率

## 摘要（原文）

> In the era of rapid development of artificial intelligence, its applications span across diverse fields, relying heavily on effective data processing and model optimization. Combined Regularized Support Vector Machines (CR-SVMs) can effectively handle the structural information among data features, but there is a lack of efficient algorithms in distributed-stored big data. To address this issue, we propose a unified optimization framework based on consensus structure. This framework is not only applicable to various loss functions and combined regularization terms but can also be effectively extended to non-convex regularization terms, showing strong scalability. Based on this framework, we develop a distributed parallel alternating direction method of multipliers (ADMM) algorithm to efficiently compute CR-SVMs when data is stored in a distributed manner. To ensure the convergence of the algorithm, we also introduce the Gaussian back-substitution method. Meanwhile, for the integrity of the paper, we introduce a new model, the sparse group lasso support vector machine (SGL-SVM), and apply it to music information retrieval. Theoretical analysis confirms that the computational complexity of the proposed algorithm is not affected by different regularization terms and loss functions, highlighting the universality of the parallel algorithm. Experiments on synthetic and free music archiv datasets demonstrate the reliability, stability, and efficiency of the algorithm.

