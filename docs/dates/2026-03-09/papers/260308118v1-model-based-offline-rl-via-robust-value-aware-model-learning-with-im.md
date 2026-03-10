---
layout: default
title: Model-based Offline RL via Robust Value-Aware Model Learning with Implicitly Differentiable Adaptive Weighting
---

# Model-based Offline RL via Robust Value-Aware Model Learning with Implicitly Differentiable Adaptive Weighting
**arXiv**：[2603.08118v1](https://arxiv.org/abs/2603.08118) · [PDF](https://arxiv.org/pdf/2603.08118.pdf)  
**作者**：Zhongjian Qiao, Jiafei Lyu, Boxiang Lyu, Yao Shu, Siyang Gao, Shuang Qiu  

**一句话要点**：提出ROMI方法以解决基于模型的离线强化学习中模型利用导致的性能下降问题

**关键词**：离线强化学习, 模型学习, 鲁棒优化, 值感知, 状态不确定性, 梯度稳定

## 3 点简述
- 核心问题：模型误差导致模型利用，引发Q值低估和梯度爆炸，影响算法稳定性和性能
- 方法要点：引入鲁棒值感知模型学习，通过可调状态不确定性集预测接近最小Q值的未来状态，实现可控保守性和稳定更新
- 实验或效果：在D4RL和NeoRL数据集上显著优于RAMBO，并在RAMBO表现不佳的数据集上达到或超越其他先进方法

## 摘要（原文）

> Model-based offline reinforcement learning (RL) aims to enhance offline RL with a dynamics model that facilitates policy exploration. However, \textit{model exploitation} could occur due to inevitable model errors, degrading algorithm performance. Adversarial model learning offers a theoretical framework to mitigate model exploitation by solving a maximin formulation. Within such a paradigm, RAMBO~\citep{rigter2022rambo} has emerged as a representative and most popular method that provides a practical implementation with model gradient. However, we empirically reveal that severe Q-value underestimation and gradient explosion can occur in RAMBO with only slight hyperparameter tuning, suggesting that it tends to be overly conservative and suffers from unstable model updates. To address these issues, we propose \textbf{RO}bust value-aware \textbf{M}odel learning with \textbf{I}mplicitly differentiable adaptive weighting (ROMI). Instead of updating the dynamics model with model gradient, ROMI introduces a novel robust value-aware model learning approach. This approach requires the dynamics model to predict future states with values close to the minimum Q-value within a scale-adjustable state uncertainty set, enabling controllable conservatism and stable model updates. To further improve out-of-distribution (OOD) generalization during multi-step rollouts, we propose implicitly differentiable adaptive weighting, a bi-level optimization scheme that adaptively achieves dynamics- and value-aware model learning. Empirical results on D4RL and NeoRL datasets show that ROMI significantly outperforms RAMBO and achieves competitive or superior performance compared to other state-of-the-art methods on datasets where RAMBO typically underperforms. Code is available at https://github.com/zq2r/ROMI.git.

