---
layout: default
title: Inverting Data Transformations via Diffusion Sampling
---

# Inverting Data Transformations via Diffusion Sampling
**arXiv**：[2602.08267v1](https://arxiv.org/abs/2602.08267) · [PDF](https://arxiv.org/pdf/2602.08267.pdf)  
**作者**：Jinwoo Kim, Sékou-Oumar Kaba, Jiyun Park, Seunghoon Hong, Siamak Ravanbakhsh  

**一句话要点**：提出TIED方法，通过李群扩散采样解决未知变换反演问题，提升测试时等变性。

**关键词**：变换反演, 李群扩散, 测试时等变性, 能量函数采样, 数据分布恢复, 未知变换建模

## 3 点简述
- 研究李群上未知变换反演问题，旨在恢复数据到原始分布。
- 引入李群扩散过程，基于能量函数后验采样，利用平凡化目标-得分恒等式。
- 实验验证在图像单应性和PDE对称性中，TIED能有效恢复变换输入，优于基线方法。

## 摘要（原文）

> We study the problem of transformation inversion on general Lie groups: a datum is transformed by an unknown group element, and the goal is to recover an inverse transformation that maps it back to the original data distribution. Such unknown transformations arise widely in machine learning and scientific modeling, where they can significantly distort observations. We take a probabilistic view and model the posterior over transformations as a Boltzmann distribution defined by an energy function on data space. To sample from this posterior, we introduce a diffusion process on Lie groups that keeps all updates on-manifold and only requires computations in the associated Lie algebra. Our method, Transformation-Inverting Energy Diffusion (TIED), relies on a new trivialized target-score identity that enables efficient score-based sampling of the transformation posterior. As a key application, we focus on test-time equivariance, where the objective is to improve the robustness of pretrained neural networks to input transformations. Experiments on image homographies and PDE symmetries demonstrate that TIED can restore transformed inputs to the training distribution at test time, showing improved performance over strong canonicalization and sampling baselines. Code is available at https://github.com/jw9730/tied.

