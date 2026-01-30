---
layout: default
title: NEXUS: Bit-Exact ANN-to-SNN Equivalence via Neuromorphic Gate Circuits with Surrogate-Free Training
---

# NEXUS: Bit-Exact ANN-to-SNN Equivalence via Neuromorphic Gate Circuits with Surrogate-Free Training
**arXiv**：[2601.21279v1](https://arxiv.org/abs/2601.21279) · [PDF](https://arxiv.org/pdf/2601.21279.pdf)  
**作者**：Zhengzheng Tang  

**一句话要点**：提出NEXUS框架，通过基于IF神经元的门电路实现ANN到SNN的比特精确等价，以解决SNN因离散近似导致的精度损失问题。

**关键词**：脉冲神经网络, 比特精确等价, 神经形态门电路, 免代理训练, 能效计算, 空间比特编码

## 3 点简述
- 核心问题：现有SNN方法因用离散脉冲近似连续值而牺牲精度，无法实现与ANN的精确等价。
- 方法要点：利用IF神经元构建IEEE-754浮点运算门电路，结合空间比特编码和免代理STE训练，实现数学上相同的输出。
- 实验或效果：在LLaMA-2 70B等模型上实现0.00%精度损失，平均ULP误差仅6.19，并在神经形态硬件上实现27-168,000倍能效提升。

## 摘要（原文）

> Spiking Neural Networks (SNNs) promise energy-efficient computing through event-driven sparsity, yet all existing approaches sacrifice accuracy by approximating continuous values with discrete spikes. We propose NEXUS, a framework that achieves bit-exact ANN-to-SNN equivalence -- not approximate, but mathematically identical outputs. Our key insight is constructing all arithmetic operations, both linear and nonlinear, from pure IF neuron logic gates that implement IEEE-754 compliant floating-point arithmetic. Through spatial bit encoding (zero encoding error by construction), hierarchical neuromorphic gate circuits (from basic logic gates to complete transformer layers), and surrogate-free STE training (exact identity mapping rather than heuristic approximation), NEXUS produces outputs identical to standard ANNs up to machine precision. Experiments on models up to LLaMA-2 70B demonstrate identical task accuracy (0.00\% degradation) with mean ULP error of only 6.19, while achieving 27-168,000$\times$ energy reduction on neuromorphic hardware. Crucially, spatial bit encoding's single-timestep design renders the framework inherently immune to membrane potential leakage (100\% accuracy across all decay factors $β\in[0.1,1.0]$), while tolerating synaptic noise up to $σ=0.2$ with >98\% gate-level accuracy.

