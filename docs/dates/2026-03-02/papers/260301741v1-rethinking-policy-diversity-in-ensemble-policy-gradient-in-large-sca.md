---
layout: default
title: Rethinking Policy Diversity in Ensemble Policy Gradient in Large-Scale Reinforcement Learning
---

# Rethinking Policy Diversity in Ensemble Policy Gradient in Large-Scale Reinforcement Learning
**arXiv**：[2603.01741v1](https://arxiv.org/abs/2603.01741) · [PDF](https://arxiv.org/pdf/2603.01741.pdf)  
**作者**：Naoki Shitanda, Motoki Omura, Tatsuya Harada, Takayuki Osa  

**一句话要点**：提出耦合策略优化以在大规模强化学习中调控策略多样性提升学习效率

**关键词**：策略集成, 策略梯度, KL约束, 大规模强化学习, 探索多样性

## 3 点简述
- 核心问题：策略集成方法中策略多样性过高可能降低探索质量或训练稳定性
- 方法要点：通过KL约束调控策略间多样性，实现结构化高效探索
- 实验或效果：在灵巧操作等任务上超越SAPG、PBT和PPO，样本效率和最终性能更优

## 摘要（原文）

> Scaling reinforcement learning to tens of thousands of parallel environments requires overcoming the limited exploration capacity of a single policy. Ensemble-based policy gradient methods, which employ multiple policies to collect diverse samples, have recently been proposed to promote exploration. However, merely broadening the exploration space does not always enhance learning capability, since excessive exploration can reduce exploration quality or compromise training stability. In this work, we theoretically analyze the impact of inter-policy diversity on learning efficiency in policy ensembles, and propose Coupled Policy Optimization which regulates diversity through KL constraints between policies. The proposed method enables effective exploration and outperforms strong baselines such as SAPG, PBT, and PPO across multiple tasks, including challenging dexterous manipulation, in terms of both sample efficiency and final performance. Furthermore, analysis of policy diversity and effective sample size during training reveals that follower policies naturally distribute around the leader, demonstrating the emergence of structured and efficient exploratory behavior. Our results indicate that diverse exploration under appropriate regulation is key to achieving stable and sample-efficient learning in ensemble policy gradient methods. Project page at https://naoki04.github.io/paper-cpo/ .

