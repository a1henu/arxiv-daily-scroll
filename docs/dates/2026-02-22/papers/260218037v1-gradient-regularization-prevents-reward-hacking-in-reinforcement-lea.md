---
layout: default
title: Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards
---

# Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards
**arXiv**：[2602.18037v1](https://arxiv.org/abs/2602.18037) · [PDF](https://arxiv.org/pdf/2602.18037.pdf)  
**作者**：Johannes Ackermann, Michael Noukhovitch, Takashi Ishida, Masashi Sugiyama  

**一句话要点**：提出梯度正则化以防止强化学习从人类反馈和可验证奖励中的奖励黑客问题

**关键词**：强化学习, 奖励黑客, 梯度正则化, 语言模型, 人类反馈, 可验证奖励

## 3 点简述
- 核心问题：奖励黑客，即策略利用奖励模型的不准确性学习非预期行为。
- 方法要点：通过梯度正则化偏置策略更新到奖励更准确的平坦区域。
- 实验或效果：在语言模型强化学习实验中，梯度正则化优于KL惩罚，提升GPT判断胜率并防止奖励黑客。

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) or Verifiable Rewards (RLVR) are two key steps in the post-training of modern Language Models (LMs). A common problem is reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior. Most previous works address this by limiting the policy update with a Kullback-Leibler (KL) penalty towards a reference model. We propose a different framing: Train the LM in a way that biases policy updates towards regions in which the reward is more accurate. First, we derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence. Gradient regularization (GR) can then be used to bias training to flatter regions and thereby maintain reward model accuracy. We confirm these results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF. We then show that Reference Resets of the KL penalty implicitly use GR to find flatter regions with higher reward accuracy. We further improve on this by proposing to use explicit GR with an efficient finite-difference estimate. Empirically, GR performs better than a KL penalty across a diverse set of RL experiments with LMs. GR achieves a higher GPT-judged win-rate in RLHF, avoids overly focusing on the format in rule-based math rewards, and prevents hacking the judge in LLM-as-a-Judge math tasks.

