---
layout: default
title: GrndCtrl: Grounding World Models via Self-Supervised Reward Alignment
---

# GrndCtrl: Grounding World Models via Self-Supervised Reward Alignment
**arXiv**：[2512.01952v1](https://arxiv.org/abs/2512.01952) · [PDF](https://arxiv.org/pdf/2512.01952.pdf)  
**作者**：Haoyang He, Jay Patrikar, Dong-Ki Kim, Max Smith, Daniel McGann, Ali-akbar Agha-mohammadi, Shayegan Omidshafiei, Sebastian Scherer  

**一句话要点**：提出GrndCtrl框架，通过自监督奖励对齐增强世界模型的几何基础，以提升导航任务的空间一致性和稳定性。

**关键词**：世界模型, 自监督学习, 奖励对齐, 几何基础, 导航任务, 强化学习

## 3 点简述
- 视频世界模型缺乏几何基础，限制其在导航任务中的空间一致性和长期稳定性。
- 引入RLWG框架，利用几何和感知奖励自监督对齐预训练世界模型，基于GRPO实现奖励对齐。
- 在户外环境中，GrndCtrl优于监督微调，实现更优的空间一致性和导航稳定性。

## 摘要（原文）

> Recent advances in video world modeling have enabled large-scale generative models to simulate embodied environments with high visual fidelity, providing strong priors for prediction, planning, and control. Yet, despite their realism, these models often lack geometric grounding, limiting their use in navigation tasks that require spatial coherence and long-horizon stability. We introduce Reinforcement Learning with World Grounding (RLWG), a self-supervised post-training framework that aligns pretrained world models with a physically verifiable structure through geometric and perceptual rewards. Analogous to reinforcement learning from verifiable feedback (RLVR) in language models, RLWG can use multiple rewards that measure pose cycle-consistency, depth reprojection, and temporal coherence. We instantiate this framework with GrndCtrl, a reward-aligned adaptation method based on Group Relative Policy Optimization (GRPO), yielding world models that maintain stable trajectories, consistent geometry, and reliable rollouts for embodied navigation. Like post-training alignment in large language models, GrndCtrl leverages verifiable rewards to bridge generative pretraining and grounded behavior, achieving superior spatial coherence and navigation stability over supervised fine-tuning in outdoor environments.

