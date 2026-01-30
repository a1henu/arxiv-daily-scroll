---
layout: default
title: Reinforcement Learning for Adaptive Composition of Quantum Circuit Optimisation Passes
---

# Reinforcement Learning for Adaptive Composition of Quantum Circuit Optimisation Passes
**arXiv**：[2601.21629v1](https://arxiv.org/abs/2601.21629) · [PDF](https://arxiv.org/pdf/2601.21629.pdf)  
**作者**：Daniel Mills, Ifan Williams, Jacob Swain, Gabriel Matos, Enrico Rinaldi, Alexander Koziell-Pipe  

**一句话要点**：提出强化学习代理以自适应组合量子电路优化通道序列，提升双量子比特门减少效果。

**关键词**：强化学习, 量子电路优化, 自适应序列组合, 双量子比特门减少, PyTKET

## 3 点简述
- 核心问题：量子电路优化通道顺序依赖用户或通用默认序列，缺乏针对特定电路的自适应优化。
- 方法要点：训练强化学习代理，动作空间为PyTKET默认序列中的双量子比特门减少通道，学习组合优化序列。
- 实验或效果：在多样化测试集上，代理移除双量子比特门的平均和中位数分数分别为57.7%和56.7%，优于最佳默认序列。

## 摘要（原文）

> Many quantum software development kits provide a suite of circuit optimisation passes. These passes have been highly optimised and tested in isolation. However, the order in which they are applied is left to the user, or else defined in general-purpose default pass sequences. While general-purpose sequences miss opportunities for optimisation which are particular to individual circuits, designing pass sequences bespoke to particular circuits requires exceptional knowledge about quantum circuit design and optimisation. Here we propose and demonstrate training a reinforcement learning agent to compose optimisation-pass sequences. In particular the agent's action space consists of passes for two-qubit gate count reduction used in default PyTKET pass sequences. For the circuits in our diverse test set, the (mean, median) fraction of two-qubit gates removed by the agent is $(57.7\%, \ 56.7 \%)$, compared to $(41.8 \%, \ 50.0 \%)$ for the next best default pass sequence.

