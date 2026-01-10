---
layout: default
title: Gradient-based Optimisation of Modulation Effects
---

# Gradient-based Optimisation of Modulation Effects
**arXiv**：[2601.04867v1](https://arxiv.org/abs/2601.04867) · [PDF](https://arxiv.org/pdf/2601.04867.pdf)  
**作者**：Alistair Carson, Alec Wright, Stefan Bilbao  

**一句话要点**：提出基于可微分数字信号处理的调制效果建模框架，以解决模拟单元仿真中的延迟和计算成本问题。

**关键词**：可微分数字信号处理, 调制效果仿真, 梯度优化, 零延迟推理, 损失函数设计

## 3 点简述
- 核心问题：传统机器学习方法仿真模拟调制效果时，常受限于单一效果类型、高计算成本或延迟。
- 方法要点：采用可微分数字信号处理建模，在时频域训练，时域推理实现零延迟。
- 实验或效果：通过低频加权损失函数优化延迟时间，部分效果输出与参考感知无差异，但长延迟和反馈效果仍存挑战。

## 摘要（原文）

> Modulation effects such as phasers, flangers and chorus effects are heavily used in conjunction with the electric guitar. Machine learning based emulation of analog modulation units has been investigated in recent years, but most methods have either been limited to one class of effect or suffer from a high computational cost or latency compared to canonical digital implementations. Here, we build on previous work and present a framework for modelling flanger, chorus and phaser effects based on differentiable digital signal processing. The model is trained in the time-frequency domain, but at inference operates in the time-domain, requiring zero latency. We investigate the challenges associated with gradient-based optimisation of such effects, and show that low-frequency weighting of loss functions avoids convergence to local minima when learning delay times. We show that when trained against analog effects units, sound output from the model is in some cases perceptually indistinguishable from the reference, but challenges still remain for effects with long delay times and feedback.

