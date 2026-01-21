---
layout: default
title: Autoregressive deep learning for real-time simulation of soft tissue dynamics during virtual neurosurgery
---

# Autoregressive deep learning for real-time simulation of soft tissue dynamics during virtual neurosurgery
**arXiv**：[2601.13676v1](https://arxiv.org/abs/2601.13676) · [PDF](https://arxiv.org/pdf/2601.13676.pdf)  
**作者**：Fabian Greifeneder, Wolfgang Fenz, Benedikt Alkin, Johannes Brandstetter, Michael Giretzlehner, Philipp Moser  

**一句话要点**：提出基于自回归深度学习的脑组织动态模拟方法，用于虚拟神经外科实时仿真

**关键词**：脑组织变形模拟, 深度学习代理模型, 自回归推理, 随机教师强制, 实时仿真, 虚拟神经外科

## 3 点简述
- 核心问题：传统数值求解器难以满足脑组织非线性变形模拟的实时性要求
- 方法要点：基于通用物理变换器构建深度学习代理模型，采用随机教师强制策略减少误差累积
- 实验或效果：模型在15万节点网格上实现准确预测，单步仿真时间低于10毫秒，最大误差从6.7毫米降至3.5毫米

## 摘要（原文）

> Accurate simulation of brain deformation is a key component for developing realistic, interactive neurosurgical simulators, as complex nonlinear deformations must be captured to ensure realistic tool-tissue interactions. However, traditional numerical solvers often fall short in meeting real-time performance requirements. To overcome this, we introduce a deep learning-based surrogate model that efficiently simulates transient brain deformation caused by continuous interactions between surgical instruments and the virtual brain geometry. Building on Universal Physics Transformers, our approach operates directly on large-scale mesh data and is trained on an extensive dataset generated from nonlinear finite element simulations, covering a broad spectrum of temporal instrument-tissue interaction scenarios. To reduce the accumulation of errors in autoregressive inference, we propose a stochastic teacher forcing strategy applied during model training. Specifically, training consists of short stochastic rollouts in which the proportion of ground truth inputs is gradually decreased in favor of model-generated predictions. Our results show that the proposed surrogate model achieves accurate and efficient predictions across a range of transient brain deformation scenarios, scaling to meshes with up to 150,000 nodes. The introduced stochastic teacher forcing technique substantially improves long-term rollout stability, reducing the maximum prediction error from 6.7 mm to 3.5 mm. We further integrate the trained surrogate model into an interactive neurosurgical simulation environment, achieving runtimes below 10 ms per simulation step on consumer-grade inference hardware. Our proposed deep learning framework enables rapid, smooth and accurate biomechanical simulations of dynamic brain tissue deformation, laying the foundation for realistic surgical training environments.

