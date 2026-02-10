---
layout: default
title: Foundation Inference Models for Ordinary Differential Equations
---

# Foundation Inference Models for Ordinary Differential Equations
**arXiv**：[2602.08733v1](https://arxiv.org/abs/2602.08733) · [PDF](https://arxiv.org/pdf/2602.08733.pdf)  
**作者**：Maximilian Mauel, Johannes R. Hübers, David Berghaus, Patrick Seifner, Ramses J. Sanchez  

**一句话要点**：提出FIM-ODE基础推理模型，通过单次前向预测从噪声轨迹推断常微分方程向量场。

**关键词**：常微分方程推断, 基础推理模型, 神经算子, 零样本学习, 预训练模型

## 3 点简述
- 核心问题：从噪声轨迹推断常微分方程向量场，现有方法需复杂训练或强先验知识。
- 方法要点：预训练基础推理模型，基于低阶多项式向量场先验分布，使用神经算子直接预测。
- 实验或效果：零样本性能强，匹配或超越ODEFormer，预训练为微调提供快速稳定初始化。

## 摘要（原文）

> Ordinary differential equations (ODEs) are central to scientific modelling, but inferring their vector fields from noisy trajectories remains challenging. Current approaches such as symbolic regression, Gaussian process (GP) regression, and Neural ODEs often require complex training pipelines and substantial machine learning expertise, or they depend strongly on system-specific prior knowledge. We propose FIM-ODE, a pretrained Foundation Inference Model that amortises low-dimensional ODE inference by predicting the vector field directly from noisy trajectory data in a single forward pass. We pretrain FIM-ODE on a prior distribution over ODEs with low-degree polynomial vector fields and represent the target field with neural operators. FIM-ODE achieves strong zero-shot performance, matching and often improving upon ODEFormer, a recent pretrained symbolic baseline, across a range of regimes despite using a simpler pretraining prior distribution. Pretraining also provides a strong initialisation for finetuning, enabling fast and stable adaptation that outperforms modern neural and GP baselines without requiring machine learning expertise.

