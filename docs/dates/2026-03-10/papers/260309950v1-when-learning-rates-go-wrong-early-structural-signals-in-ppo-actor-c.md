---
layout: default
title: When Learning Rates Go Wrong: Early Structural Signals in PPO Actor-Critic
---

# When Learning Rates Go Wrong: Early Structural Signals in PPO Actor-Critic
**arXiv**：[2603.09950v1](https://arxiv.org/abs/2603.09950) · [PDF](https://arxiv.org/pdf/2603.09950.pdf)  
**作者**：Alberto Fernández-Hernández, Cristian Pérez-Corral, Jose I. Mestre, Manuel F. Dolz, Jose Duato, Enrique S. Quintana-Ortí  

**一句话要点**：提出基于激活模式平衡的早期筛选方法，以优化PPO中学习率选择问题。

**关键词**：强化学习, PPO算法, 学习率优化, 神经网络结构, 早期筛选, 激活模式分析

## 3 点简述
- 核心问题：PPO中学习率不当导致收敛慢或不稳定，需高效筛选训练。
- 方法要点：利用OUI指标量化网络激活模式，理论连接学习率与神经元结构变化。
- 实验或效果：在10%训练时OUI能区分学习率，结合早期回报实现高精度筛选。

## 摘要（原文）

> Deep Reinforcement Learning systems are highly sensitive to the learning rate (LR), and selecting stable and performant training runs often requires extensive hyperparameter search. In Proximal Policy Optimization (PPO) actor--critic methods, small LR values lead to slow convergence, whereas large LR values may induce instability or collapse. We analyse this phenomenon from the behavior of the hidden neurons in the network using the Overfitting-Underfitting Indicator (OUI), a metric that quantifies the balance of binary activation patterns over a fixed probe batch. We introduce an efficient batch-based formulation of OUI and derive a theoretical connection between LR and activation sign changes, clarifying how a correct evolution of the neuron's inner structure depends on the step size.
>   Empirically, across three discrete-control environments and multiple seeds, we show that OUI measured at only 10\% of training already discriminates between LR regimes. We observe a consistent asymmetry: critic networks achieving highest return operate in an intermediate OUI band (avoiding saturation), whereas actor networks achieving highest return exhibit comparatively high OUI values. We then compare OUI-based screening rules against early return, clip-based, divergence-based, and flip-based criteria under matched recall over successful runs. In this setting, OUI provides the strongest early screening signal: OUI alone achieves the best precision at broader recall, while combining early return with OUI yields the highest precision in best-performing screening regimes, enabling aggressive pruning of unpromising runs without requiring full training.

