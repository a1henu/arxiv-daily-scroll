---
layout: default
title: Particle-Guided Diffusion Models for Partial Differential Equations
---

# Particle-Guided Diffusion Models for Partial Differential Equations
**arXiv**：[2601.23262v1](https://arxiv.org/abs/2601.23262) · [PDF](https://arxiv.org/pdf/2601.23262.pdf)  
**作者**：Andrew Millard, Fredrik Lindsten, Zheng Zhao  

**一句话要点**：提出基于粒子引导的扩散模型，以增强偏微分方程求解的物理约束生成能力。

**关键词**：扩散模型, 偏微分方程求解, 物理引导采样, 顺序蒙特卡洛, 生成模型

## 3 点简述
- 核心问题：扩散模型生成样本时缺乏物理约束，导致偏微分方程求解不准确。
- 方法要点：引入基于偏微分方程残差和观测约束的物理引导采样，结合顺序蒙特卡洛框架。
- 实验或效果：在多个基准和复杂偏微分方程系统中，生成解场的数值误差低于现有生成方法。

## 摘要（原文）

> We introduce a guided stochastic sampling method that augments sampling from diffusion models with physics-based guidance derived from partial differential equation (PDE) residuals and observational constraints, ensuring generated samples remain physically admissible. We embed this sampling procedure within a new Sequential Monte Carlo (SMC) framework, yielding a scalable generative PDE solver. Across multiple benchmark PDE systems as well as multiphysics and interacting PDE systems, our method produces solution fields with lower numerical error than existing state-of-the-art generative methods.

