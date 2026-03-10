---
layout: default
title: DeReCo: Decoupling Representation and Coordination Learning for Object-Adaptive Decentralized Multi-Robot Cooperative Transport
---

# DeReCo: Decoupling Representation and Coordination Learning for Object-Adaptive Decentralized Multi-Robot Cooperative Transport
**arXiv**：[2603.08111v1](https://arxiv.org/abs/2603.08111) · [PDF](https://arxiv.org/pdf/2603.08111.pdf)  
**作者**：Kazuki Shibata, Ryosuke Sota, Shandil Dhiresh Bosch, Yuki Kadokawa, Tsurumine Yoshihisa, Takamitsu Matsubara  

**一句话要点**：提出DeReCo框架，通过解耦表示与协调学习，提升多机器人协同运输的样本效率与泛化能力。

**关键词**：多机器人协同运输, 表示学习, 协调学习, 去中心化执行, 样本效率, 泛化能力

## 3 点简述
- 核心问题：去中心化多机器人协同运输中，对象依赖表示学习与协调学习因部分可观测性和非平稳性相互干扰，导致训练低效。
- 方法要点：采用三阶段训练策略，先集中学习协调，再重建对象表示，最后逐步移除特权信息，实现解耦优化。
- 实验或效果：在仿真和真实机器人实验中，DeReCo优于基线，能泛化到未见对象，提升性能与样本效率。

## 摘要（原文）

> Generalizing decentralized multi-robot cooperative transport across objects with diverse shapes and physical properties remains a fundamental challenge. Under decentralized execution, two key challenges arise: object-dependent representation learning under partial observability and coordination learning in multi-agent reinforcement learning (MARL) under non-stationarity. A typical approach jointly optimizes object-dependent representations and coordinated policies in an end-to-end manner while randomizing object shapes and physical properties during training. However, this joint optimization tightly couples representation and coordination learning, introducing bidirectional interference: inaccurate representations under partial observability destabilize coordination learning, while non-stationarity in MARL further degrades representation learning, resulting in sample-inefficient training. To address this structural coupling, we propose DeReCo, a novel MARL framework that decouples representation and coordination learning for object-adaptive multi-robot cooperative transport, improving sample efficiency and generalization across objects and transport scenarios. DeReCo adopts a three-stage training strategy: (1) centralized coordination learning with privileged object information, (2) reconstruction of object-dependent representations from local observations, and (3) progressive removal of privileged information for decentralized execution. This decoupling mitigates interference between representation and coordination learning and enables stable and sample-efficient training. Experimental results show that DeReCo outperforms baselines in simulation on three training objects, generalizes to six unseen objects with varying masses and friction coefficients, and achieves superior performance on two unseen objects in real-robot experiments.

