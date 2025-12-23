---
layout: default
title: Cluster-Based Generalized Additive Models Informed by Random Fourier Features
---

# Cluster-Based Generalized Additive Models Informed by Random Fourier Features
**arXiv**：[2512.19373v1](https://arxiv.org/abs/2512.19373) · [PDF](https://arxiv.org/pdf/2512.19373.pdf)  
**作者**：Xin Huang, Jia Li, Jun Yu  

**一句话要点**：提出基于随机傅里叶特征和聚类的广义可加模型混合框架，以提升可解释机器学习性能

**关键词**：可解释机器学习, 广义可加模型, 随机傅里叶特征, 软聚类, 表示学习, 回归分析

## 3 点简述
- 核心问题：黑盒模型如深度神经网络预测准确但难以解释，需平衡准确性与透明度
- 方法要点：利用随机傅里叶特征嵌入进行软聚类，构建局部广义可加模型捕获非线性效应
- 实验或效果：在真实回归基准数据集上，相比经典可解释模型，预测性能有所提升

## 摘要（原文）

> Explainable machine learning aims to strike a balance between prediction accuracy and model transparency, particularly in settings where black-box predictive models, such as deep neural networks or kernel-based methods, achieve strong empirical performance but remain difficult to interpret. This work introduces a mixture of generalized additive models (GAMs) in which random Fourier feature (RFF) representations are leveraged to uncover locally adaptive structure in the data. In the proposed method, an RFF-based embedding is first learned and then compressed via principal component analysis. The resulting low-dimensional representations are used to perform soft clustering of the data through a Gaussian mixture model. These cluster assignments are then applied to construct a mixture-of-GAMs framework, where each local GAM captures nonlinear effects through interpretable univariate smooth functions. Numerical experiments on real-world regression benchmarks, including the California Housing, NASA Airfoil Self-Noise, and Bike Sharing datasets, demonstrate improved predictive performance relative to classical interpretable models. Overall, this construction provides a principled approach for integrating representation learning with transparent statistical modeling.

