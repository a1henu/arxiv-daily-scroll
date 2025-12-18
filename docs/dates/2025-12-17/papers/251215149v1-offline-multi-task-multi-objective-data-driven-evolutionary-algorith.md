---
layout: default
title: Offline Multi-Task Multi-Objective Data-Driven Evolutionary Algorithm with Language Surrogate Model and Implicit Q-Learning
---

# Offline Multi-Task Multi-Objective Data-Driven Evolutionary Algorithm with Language Surrogate Model and Implicit Q-Learning
**arXiv**：[2512.15149v1](https://arxiv.org/abs/2512.15149) · [PDF](https://arxiv.org/pdf/2512.15149.pdf)  
**作者**：Xian-Rong Zhang, Yue-Jiao Gong, Zeyuan Ma, Jun Zhang  

**一句话要点**：提出Q-MetaSur作为即插即用代理建模方案，以解决离线多任务多目标优化中的复杂目标近似问题。

**关键词**：离线优化, 多任务多目标优化, 代理建模, 大语言模型, 强化学习, 序列到序列建模

## 3 点简述
- 核心问题：现有代理建模在复杂多任务多目标优化中依赖重复近似，效率受限。
- 方法要点：采用基于大语言模型的序列到序列建模，结合监督调优和强化学习微调的两阶段离线训练策略。
- 实验或效果：在CEC2019基准测试中，Q-MetaSur在目标近似精度和优化收敛性上优于代表性基线。

## 摘要（原文）

> Data-driven evolutionary algorithms has shown surprising results in addressing expensive optimization problems through robust surrogate modeling. Though promising, existing surrogate modeling schemes may encounter limitations in complex optimization problems with many sub-objectives, which rely on repeated and tedious approximation. To address such technical gap, we propose Q-MetaSur as a plug-and-play surrogate modeling scheme capable of providing unified and generalized surrogate learning. Specifically, we consider multi-task-multi-objective optimization~(MTMOO) in offline setting. Several key designs are proposed: 1) we transform objective approximation into sequence-to-sequence modeling where MTMOO problem can be represented by tenxual tokenization. To operate under such auto-regressive modeling, we introduce a Large Language Model-based surrogate model that first encodes a MTMOO instance and then decodes objective values of unseen decision variables. To ensure stability in training the proposed model, we propose a two-stage offline training strategy that operates as a synergy of supervised tuning and RL fine-tuning, which first exploits offline dataset to fit existing knowledge and then leverages RL to enhance model's generalization performance. Extensive empirical results on the CEC2019 benchmark demonstrate that Q-MetaSur not only outperforms representative surrogate baselines in objective approximation accuracy, but also helps underlying evolutionary algorithms achieve both desired optimization convergence and improved pareto optimality.

