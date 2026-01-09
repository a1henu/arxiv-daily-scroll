---
layout: default
title: Approximate equivariance via projection-based regularisation
---

# Approximate equivariance via projection-based regularisation
**arXiv**：[2601.05028v1](https://arxiv.org/abs/2601.05028) · [PDF](https://arxiv.org/pdf/2601.05028.pdf)  
**作者**：Torben Berndt, Jan Stühmer  

**一句话要点**：提出基于投影的正则化方法以实现近似等变性，平衡对称性与数据拟合。

**关键词**：近似等变性, 投影正则化, 连续群, 算子层面惩罚, 正交分解

## 3 点简述
- 核心问题：现有近似等变性方法依赖数据增强，样本复杂度高，尤其对连续群如SO(3)。
- 方法要点：利用线性层的正交分解，在算子层面惩罚非等变性，而非逐点方式。
- 实验或效果：在模型性能和效率上优于先前方法，显著提升运行速度。

## 摘要（原文）

> Equivariance is a powerful inductive bias in neural networks, improving generalisation and physical consistency. Recently, however, non-equivariant models have regained attention, due to their better runtime performance and imperfect symmetries that might arise in real-world applications. This has motivated the development of approximately equivariant models that strike a middle ground between respecting symmetries and fitting the data distribution. Existing approaches in this field usually apply sample-based regularisers which depend on data augmentation at training time, incurring a high sample complexity, in particular for continuous groups such as $SO(3)$. This work instead approaches approximate equivariance via a projection-based regulariser which leverages the orthogonal decomposition of linear layers into equivariant and non-equivariant components. In contrast to existing methods, this penalises non-equivariance at an operator level across the full group orbit, rather than point-wise. We present a mathematical framework for computing the non-equivariance penalty exactly and efficiently in both the spatial and spectral domain. In our experiments, our method consistently outperforms prior approximate equivariance approaches in both model performance and efficiency, achieving substantial runtime gains over sample-based regularisers.

