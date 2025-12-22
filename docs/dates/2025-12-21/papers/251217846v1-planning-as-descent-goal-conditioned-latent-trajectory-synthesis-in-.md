---
layout: default
title: Planning as Descent: Goal-Conditioned Latent Trajectory Synthesis in Learned Energy Landscapes
---

# Planning as Descent: Goal-Conditioned Latent Trajectory Synthesis in Learned Energy Landscapes
**arXiv**：[2512.17846v1](https://arxiv.org/abs/2512.17846) · [PDF](https://arxiv.org/pdf/2512.17846.pdf)  
**作者**：Carlos Vélez García, Miguel Cazorla, Jorge Pomares  

**一句话要点**：提出Planning as Descent框架，用于离线目标条件强化学习，通过能量函数和梯度优化实现轨迹合成。

**关键词**：离线强化学习, 目标条件规划, 能量函数, 轨迹合成, 梯度优化, 自监督学习

## 3 点简述
- 核心问题：离线目标条件强化学习中，解耦建模常导致训练-测试不匹配，需稳健的轨迹规划方法。
- 方法要点：学习目标条件能量函数评估潜在轨迹，规划作为能量景观中的梯度优化，训练与推理计算一致。
- 实验或效果：在OGBench立方体操作任务上，PaD达到95%成功率，优于先前方法，噪声数据训练提升性能。

## 摘要（原文）

> We present Planning as Descent (PaD), a framework for offline goal-conditioned reinforcement learning that grounds trajectory synthesis in verification. Instead of learning a policy or explicit planner, PaD learns a goal-conditioned energy function over entire latent trajectories, assigning low energy to feasible, goal-consistent futures. Planning is realized as gradient-based refinement in this energy landscape, using identical computation during training and inference to reduce train-test mismatch common in decoupled modeling pipelines.
>   PaD is trained via self-supervised hindsight goal relabeling, shaping the energy landscape around the planning dynamics. At inference, multiple trajectory candidates are refined under different temporal hypotheses, and low-energy plans balancing feasibility and efficiency are selected.
>   We evaluate PaD on OGBench cube manipulation tasks. When trained on narrow expert demonstrations, PaD achieves state-of-the-art 95\% success, strongly outperforming prior methods that peak at 68\%. Remarkably, training on noisy, suboptimal data further improves success and plan efficiency, highlighting the benefits of verification-driven planning. Our results suggest learning to evaluate and refine trajectories provides a robust alternative to direct policy learning for offline, reward-free planning.

