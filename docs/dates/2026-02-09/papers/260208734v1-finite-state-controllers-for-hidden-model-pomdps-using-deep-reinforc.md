---
layout: default
title: Finite-State Controllers for (Hidden-Model) POMDPs using Deep Reinforcement Learning
---

# Finite-State Controllers for (Hidden-Model) POMDPs using Deep Reinforcement Learning
**arXiv**：[2602.08734v1](https://arxiv.org/abs/2602.08734) · [PDF](https://arxiv.org/pdf/2602.08734.pdf)  
**作者**：David Hudák, Maris F. L. Galesloot, Martin Tappler, Martin Kurečka, Nils Jansen, Milan Češka  

**一句话要点**：提出Lexpop框架，利用深度强化学习训练神经策略并提取有限状态控制器，以解决POMDP和HM-POMDP的可扩展性问题。

**关键词**：部分可观察马尔可夫决策过程, 深度强化学习, 有限状态控制器, 鲁棒策略, 隐藏模型POMDP, 策略提取

## 3 点简述
- 核心问题：部分可观察马尔可夫决策过程（POMDP）求解的可扩展性有限，且需在多POMDP场景中保持策略鲁棒性。
- 方法要点：结合深度强化学习训练循环神经网络策略，并通过高效提取方法构建可形式化评估的有限状态控制器。
- 实验或效果：在大型状态空间问题上，Lexpop优于现有POMDP和HM-POMDP求解器。

## 摘要（原文）

> Solving partially observable Markov decision processes (POMDPs) requires computing policies under imperfect state information. Despite recent advances, the scalability of existing POMDP solvers remains limited. Moreover, many settings require a policy that is robust across multiple POMDPs, further aggravating the scalability issue. We propose the Lexpop framework for POMDP solving. Lexpop (1) employs deep reinforcement learning to train a neural policy, represented by a recurrent neural network, and (2) constructs a finite-state controller mimicking the neural policy through efficient extraction methods. Crucially, unlike neural policies, such controllers can be formally evaluated, providing performance guarantees. We extend Lexpop to compute robust policies for hidden-model POMDPs (HM-POMDPs), which describe finite sets of POMDPs. We associate every extracted controller with its worst-case POMDP. Using a set of such POMDPs, we iteratively train a robust neural policy and consequently extract a robust controller. Our experiments show that on problems with large state spaces, Lexpop outperforms state-of-the-art solvers for POMDPs as well as HM-POMDPs.

