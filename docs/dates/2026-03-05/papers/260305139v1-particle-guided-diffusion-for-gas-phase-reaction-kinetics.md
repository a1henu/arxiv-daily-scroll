---
layout: default
title: Particle-Guided Diffusion for Gas-Phase Reaction Kinetics
---

# Particle-Guided Diffusion for Gas-Phase Reaction Kinetics
**arXiv**：[2603.05139v1](https://arxiv.org/abs/2603.05139) · [PDF](https://arxiv.org/pdf/2603.05139.pdf)  
**作者**：Andrew Millard, Henrik Pedersen  

**一句话要点**：提出粒子引导扩散方法以解决气相化学反应动力学中的物理一致性预测问题

**关键词**：扩散模型, 气相反应动力学, 物理引导采样, 平流-反应-扩散方程, 浓度场预测

## 3 点简述
- 核心问题：物理引导采样在化学反应-传输系统中的应用有限，需生成物理一致的浓度场
- 方法要点：基于平流-反应-扩散方程训练扩散模型，通过引导采样生成浓度场
- 实验或效果：方法能准确预测出口浓度，包括未见参数值，展示扩散模型在反应传输推断中的潜力

## 摘要（原文）

> Physics-guided sampling with diffusion model priors has shown promise for solving partial differential equation (PDE) governed problems, but applications to chemically meaningful reaction-transport systems remain limited. We apply diffusion-based guided sampling to gas-phase chemical reactions by training on solutions of the advection-reaction-diffusion (ARD) equation across varying parameters. The method generates physically consistent concentration fields and accurately predicts outlet concentrations, including at unseen parameter values, demonstrating the potential of diffusion models for inference in reactive transport.

