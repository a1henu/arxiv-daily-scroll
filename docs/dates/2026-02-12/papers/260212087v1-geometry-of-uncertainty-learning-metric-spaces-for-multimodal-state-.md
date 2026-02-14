---
layout: default
title: Geometry of Uncertainty: Learning Metric Spaces for Multimodal State Estimation in RL
---

# Geometry of Uncertainty: Learning Metric Spaces for Multimodal State Estimation in RL
**arXiv**：[2602.12087v1](https://arxiv.org/abs/2602.12087) · [PDF](https://arxiv.org/pdf/2602.12087.pdf)  
**作者**：Alfredo Reichlin, Adriano Pacciarelli, Danica Kragic, Miguel Vasco  

**一句话要点**：提出基于度量空间的多模态状态估计方法，以提升强化学习中的鲁棒性。

**关键词**：强化学习, 状态估计, 度量空间, 多模态融合, 鲁棒性, 潜在表示

## 3 点简述
- 核心问题：高维多模态噪声观测下的状态估计，传统概率模型依赖显式噪声假设限制泛化。
- 方法要点：学习结构化潜在表示，距离对应状态间最小动作数，无需显式概率建模，引入多模态潜在转移模型和逆距离加权传感器融合。
- 实验或效果：在多模态RL任务中验证，相比基线方法提升噪声鲁棒性和状态估计性能，增强RL代理表现。

## 摘要（原文）

> Estimating the state of an environment from high-dimensional, multimodal, and noisy observations is a fundamental challenge in reinforcement learning (RL). Traditional approaches rely on probabilistic models to account for the uncertainty, but often require explicit noise assumptions, in turn limiting generalization. In this work, we contribute a novel method to learn a structured latent representation, in which distances between states directly correlate with the minimum number of actions required to transition between them. The proposed metric space formulation provides a geometric interpretation of uncertainty without the need for explicit probabilistic modeling. To achieve this, we introduce a multimodal latent transition model and a sensor fusion mechanism based on inverse distance weighting, allowing for the adaptive integration of multiple sensor modalities without prior knowledge of noise distributions. We empirically validate the approach on a range of multimodal RL tasks, demonstrating improved robustness to sensor noise and superior state estimation compared to baseline methods. Our experiments show enhanced performance of an RL agent via the learned representation, eliminating the need of explicit noise augmentation. The presented results suggest that leveraging transition-aware metric spaces provides a principled and scalable solution for robust state estimation in sequential decision-making.

