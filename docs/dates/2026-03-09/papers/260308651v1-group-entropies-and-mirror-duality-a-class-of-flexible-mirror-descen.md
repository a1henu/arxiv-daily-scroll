---
layout: default
title: Group Entropies and Mirror Duality: A Class of Flexible Mirror Descent Updates for Machine Learning
---

# Group Entropies and Mirror Duality: A Class of Flexible Mirror Descent Updates for Machine Learning
**arXiv**：[2603.08651v1](https://arxiv.org/abs/2603.08651) · [PDF](https://arxiv.org/pdf/2603.08651.pdf)  
**作者**：Andrzej Cichocki, Piergiulio Tempesta  

**一句话要点**：提出基于群熵与镜像对偶的灵活镜像下降更新框架，用于机器学习优化

**关键词**：群熵理论, 镜像下降, 优化算法, 机器学习, 统计分布适应

## 3 点简述
- 核心问题：传统镜像下降算法在适应不同数据几何和统计分布时灵活性有限
- 方法要点：利用群熵理论构建多参数镜像映射，通过镜像对偶实现函数与逆函数的互换
- 实验或效果：在大规模单纯形约束二次规划问题上验证了更新方法的有效性和鲁棒性

## 摘要（原文）

> We introduce a comprehensive theoretical and algorithmic framework that bridges formal group theory and group entropies with modern machine learning, paving the way for an infinite, flexible family of Mirror Descent (MD) optimization algorithms. Our approach exploits the rich structure of group entropies, which are generalized entropic functionals governed by group composition laws, encompassing and significantly extending all trace-form entropies such as the Shannon, Tsallis, and Kaniadakis families. By leveraging group-theoretical mirror maps (or link functions) in MD, expressed via multi-parametric generalized logarithms and their inverses (group exponentials), we achieve highly flexible and adaptable MD updates that can be tailored to diverse data geometries and statistical distributions. To this end, we introduce the notion of \textit{mirror duality}, which allows us to seamlessly switch or interchange group-theoretical link functions with their inverses, subject to specific learning rate constraints. By tuning or learning the hyperparameters of the group logarithms enables us to adapt the model to the statistical properties of the training distribution, while simultaneously ensuring desirable convergence characteristics via fine-tuning. This generality not only provides greater flexibility and improved convergence properties, but also opens new perspectives for applications in machine learning and deep learning by expanding the design of regularizers and natural gradient algorithms. We extensively evaluate the validity, robustness, and performance of the proposed updates on large-scale, simplex-constrained quadratic programming problems.

