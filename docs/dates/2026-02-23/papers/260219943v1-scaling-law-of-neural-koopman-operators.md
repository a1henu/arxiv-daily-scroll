---
layout: default
title: Scaling Law of Neural Koopman Operators
---

# Scaling Law of Neural Koopman Operators
**arXiv**：[2602.19943v1](https://arxiv.org/abs/2602.19943) · [PDF](https://arxiv.org/pdf/2602.19943.pdf)  
**作者**：Abulikemu Abuduweili, Yuyang Pang, Feihan Li, Changliu Liu  

**一句话要点**：提出神经Koopman算子的缩放定律，以优化非线性机器人系统的数据驱动建模与控制。

**关键词**：神经Koopman算子, 缩放定律, 非线性系统控制, 数据驱动建模, 正则化方法, 机器人环境

## 3 点简述
- 核心问题：神经Koopman算子性能受样本量与模型维度权衡影响，缩放定律不明确。
- 方法要点：推导理论误差上界，分解为采样与投影误差，并引入协方差损失和逆控制损失正则化。
- 实验或效果：在六个机器人环境中验证缩放定律，正则化提升模型拟合与闭环控制性能。

## 摘要（原文）

> Data-driven neural Koopman operator theory has emerged as a powerful tool for linearizing and controlling nonlinear robotic systems. However, the performance of these data-driven models fundamentally depends on the trade-off between sample size and model dimensions, a relationship for which the scaling laws have remained unclear. This paper establishes a rigorous framework to address this challenge by deriving and empirically validating scaling laws that connect sample size, latent space dimension, and downstream control quality. We derive a theoretical upper bound on the Koopman approximation error, explicitly decomposing it into sampling error and projection error. We show that these terms decay at specific rates relative to dataset size and latent dimension, providing a rigorous basis for the scaling law. Based on the theoretical results, we introduce two lightweight regularizers for the neural Koopman operator: a covariance loss to help stabilize the learned latent features and an inverse control loss to ensure the model aligns with physical actuation. The results from systematic experiments across six robotic environments confirm that model fitting error follows the derived scaling laws, and the regularizers improve dynamic model fitting fidelity, with enhanced closed-loop control performance. Together, our results provide a simple recipe for allocating effort between data collection and model capacity when learning Koopman dynamics for control.

