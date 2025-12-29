---
layout: default
title: Pruning as a Game: Equilibrium-Driven Sparsification of Neural Networks
---

# Pruning as a Game: Equilibrium-Driven Sparsification of Neural Networks
**arXiv**：[2512.22106v1](https://arxiv.org/abs/2512.22106) · [PDF](https://arxiv.org/pdf/2512.22106.pdf)  
**作者**：Zubair Shah, Noaman Khan  

**一句话要点**：提出基于博弈均衡的神经网络剪枝方法，将剪枝视为模型组件间策略互动的结果。

**关键词**：神经网络剪枝, 博弈论, 稀疏化, 均衡驱动, 模型压缩, 理论解释

## 3 点简述
- 核心问题：传统剪枝方法依赖启发式重要性评分或正则化，缺乏理论解释。
- 方法要点：建模参数组为连续非合作博弈玩家，均衡时冗余参与者自然归零实现剪枝。
- 实验或效果：标准基准测试显示，该方法在稀疏性-准确性权衡上具有竞争力，提供可解释的理论基础。

## 摘要（原文）

> Neural network pruning is widely used to reduce model size and computational cost. Yet, most existing methods treat sparsity as an externally imposed constraint, enforced through heuristic importance scores or training-time regularization. In this work, we propose a fundamentally different perspective: pruning as an equilibrium outcome of strategic interaction among model components. We model parameter groups such as weights, neurons, or filters as players in a continuous non-cooperative game, where each player selects its level of participation in the network to balance contribution against redundancy and competition. Within this formulation, sparsity emerges naturally when continued participation becomes a dominated strategy at equilibrium. We analyze the resulting game and show that dominated players collapse to zero participation under mild conditions, providing a principled explanation for pruning behavior. Building on this insight, we derive a simple equilibrium-driven pruning algorithm that jointly updates network parameters and participation variables without relying on explicit importance scores. This work focuses on establishing a principled formulation and empirical validation of pruning as an equilibrium phenomenon, rather than exhaustive architectural or large-scale benchmarking. Experiments on standard benchmarks demonstrate that the proposed approach achieves competitive sparsity-accuracy trade-offs while offering an interpretable, theory-grounded alternative to existing pruning methods.

