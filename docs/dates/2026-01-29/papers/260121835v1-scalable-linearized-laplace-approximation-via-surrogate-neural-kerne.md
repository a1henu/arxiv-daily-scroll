---
layout: default
title: Scalable Linearized Laplace Approximation via Surrogate Neural Kernel
---

# Scalable Linearized Laplace Approximation via Surrogate Neural Kernel
**arXiv**：[2601.21835v1](https://arxiv.org/abs/2601.21835) · [PDF](https://arxiv.org/pdf/2601.21835.pdf)  
**作者**：Luis A. Ortega, Simón Rodríguez-Santana, Daniel Hernández-Lobato  

**一句话要点**：提出基于代理神经核的可扩展线性化拉普拉斯近似方法，以高效计算预训练深度神经网络的预测不确定性。

**关键词**：线性化拉普拉斯近似, 神经正切核, 预测不确定性, 分布外检测, 深度神经网络, 可扩展方法

## 3 点简述
- 核心问题：线性化拉普拉斯近似（LLA）需计算大雅可比矩阵，在大规模预训练深度神经网络中计算成本高。
- 方法要点：使用代理深度神经网络学习紧凑特征表示，其内积复制神经正切核（NTK），避免直接计算雅可比矩阵，仅需高效雅可比-向量积。
- 实验或效果：在不确定性估计和校准方面与现有LLA近似方法相当或更优，且通过偏置学习核显著提升分布外检测性能。

## 摘要（原文）

> We introduce a scalable method to approximate the kernel of the Linearized Laplace Approximation (LLA). For this, we use a surrogate deep neural network (DNN) that learns a compact feature representation whose inner product replicates the Neural Tangent Kernel (NTK). This avoids the need to compute large Jacobians. Training relies solely on efficient Jacobian-vector products, allowing to compute predictive uncertainty on large-scale pre-trained DNNs. Experimental results show similar or improved uncertainty estimation and calibration compared to existing LLA approximations. Notwithstanding, biasing the learned kernel significantly enhances out-of-distribution detection. This remarks the benefits of the proposed method for finding better kernels than the NTK in the context of LLA to compute prediction uncertainty given a pre-trained DNN.

