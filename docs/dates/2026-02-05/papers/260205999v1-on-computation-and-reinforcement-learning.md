---
layout: default
title: On Computation and Reinforcement Learning
---

# On Computation and Reinforcement Learning
**arXiv**：[2602.05999v1](https://arxiv.org/abs/2602.05999) · [PDF](https://arxiv.org/pdf/2602.05999.pdf)  
**作者**：Raj Ghugare, Michał Bortkiewicz, Alicja Ziarko, Benjamin Eysenbach  

**一句话要点**：提出计算有界策略以分析强化学习中计算量对性能的影响

**关键词**：强化学习, 计算有界策略, 泛化性能, 长时域任务, 模型无关规划

## 3 点简述
- 核心问题：计算量如何影响强化学习策略的学习能力和泛化性能
- 方法要点：形式化计算有界策略，设计可变计算量的最小架构
- 实验或效果：在31个任务上验证增加计算量可提升性能和长时域泛化

## 摘要（原文）

> How does the amount of compute available to a reinforcement learning (RL) policy affect its learning? Can policies using a fixed amount of parameters, still benefit from additional compute? The standard RL framework does not provide a language to answer these questions formally. Empirically, deep RL policies are often parameterized as neural networks with static architectures, conflating the amount of compute and the number of parameters. In this paper, we formalize compute bounded policies and prove that policies which use more compute can solve problems and generalize to longer-horizon tasks that are outside the scope of policies with less compute. Building on prior work in algorithmic learning and model-free planning, we propose a minimal architecture that can use a variable amount of compute. Our experiments complement our theory. On a set 31 different tasks spanning online and offline RL, we show that $(1)$ this architecture achieves stronger performance simply by using more compute, and $(2)$ stronger generalization on longer-horizon test tasks compared to standard feedforward networks or deep residual network using up to 5 times more parameters.

