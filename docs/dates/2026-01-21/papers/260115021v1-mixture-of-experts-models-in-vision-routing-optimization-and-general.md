---
layout: default
title: Mixture-of-Experts Models in Vision: Routing, Optimization, and Generalization
---

# Mixture-of-Experts Models in Vision: Routing, Optimization, and Generalization
**arXiv**：[2601.15021v1](https://arxiv.org/abs/2601.15021) · [PDF](https://arxiv.org/pdf/2601.15021.pdf)  
**作者**：Adam Rokah, Daniel Veress, Caleb Caulk, Sourav Sharan  

**一句话要点**：研究视觉中混合专家模型的路由、优化与泛化行为，在CIFAR10上比较不同变体

**关键词**：混合专家模型, 图像分类, 路由优化, 泛化分析, CIFAR10数据集, 条件计算

## 3 点简述
- 核心问题：探索MoE在图像分类中的性能、专家利用和泛化特性，而非语言模型扩展
- 方法要点：在可比模型容量下，比较密集、SoftMoE和SparseMoE分类头，使用正则化避免专家崩溃
- 实验或效果：MoE变体验证精度略高于密集基线，泛化分析显示SoftMoE曲率更高，但条件路由未实现推理加速

## 摘要（原文）

> Mixture-of-Experts (MoE) architectures enable conditional computation by routing inputs to multiple expert subnetworks and are often motivated as a mechanism for scaling large language models. In this project, we instead study MoE behavior in an image classification setting, focusing on predictive performance, expert utilization, and generalization. We compare dense, SoftMoE, and SparseMoE classifier heads on the CIFAR10 dataset under comparable model capacity. Both MoE variants achieve slightly higher validation accuracy than the dense baseline while maintaining balanced expert utilization through regularization, avoiding expert collapse. To analyze generalization, we compute Hessian-based sharpness metrics at convergence, including the largest eigenvalue and trace of the loss Hessian, evaluated on both training and test data. We find that SoftMoE exhibits higher sharpness by these metrics, while Dense and SparseMoE lie in a similar curvature regime, despite all models achieving comparable generalization performance. Complementary loss surface perturbation analyses reveal qualitative differences in non-local behavior under finite parameter perturbations between dense and MoE models, which help contextualize curvature-based measurements without directly explaining validation accuracy. We further evaluate empirical inference efficiency and show that naively implemented conditional routing does not yield inference speedups on modern hardware at this scale, highlighting the gap between theoretical and realized efficiency in sparse MoE models.

