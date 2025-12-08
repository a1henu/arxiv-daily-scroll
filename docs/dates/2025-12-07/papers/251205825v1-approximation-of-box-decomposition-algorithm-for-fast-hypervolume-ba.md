---
layout: default
title: Approximation of Box Decomposition Algorithm for Fast Hypervolume-Based Multi-Objective Optimization
---

# Approximation of Box Decomposition Algorithm for Fast Hypervolume-Based Multi-Objective Optimization
**arXiv**：[2512.05825v1](https://arxiv.org/abs/2512.05825) · [PDF](https://arxiv.org/pdf/2512.05825.pdf)  
**作者**：Shuhei Watanabe  

**一句话要点**：提出超体积盒分解近似算法以加速多目标贝叶斯优化

**关键词**：超体积优化, 多目标贝叶斯优化, 盒分解算法, 近似算法, 计算复杂度

## 3 点简述
- 核心问题：超体积改进计算成本高，盒分解算法存在超多项式内存复杂度瓶颈
- 方法要点：提供近似算法的详细数学和算法描述，填补文献空白
- 实验或效果：未知

## 摘要（原文）

> Hypervolume (HV)-based Bayesian optimization (BO) is one of the standard approaches for multi-objective decision-making. However, the computational cost of optimizing the acquisition function remains a significant bottleneck, primarily due to the expense of HV improvement calculations. While HV box-decomposition offers an efficient way to cope with the frequent exact improvement calculations, it suffers from super-polynomial memory complexity $O(MN^{\lfloor \frac{M + 1}{2} \rfloor})$ in the worst case as proposed by Lacour et al. (2017). To tackle this problem, Couckuyt et al. (2012) employed an approximation algorithm. However, a rigorous algorithmic description is currently absent from the literature. This paper bridges this gap by providing comprehensive mathematical and algorithmic details of this approximation algorithm.

