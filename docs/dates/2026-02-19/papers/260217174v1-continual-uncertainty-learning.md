---
layout: default
title: Continual uncertainty learning
---

# Continual uncertainty learning
**arXiv**：[2602.17174v1](https://arxiv.org/abs/2602.17174) · [PDF](https://arxiv.org/pdf/2602.17174.pdf)  
**作者**：Heisei Yonezawa, Ansei Yonezawa, Itsuro Kajiwara  

**一句话要点**：提出基于课程持续学习框架以解决非线性动力系统多源不确定性鲁棒控制问题

**关键词**：持续学习, 鲁棒控制, 深度强化学习, 非线性动力系统, 不确定性处理, 仿真到现实迁移

## 3 点简述
- 核心问题：非线性动力系统多源不确定性叠加导致鲁棒控制策略学习效率低和性能次优
- 方法要点：将复杂控制问题分解为持续学习任务序列，结合模型基控制器加速收敛
- 实验或效果：应用于汽车动力总成主动振动控制，验证了鲁棒性和仿真到现实迁移成功

## 摘要（原文）

> Robust control of mechanical systems with multiple uncertainties remains a fundamental challenge, particularly when nonlinear dynamics and operating-condition variations are intricately intertwined. While deep reinforcement learning (DRL) combined with domain randomization has shown promise in mitigating the sim-to-real gap, simultaneously handling all sources of uncertainty often leads to sub-optimal policies and poor learning efficiency. This study formulates a new curriculum-based continual learning framework for robust control problems involving nonlinear dynamical systems in which multiple sources of uncertainty are simultaneously superimposed. The key idea is to decompose a complex control problem with multiple uncertainties into a sequence of continual learning tasks, in which strategies for handling each uncertainty are acquired sequentially. The original system is extended into a finite set of plants whose dynamic uncertainties are gradually expanded and diversified as learning progresses. The policy is stably updated across the entire plant sets associated with tasks defined by different uncertainty configurations without catastrophic forgetting. To ensure learning efficiency, we jointly incorporate a model-based controller (MBC), which guarantees a shared baseline performance across the plant sets, into the learning process to accelerate the convergence. This residual learning scheme facilitates task-specific optimization of the DRL agent for each uncertainty, thereby enhancing sample efficiency. As a practical industrial application, this study applies the proposed method to designing an active vibration controller for automotive powertrains. We verified that the resulting controller is robust against structural nonlinearities and dynamic variations, realizing successful sim-to-real transfer.

