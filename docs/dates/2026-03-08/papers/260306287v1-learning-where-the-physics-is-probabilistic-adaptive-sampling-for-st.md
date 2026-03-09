---
layout: default
title: Learning Where the Physics Is: Probabilistic Adaptive Sampling for Stiff PDEs
---

# Learning Where the Physics Is: Probabilistic Adaptive Sampling for Stiff PDEs
**arXiv**：[2603.06287v1](https://arxiv.org/abs/2603.06287) · [PDF](https://arxiv.org/pdf/2603.06287.pdf)  
**作者**：Akshay Govind Srinivasan, Balaji Srinivasan  

**一句话要点**：提出GMM-PIELM以解决刚性偏微分方程建模中物理位置未知的采样问题

**关键词**：科学机器学习, 偏微分方程求解, 自适应采样, 高斯混合模型, 极端学习机, 边界层解析

## 3 点简述
- 核心问题：PINNs存在谱偏差和训练慢，PIELMs因随机初始化无法自适应捕捉物理位置。
- 方法要点：使用高斯混合模型和加权EM算法，自适应采样径向基函数中心于高误差区域。
- 实验或效果：在1D对流扩散方程上，L2误差比基线低7个数量级，保持ELM速度优势。

## 摘要（原文）

> Modeling stiff partial differential equations (PDEs) with sharp gradients remains a significant challenge for scientific machine learning. While Physics-Informed Neural Networks (PINNs) struggle with spectral bias and slow training times, Physics-Informed Extreme Learning Machines (PIELMs) offer a rapid, closed-form linear solution but are fundamentally limited by physics-agnostic, random initialization. We introduce the Gaussian Mixture Model Adaptive PIELM (GMM-PIELM), a probabilistic framework that learns a probability density function representing the ``location of physics'' for adaptively sampling kernels of PIELMs. By employing a weighted Expectation-Maximization (EM) algorithm, GMM-PIELM autonomously concentrates radial basis function centers in regions of high numerical error, such as shock fronts and boundary layers. This approach dynamically improves the conditioning of the hidden layer without the expensive gradient-based optimization(of PINNs) or Bayesian search. We evaluate our methodology on 1D singularly perturbed convection-diffusion equations with diffusion coefficients $ν=10^{-4}$. Our method achieves $L_2$ errors up to $7$ orders of magnitude lower than baseline RBF-PIELMs, successfully resolving exponentially thin boundary layers while retaining the orders-of-magnitude speed advantage of the ELM architecture.

