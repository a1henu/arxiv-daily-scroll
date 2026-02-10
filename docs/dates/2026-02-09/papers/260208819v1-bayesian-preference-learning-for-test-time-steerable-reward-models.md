---
layout: default
title: Bayesian Preference Learning for Test-Time Steerable Reward Models
---

# Bayesian Preference Learning for Test-Time Steerable Reward Models
**arXiv**：[2602.08819v1](https://arxiv.org/abs/2602.08819) · [PDF](https://arxiv.org/pdf/2602.08819.pdf)  
**作者**：Jiwoo Hong, Shao Tang, Zhipeng Wang  

**一句话要点**：提出变分上下文奖励建模以解决测试时奖励模型不可调整的问题

**关键词**：奖励建模, 贝叶斯推断, 上下文学习, 强化学习对齐, 多目标优化

## 3 点简述
- 奖励模型在训练后静态化，难以适应测试时复杂偏好分布
- 基于贝叶斯推断，通过上下文演示实现奖励模型的测试时可调整性
- 在单目标和多目标设置中提升准确率，并增强RL训练的实际应用效果

## 摘要（原文）

> Reward models are central to aligning language models with human preferences via reinforcement learning (RL). As RL is increasingly applied to settings such as verifiable rewards and multi-objective alignment, RMs are expected to encode more complex and multifaceted preference distributions. However, classifier RMs remain static once trained, limiting their adaptability at test time. We propose Variational In-Context Reward Modeling (ICRM), a novel Bayesian reward modeling objective that enables test-time steerability via in-context preference demonstrations. ICRM casts reward modeling as amortized variational inference over a latent preference probability under the Bradley-Terry model using a conjugate Beta prior. We show that ICRM adapt to unseen preference distributions at test time for both single and multi-objective settings. With more in-context demonstrations, ICRM gains 34% accuracy on SafeRLHF and 9% accuracy on RM-Bench in the single-objective setting, while widening the Pareto frontier with a 4% gain in hypervolume on helpfulness and refusal benchmarks. We further study the practical applicability of ICRM for RL training, showing that it can effectively encode verifiable rewards by outperforming a conventional RM in math reasoning. Finally, we provide theoretical guarantees that the variational objective admits a global interior optimum with finite confidence, and we analyze how KL regularization mitigates reward over-optimization.

