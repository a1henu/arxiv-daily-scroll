---
layout: default
title: A Gaussian Comparison Theorem for Training Dynamics in Machine Learning
---

# A Gaussian Comparison Theorem for Training Dynamics in Machine Learning
**arXiv**：[2603.09310v1](https://arxiv.org/abs/2603.09310) · [PDF](https://arxiv.org/pdf/2603.09310.pdf)  
**作者**：Ashkan Panahi  

**一句话要点**：提出基于高斯比较定理的非渐近训练动态分析框架，适用于高斯混合数据下的机器学习算法。

**关键词**：高斯比较定理, 训练动态分析, 高斯混合模型, 动态平均场, 非渐近理论, 感知机训练

## 3 点简述
- 研究高斯混合数据下训练算法的动态行为，聚焦特定算法族。
- 利用Gordon比较定理，将模型演化连接至更易分析的代理动力系统。
- 在渐近场景中严格证明动态平均场表达，并建议非渐近场景的迭代细化方案。

## 摘要（原文）

> We study training algorithms with data following a Gaussian mixture model. For a specific family of such algorithms, we present a non-asymptotic result, connecting the evolution of the model to a surrogate dynamical system, which can be easier to analyze. The proof of our result is based on the celebrated Gordon comparison theorem. Using our theorem, we rigorously prove the validity of the dynamic mean-field (DMF) expressions in the asymptotic scenarios. Moreover, we suggest an iterative refinement scheme to obtain more accurate expressions in non-asymptotic scenarios. We specialize our theory to the analysis of training a perceptron model with a generic first-order (full-batch) algorithm and demonstrate that fluctuation parameters in a non-asymptotic domain emerge in addition to the DMF kernels.

