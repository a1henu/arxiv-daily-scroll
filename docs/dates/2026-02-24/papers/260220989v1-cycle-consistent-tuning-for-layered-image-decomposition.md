---
layout: default
title: Cycle-Consistent Tuning for Layered Image Decomposition
---

# Cycle-Consistent Tuning for Layered Image Decomposition
**arXiv**：[2602.20989v1](https://arxiv.org/abs/2602.20989) · [PDF](https://arxiv.org/pdf/2602.20989.pdf)  
**作者**：Zheng Gu, Min Lu, Zhida Sun, Dani Lischinski, Daniel Cohen-O, Hui Huang  

**一句话要点**：提出循环一致性调优框架，基于扩散模型解决logo-物体图像分层分解问题。

**关键词**：图像分层分解, 扩散模型, 循环一致性调优, LoRA微调, logo-物体分解

## 3 点简述
- 核心问题：真实图像中视觉层（如logo与表面）的非线性全局耦合交互导致分层分解困难。
- 方法要点：通过轻量LoRA微调扩散模型，引入循环一致性策略联合训练分解与合成模型，增强鲁棒性。
- 实验或效果：实验显示方法能实现准确分解，并泛化至其他分解类型，具有统一框架潜力。

## 摘要（原文）

> Disentangling visual layers in real-world images is a persistent challenge in vision and graphics, as such layers often involve non-linear and globally coupled interactions, including shading, reflection, and perspective distortion. In this work, we present an in-context image decomposition framework that leverages large diffusion foundation models for layered separation. We focus on the challenging case of logo-object decomposition, where the goal is to disentangle a logo from the surface on which it appears while faithfully preserving both layers. Our method fine-tunes a pretrained diffusion model via lightweight LoRA adaptation and introduces a cycle-consistent tuning strategy that jointly trains decomposition and composition models, enforcing reconstruction consistency between decomposed and recomposed images. This bidirectional supervision substantially enhances robustness in cases where the layers exhibit complex interactions. Furthermore, we introduce a progressive self-improving process, which iteratively augments the training set with high-quality model-generated examples to refine performance. Extensive experiments demonstrate that our approach achieves accurate and coherent decompositions and also generalizes effectively across other decomposition types, suggesting its potential as a unified framework for layered image decomposition.

