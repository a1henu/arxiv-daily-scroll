---
layout: default
title: Efficient Differentiable Causal Discovery via Reliable Super-Structure Learning
---

# Efficient Differentiable Causal Discovery via Reliable Super-Structure Learning
**arXiv**：[2601.05474v1](https://arxiv.org/abs/2601.05474) · [PDF](https://arxiv.org/pdf/2601.05474.pdf)  
**作者**：Pingchuan Ma, Qixin Zhang, Shuai Wang, Dacheng Tao  

**一句话要点**：提出ALVGL方法，通过可靠超结构学习提升可微分因果发现的效率与准确性

**关键词**：可微分因果发现, 超结构学习, 稀疏低秩分解, ADMM优化, 因果图推断

## 3 点简述
- 核心问题：高维或含隐混淆变量数据中，可微分因果发现面临搜索空间大、目标函数复杂和约束难处理等挑战
- 方法要点：采用稀疏低秩分解学习精度矩阵，通过ADMM优化构建超结构，初始化标准方法以缩小搜索空间
- 实验或效果：在合成和真实数据集上验证，ALVGL在多种因果模型中实现高精度并显著提升优化效率

## 摘要（原文）

> Recently, differentiable causal discovery has emerged as a promising approach to improve the accuracy and efficiency of existing methods. However, when applied to high-dimensional data or data with latent confounders, these methods, often based on off-the-shelf continuous optimization algorithms, struggle with the vast search space, the complexity of the objective function, and the nontrivial nature of graph-theoretical constraints. As a result, there has been a surge of interest in leveraging super-structures to guide the optimization process. Nonetheless, learning an appropriate super-structure at the right level of granularity, and doing so efficiently across various settings, presents significant challenges.
>   In this paper, we propose ALVGL, a novel and general enhancement to the differentiable causal discovery pipeline. ALVGL employs a sparse and low-rank decomposition to learn the precision matrix of the data. We design an ADMM procedure to optimize this decomposition, identifying components in the precision matrix that are most relevant to the underlying causal structure. These components are then combined to construct a super-structure that is provably a superset of the true causal graph. This super-structure is used to initialize a standard differentiable causal discovery method with a more focused search space, thereby improving both optimization efficiency and accuracy.
>   We demonstrate the versatility of ALVGL by instantiating it across a range of structural causal models, including both Gaussian and non-Gaussian settings, with and without unmeasured confounders. Extensive experiments on synthetic and real-world datasets show that ALVGL not only achieves state-of-the-art accuracy but also significantly improves optimization efficiency, making it a reliable and effective solution for differentiable causal discovery.

