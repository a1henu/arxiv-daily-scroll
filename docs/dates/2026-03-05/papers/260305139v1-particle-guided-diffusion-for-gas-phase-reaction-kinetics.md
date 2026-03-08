---
layout: default
title: Particle-Guided Diffusion for Gas-Phase Reaction Kinetics
---

# Particle-Guided Diffusion for Gas-Phase Reaction Kinetics
**arXiv**：[2603.05139v1](https://arxiv.org/abs/2603.05139) · [PDF](https://arxiv.org/pdf/2603.05139.pdf)  
**作者**：Andrew Millard, Henrik Pedersen  

**一句话要点**：提出粒子引导扩散方法，用于气相反应动力学，以生成物理一致的浓度场并预测出口浓度。

**关键词**：扩散模型, 气相反应动力学, 物理引导采样, 对流-反应-扩散方程, 参数化推断

## 3 点简述
- 核心问题：物理引导采样在化学反应-传输系统中的应用有限，需解决气相反应动力学中的参数变化问题。
- 方法要点：基于扩散模型先验，训练对流-反应-扩散方程的解，实现参数化引导采样以生成浓度场。
- 实验或效果：方法在未见参数值下准确预测出口浓度，验证了扩散模型在反应传输推断中的潜力。

## 摘要（原文）

> Physics-guided sampling with diffusion model priors has shown promise for solving partial differential equation (PDE) governed problems, but applications to chemically meaningful reaction-transport systems remain limited. We apply diffusion-based guided sampling to gas-phase chemical reactions by training on solutions of the advection-reaction-diffusion (ARD) equation across varying parameters. The method generates physically consistent concentration fields and accurately predicts outlet concentrations, including at unseen parameter values, demonstrating the potential of diffusion models for inference in reactive transport.

