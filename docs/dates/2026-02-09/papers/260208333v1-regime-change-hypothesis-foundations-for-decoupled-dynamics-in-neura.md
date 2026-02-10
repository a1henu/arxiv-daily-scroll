---
layout: default
title: Regime Change Hypothesis: Foundations for Decoupled Dynamics in Neural Network Training
---

# Regime Change Hypothesis: Foundations for Decoupled Dynamics in Neural Network Training
**arXiv**：[2602.08333v1](https://arxiv.org/abs/2602.08333) · [PDF](https://arxiv.org/pdf/2602.08333.pdf)  
**作者**：Cristian Pérez-Corral, Alberto Fernández-Hernández, Jose I. Mestre, Manuel F. Dolz, Jose Duato, Enrique S. Quintana-Ortí  

**一句话要点**：提出激活模式两阶段变化假说，为分段线性网络训练动态提供理论基础与监测工具。

**关键词**：神经网络训练动态, 激活模式稳定性, 分段线性网络, 两阶段训练, ReLU网络, 优化策略

## 3 点简述
- 核心问题：深度神经网络训练动态难以刻画，尤其在ReLU模型中激活模式变化与权重更新的关系。
- 方法要点：证明参数扰动下激活模式的局部稳定性，并经验性追踪权重与激活模式变化以验证两阶段行为。
- 实验或效果：在多种架构中，激活模式变化比权重更新幅度早衰减3倍，支持训练后期在稳定激活机制中进行。

## 摘要（原文）

> Despite the empirical success of DNN, their internal training dynamics remain difficult to characterize. In ReLU-based models, the activation pattern induced by a given input determines the piecewise-linear region in which the network behaves affinely. Motivated by this geometry, we investigate whether training exhibits a two-timescale behavior: an early stage with substantial changes in activation patterns and a later stage where weight updates predominantly refine the model within largely stable activation regimes. We first prove a local stability property: outside measure-zero sets of parameters and inputs, sufficiently small parameter perturbations preserve the activation pattern of a fixed input, implying locally affine behavior within activation regions. We then empirically track per-iteration changes in weights and activation patterns across fully-connected and convolutional architectures, as well as Transformer-based models, where activation patterns are recorded in the ReLU feed-forward (MLP/FFN) submodules, using fixed validation subsets. Across the evaluated settings, activation-pattern changes decay 3 times earlier than weight-update magnitudes, showing that late-stage training often proceeds within relatively stable activation regimes. These findings provide a concrete, architecture-agnostic instrument for monitoring training dynamics and motivate further study of decoupled optimization strategies for piecewise-linear networks. For reproducibility, code and experiment configurations will be released upon acceptance.

