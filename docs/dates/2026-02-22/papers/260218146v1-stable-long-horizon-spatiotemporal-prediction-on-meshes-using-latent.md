---
layout: default
title: Stable Long-Horizon Spatiotemporal Prediction on Meshes Using Latent Multiscale Recurrent Graph Neural Networks
---

# Stable Long-Horizon Spatiotemporal Prediction on Meshes Using Latent Multiscale Recurrent Graph Neural Networks
**arXiv**：[2602.18146v1](https://arxiv.org/abs/2602.18146) · [PDF](https://arxiv.org/pdf/2602.18146.pdf)  
**作者**：Lionel Salesses, Larbi Arbaoui, Tariq Benamara, Arnaud Francois, Caroline Sainvitu  

**一句话要点**：提出基于潜在多尺度循环图神经网络的框架，以解决复杂几何上长时域时空预测的稳定性问题

**关键词**：长时域预测, 图神经网络, 时空建模, 多尺度架构, 增材制造, 潜在表示

## 3 点简述
- 核心问题：复杂几何上长时域时空预测的准确性和稳定性挑战，如增材制造中的温度历史预测
- 方法要点：采用时间多尺度架构，结合潜在循环图神经网络和变分图自编码器，捕捉网格上的时空动态
- 实验或效果：在模拟粉末床融合数据上验证，实现准确且稳定的长时域预测，优于现有基线

## 摘要（原文）

> Accurate long-horizon prediction of spatiotemporal fields on complex geometries is a fundamental challenge in scientific machine learning, with applications such as additive manufacturing where temperature histories govern defect formation and mechanical properties. High-fidelity simulations are accurate but computationally costly, and despite recent advances, machine learning methods remain challenged by long-horizon temperature and gradient prediction. We propose a deep learning framework for predicting full temperature histories directly on meshes, conditioned on geometry and process parameters, while maintaining stability over thousands of time steps and generalizing across heterogeneous geometries. The framework adopts a temporal multiscale architecture composed of two coupled models operating at complementary time scales. Both models rely on a latent recurrent graph neural network to capture spatiotemporal dynamics on meshes, while a variational graph autoencoder provides a compact latent representation that reduces memory usage and improves training stability. Experiments on simulated powder bed fusion data demonstrate accurate and temporally stable long-horizon predictions across diverse geometries, outperforming existing baseline. Although evaluated in two dimensions, the framework is general and extensible to physics-driven systems with multiscale dynamics and to three-dimensional geometries.

