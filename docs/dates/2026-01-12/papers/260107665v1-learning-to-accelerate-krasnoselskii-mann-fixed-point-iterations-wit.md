---
layout: default
title: Learning to accelerate Krasnosel'skii-Mann fixed-point iterations with guarantees
---

# Learning to accelerate Krasnosel'skii-Mann fixed-point iterations with guarantees
**arXiv**：[2601.07665v1](https://arxiv.org/abs/2601.07665) · [PDF](https://arxiv.org/pdf/2601.07665.pdf)  
**作者**：Andrea Martin, Giuseppe Belgioioso  

**一句话要点**：提出学习优化框架以加速Krasnosel'skii-Mann不动点迭代，保留收敛保证

**关键词**：不动点迭代, 学习优化, 算子分裂, 收敛保证, 度量次正则性, Douglas-Rachford分裂

## 3 点简述
- 针对非扩张映射的不动点问题，引入学习优化框架
- 通过可求和扰动改进标准迭代的平均性能，保持收敛性
- 在度量次正则性下证明局部线性收敛，并应用于算子分裂方法

## 摘要（原文）

> We introduce a principled learning to optimize (L2O) framework for solving fixed-point problems involving general nonexpansive mappings. Our idea is to deliberately inject summable perturbations into a standard Krasnosel'skii-Mann iteration to improve its average-case performance over a specific distribution of problems while retaining its convergence guarantees. Under a metric sub-regularity assumption, we prove that the proposed parametrization includes only iterations that locally achieve linear convergence-up to a vanishing bias term-and that it encompasses all iterations that do so at a sufficiently fast rate. We then demonstrate how our framework can be used to augment several widely-used operator splitting methods to accelerate the solution of structured monotone inclusion problems, and validate our approach on a best approximation problem using an L2O-augmented Douglas-Rachford splitting algorithm.

