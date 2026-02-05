---
layout: default
title: Dynamical Regimes of Multimodal Diffusion Models
---

# Dynamical Regimes of Multimodal Diffusion Models
**arXiv**：[2602.04780v1](https://arxiv.org/abs/2602.04780) · [PDF](https://arxiv.org/pdf/2602.04780.pdf)  
**作者**：Emil Albrychiewicz, Andrés Franco Valiente, Li-Ching Chen  

**一句话要点**：提出耦合扩散模型理论框架，基于非平衡统计物理解释多模态生成机制

**关键词**：扩散模型, 多模态生成, 非平衡统计物理, 耦合过程, 时间尺度, 理论框架

## 3 点简述
- 核心问题：多模态扩散模型的理论机制不明确，常出现去同步伪影
- 方法要点：使用耦合Ornstein-Uhlenbeck过程建模，分析相互作用时间尺度的谱层次
- 实验或效果：在MNIST数据集上验证理论预测，如同步间隙和耦合强度影响

## 摘要（原文）

> Diffusion based generative models have achieved unprecedented fidelity in synthesizing high dimensional data, yet the theoretical mechanisms governing multimodal generation remain poorly understood. Here, we present a theoretical framework for coupled diffusion models, using coupled Ornstein-Uhlenbeck processes as a tractable model. By using the nonequilibrium statistical physics of dynamical phase transitions, we demonstrate that multimodal generation is governed by a spectral hierarchy of interaction timescales rather than simultaneous resolution. A key prediction is the ``synchronization gap'', a temporal window during the reverse generative process where distinct eigenmodes stabilize at different rates, providing a theoretical explanation for common desynchronization artifacts. We derive analytical conditions for speciation and collapse times under both symmetric and anisotropic coupling regimes, establishing strict bounds for coupling strength to avoid unstable symmetry breaking. We show that the coupling strength acts as a spectral filter that enforces a tunable temporal hierarchy on generation. We support these predictions through controlled experiments with diffusion models trained on MNIST datasets and exact score samplers. These results motivate time dependent coupling schedules that target mode specific timescales, offering a potential alternative to ad hoc guidance tuning.

