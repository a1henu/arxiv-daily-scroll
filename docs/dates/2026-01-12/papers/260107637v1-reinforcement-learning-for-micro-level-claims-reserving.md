---
layout: default
title: Reinforcement Learning for Micro-Level Claims Reserving
---

# Reinforcement Learning for Micro-Level Claims Reserving
**arXiv**：[2601.07637v1](https://arxiv.org/abs/2601.07637) · [PDF](https://arxiv.org/pdf/2601.07637.pdf)  
**作者**：Benjamin Avanzi, Ronald Richman, Bernard Wong, Mario Wüthrich, Yagebu Xie  

**一句话要点**：提出基于强化学习的索赔级马尔可夫决策过程，以解决个体索赔准备金估计中的样本限制和修订稳定性问题。

**关键词**：强化学习, 索赔准备金估计, 马尔可夫决策过程, 精算应用, 样本效率, 稳定性优化

## 3 点简述
- 核心问题：传统准备金模型通常作为一次性预测器训练，仅从已结案索赔学习，导致样本量减少和选择偏差。
- 方法要点：将个体索赔准备金估计建模为索赔级马尔可夫决策过程，使用连续动作和奖励设计平衡准确性与稳定修订。
- 实验或效果：在CAS和SPLICE合成数据集上，Soft Actor-Critic实现提供竞争性索赔级准确性和强聚合准备金性能，尤其对未成熟索赔段。

## 摘要（原文）

> Outstanding claim liabilities are revised repeatedly as claims develop, yet most modern reserving models are trained as one-shot predictors and typically learn only from settled claims. We formulate individual claims reserving as a claim-level Markov decision process in which an agent sequentially updates outstanding claim liability (OCL) estimates over development, using continuous actions and a reward design that balances accuracy with stable reserve revisions. A key advantage of this reinforcement learning (RL) approach is that it can learn from all observed claim trajectories, including claims that remain open at valuation, thereby avoiding the reduced sample size and selection effects inherent in supervised methods trained on ultimate outcomes only. We also introduce practical components needed for actuarial use -- initialisation of new claims, temporally consistent tuning via a rolling-settlement scheme, and an importance-weighting mechanism to mitigate portfolio-level underestimation driven by the rarity of large claims. On CAS and SPLICE synthetic general insurance datasets, the proposed Soft Actor-Critic implementation delivers competitive claim-level accuracy and strong aggregate OCL performance, particularly for the immature claim segments that drive most of the liability.

