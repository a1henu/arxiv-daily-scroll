---
layout: default
title: Rethinking Graph Generalization through the Lens of Sharpness-Aware Minimization
---

# Rethinking Graph Generalization through the Lens of Sharpness-Aware Minimization
**arXiv**：[2602.08855v1](https://arxiv.org/abs/2602.08855) · [PDF](https://arxiv.org/pdf/2602.08855.pdf)  
**作者**：Yang Qiu, Yixiong Zou, Jun Wang  

**一句话要点**：提出能量驱动生成增强框架E2A，通过能量引导潜在扰动增强图神经网络分布外泛化能力。

**关键词**：图神经网络, 分布外泛化, 锐度感知最小化, 能量驱动增强, 局部鲁棒半径, 最小偏移翻转

## 3 点简述
- 核心问题：图神经网络对分布偏移敏感，存在最小偏移翻转现象，测试样本轻微偏离训练分布即被误分类。
- 方法要点：基于锐度感知最小化视角，引入局部鲁棒半径量化损失锐度，并开发能量驱动生成增强框架E2A生成伪分布外样本。
- 实验或效果：在多个基准测试中，E2A一致提升图分布外泛化性能，优于现有先进基线方法。

## 摘要（原文）

> Graph Neural Networks (GNNs) have achieved remarkable success across various graph-based tasks but remain highly sensitive to distribution shifts. In this work, we focus on a prevalent yet under-explored phenomenon in graph generalization, Minimal Shift Flip (MSF),where test samples that slightly deviate from the training distribution are abruptly misclassified. To interpret this phenomenon, we revisit MSF through the lens of Sharpness-Aware Minimization (SAM), which characterizes the local stability and sharpness of the loss landscape while providing a theoretical foundation for modeling generalization error. To quantify loss sharpness, we introduce the concept of Local Robust Radius, measuring the smallest perturbation required to flip a prediction and establishing a theoretical link between local stability and generalization. Building on this perspective, we further observe a continual decrease in the robust radius during training, indicating weakened local stability and an increasingly sharp loss landscape that gives rise to MSF. To jointly solve the MSF phenomenon and the intractability of radius, we develop an energy-based formulation that is theoretically proven to be monotonically correlated with the robust radius, offering a tractable and principled objective for modeling flatness and stability. Building on these insights, we propose an energy-driven generative augmentation framework (E2A) that leverages energy-guided latent perturbations to generate pseudo-OOD samples and enhance model generalization. Extensive experiments across multiple benchmarks demonstrate that E2A consistently improves graph OOD generalization, outperforming state-of-the-art baselines.

