---
layout: default
title: Multi-instance robust fitting for non-classical geometric models
---

# Multi-instance robust fitting for non-classical geometric models
**arXiv**：[2602.05602v1](https://arxiv.org/abs/2602.05602) · [PDF](https://arxiv.org/pdf/2602.05602.pdf)  
**作者**：Zongliang Zhang, Shuxiang Li, Xingwang Huang, Zongyue Wang  

**一句话要点**：提出基于模型-数据误差的估计器与元启发式优化器，以解决非经典几何模型的多实例鲁棒拟合问题。

**关键词**：非经典几何模型, 多实例拟合, 鲁棒估计, 元启发式优化, 模型-数据误差

## 3 点简述
- 核心问题：现有鲁棒拟合方法多针对经典模型，非经典模型多实例拟合研究较少。
- 方法要点：设计无预定义误差阈值的估计器处理异常值，结合元启发式算法优化非可微目标。
- 实验或效果：在多种非经典模型上验证有效性，代码已开源。

## 摘要（原文）

> Most existing robust fitting methods are designed for classical models, such as lines, circles, and planes. In contrast, fewer methods have been developed to robustly handle non-classical models, such as spiral curves, procedural character models, and free-form surfaces. Furthermore, existing methods primarily focus on reconstructing a single instance of a non-classical model. This paper aims to reconstruct multiple instances of non-classical models from noisy data. We formulate this multi-instance fitting task as an optimization problem, which comprises an estimator and an optimizer. Specifically, we propose a novel estimator based on the model-to-data error, capable of handling outliers without a predefined error threshold. Since the proposed estimator is non-differentiable with respect to the model parameters, we employ a meta-heuristic algorithm as the optimizer to seek the global optimum. The effectiveness of our method are demonstrated through experimental results on various non-classical models. The code is available at https://github.com/zhangzongliang/fitting.

