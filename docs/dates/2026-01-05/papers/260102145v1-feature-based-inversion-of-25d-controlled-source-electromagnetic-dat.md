---
layout: default
title: Feature-based Inversion of 2.5D Controlled Source Electromagnetic Data using Generative Priors
---

# Feature-based Inversion of 2.5D Controlled Source Electromagnetic Data using Generative Priors
**arXiv**：[2601.02145v1](https://arxiv.org/abs/2601.02145) · [PDF](https://arxiv.org/pdf/2601.02145.pdf)  
**作者**：Hongyu Zhou, Haoran Sun, Rui Guo, Maokun Li, Fan Yang, Shenheng Xu  

**一句话要点**：提出基于生成先验的特征反演方法，用于2.5D海洋可控源电磁数据反演

**关键词**：海洋可控源电磁反演, 生成先验, 变分自编码器, 高斯牛顿法, 特征反演

## 3 点简述
- 核心问题：传统黑盒神经网络反演缺乏对数据失配的显式控制和先验信息有效融入
- 方法要点：采用变分自编码器学习电导率分布先验，结合高斯牛顿法迭代更新模型
- 实验或效果：数值和现场实验验证方法能提高重建精度和泛化性能

## 摘要（原文）

> In this study, we investigate feature-based 2.5D controlled source marine electromagnetic (mCSEM) data inversion using generative priors. Two-and-half dimensional modeling using finite difference method (FDM) is adopted to compute the response of horizontal electric dipole (HED) excitation. Rather than using a neural network to approximate the entire inverse mapping in a black-box manner, we adopt a plug-andplay strategy in which a variational autoencoder (VAE) is used solely to learn prior information on conductivity distributions. During the inversion process, the conductivity model is iteratively updated using the Gauss Newton method, while the model space is constrained by projections onto the learned VAE decoder. This framework preserves explicit control over data misfit and enables flexible adaptation to different survey configurations. Numerical and field experiments demonstrate that the proposed approach effectively incorporates prior information, improves reconstruction accuracy, and exhibits good generalization performance.

