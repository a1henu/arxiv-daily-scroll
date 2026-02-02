---
layout: default
title: Bayesian Interpolating Neural Network (B-INN): a scalable and reliable Bayesian model for large-scale physical systems
---

# Bayesian Interpolating Neural Network (B-INN): a scalable and reliable Bayesian model for large-scale physical systems
**arXiv**：[2601.22860v1](https://arxiv.org/abs/2601.22860) · [PDF](https://arxiv.org/pdf/2601.22860.pdf)  
**作者**：Chanwook Park, Brian Kim, Jiachen Guo, Wing Kam Liu  

**一句话要点**：提出贝叶斯插值神经网络以解决大规模物理系统中不确定性量化的可扩展性与可靠性问题

**关键词**：贝叶斯模型, 不确定性量化, 大规模物理系统, 主动学习, 张量分解, 插值理论

## 3 点简述
- 核心问题：神经网络和机器学习模型在大规模不确定性量化中可扩展性差、可靠性低，工业级主动学习场景下计算成本高
- 方法要点：结合高阶插值理论、张量分解和交替方向算法，实现高效降维且保持预测精度，贝叶斯推断复杂度为线性
- 实验或效果：数值实验显示比贝叶斯神经网络和高斯过程快20至10000倍，并提供稳健的不确定性估计

## 摘要（原文）

> Neural networks and machine learning models for uncertainty quantification suffer from limited scalability and poor reliability compared to their deterministic counterparts. In industry-scale active learning settings, where generating a single high-fidelity simulation may require days or weeks of computation and produce data volumes on the order of gigabytes, they quickly become impractical. This paper proposes a scalable and reliable Bayesian surrogate model, termed the Bayesian Interpolating Neural Network (B-INN). The B-INN combines high-order interpolation theory with tensor decomposition and alternating direction algorithm to enable effective dimensionality reduction without compromising predictive accuracy. We theoretically show that the function space of a B-INN is a subset of that of Gaussian processes, while its Bayesian inference exhibits linear complexity, $\mathcal{O}(N)$, with respect to the number of training samples. Numerical experiments demonstrate that B-INNs can be from 20 times to 10,000 times faster with a robust uncertainty estimation compared to Bayesian neural networks and Gaussian processes. These capabilities make B-INN a practical foundation for uncertainty-driven active learning in large-scale industrial simulations, where computational efficiency and robust uncertainty calibration are paramount.

