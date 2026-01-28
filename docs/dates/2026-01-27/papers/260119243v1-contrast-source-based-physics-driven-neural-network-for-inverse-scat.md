---
layout: default
title: Contrast-Source-Based Physics-Driven Neural Network for Inverse Scattering Problems
---

# Contrast-Source-Based Physics-Driven Neural Network for Inverse Scattering Problems
**arXiv**：[2601.19243v1](https://arxiv.org/abs/2601.19243) · [PDF](https://arxiv.org/pdf/2601.19243.pdf)  
**作者**：Yutong Du, Zicheng Liu  

**一句话要点**：提出基于对比源的物理驱动神经网络，以高效解决逆散射问题中的泛化与计算效率限制。

**关键词**：逆散射问题, 物理驱动神经网络, 对比源方法, 自适应总变差损失, 感应电流预测, 无训练神经网络

## 3 点简述
- 核心问题：监督深度神经网络需大规模数据集，无训练神经网络推理时间长，限制逆散射问题实际应用。
- 方法要点：基于对比源预测感应电流分布，结合自适应总变差损失，提升重建鲁棒性与效率。
- 实验或效果：通过数值模拟与实验数据验证，改进成像性能，适应不同对比度与噪声条件。

## 摘要（原文）

> Deep neural networks (DNNs) have recently been applied to inverse scattering problems (ISPs) due to their strong nonlinear mapping capabilities. However, supervised DNN solvers require large-scale datasets, which limits their generalization in practical applications. Untrained neural networks (UNNs) address this issue by updating weights from measured electric fields and prior physical knowledge, but existing UNN solvers suffer from long inference time. To overcome these limitations, this paper proposes a contrast-source-based physics-driven neural network (CSPDNN), which predicts the induced current distribution to improve efficiency and incorporates an adaptive total variation loss for robust reconstruction under varying contrast and noise conditions. The improved imaging performance is validated through comprehensive numerical simulations and experimental data.

