---
layout: default
title: Generalised Linear Models in Deep Bayesian RL with Learnable Basis Functions
---

# Generalised Linear Models in Deep Bayesian RL with Learnable Basis Functions
**arXiv**：[2512.20974v1](https://arxiv.org/abs/2512.20974) · [PDF](https://arxiv.org/pdf/2512.20974.pdf)  
**作者**：Jingyang You, Hanna Kurniawati  

**一句话要点**：提出GLiBRL方法，通过可学习基函数和广义线性模型，提升深度贝叶斯强化学习中的模型学习效率与准确性。

**关键词**：贝叶斯强化学习, 模型学习, 广义线性模型, 可学习基函数, MetaWorld基准

## 3 点简述
- 核心问题：经典贝叶斯强化学习方法假设已知转移和奖励模型形式，限制了实际应用；深度方法使用ELBO优化困难，可能导致任务参数不明确。
- 方法要点：引入GLiBRL，结合可学习基函数和广义线性模型，实现转移和奖励模型的高效准确学习，支持完全可处理的边际似然和贝叶斯推断。
- 实验或效果：在MetaWorld ML10/45基准测试中，GLiBRL将VariBAD的成功率提升高达2.7倍，相比其他方法表现出低方差和稳定性能。

## 摘要（原文）

> Bayesian Reinforcement Learning (BRL) provides a framework for generalisation of Reinforcement Learning (RL) problems from its use of Bayesian task parameters in the transition and reward models. However, classical BRL methods assume known forms of transition and reward models, reducing their applicability in real-world problems. As a result, recent deep BRL methods have started to incorporate model learning, though the use of neural networks directly on the joint data and task parameters requires optimising the Evidence Lower Bound (ELBO). ELBOs are difficult to optimise and may result in indistinctive task parameters, hence compromised BRL policies. To this end, we introduce a novel deep BRL method, Generalised Linear Models in Deep Bayesian RL with Learnable Basis Functions (GLiBRL), that enables efficient and accurate learning of transition and reward models, with fully tractable marginal likelihood and Bayesian inference on task parameters and model noises. On challenging MetaWorld ML10/45 benchmarks, GLiBRL improves the success rate of one of the state-of-the-art deep BRL methods, VariBAD, by up to 2.7x. Comparing against representative or recent deep BRL / Meta-RL methods, such as MAML, RL2, SDVT, TrMRL and ECET, GLiBRL also demonstrates its low-variance and decent performance consistently.

