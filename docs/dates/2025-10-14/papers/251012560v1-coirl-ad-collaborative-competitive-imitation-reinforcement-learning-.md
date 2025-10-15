---
layout: default
title: CoIRL-AD: Collaborative-Competitive Imitation-Reinforcement Learning in Latent World Models for Autonomous Driving
---

# CoIRL-AD: Collaborative-Competitive Imitation-Reinforcement Learning in Latent World Models for Autonomous Driving
**arXiv**：[2510.12560v1](https://arxiv.org/abs/2510.12560) · [PDF](https://arxiv.org/pdf/2510.12560.pdf)  
**作者**：Xiaoji Zheng, Ziyuan Yang, Yanhao Chen, Yuhang Peng, Yuanrong Tang, Gengyuan Liu, Bokui Chen, Jiangtao Gong  

**一句话要点**：提出CoIRL-AD框架，结合模仿与强化学习提升自动驾驶泛化能力

**关键词**：自动驾驶, 模仿学习, 强化学习, 双策略框架, 泛化能力, 长尾场景

## 3 点简述
- 端到端自动驾驶模型仅用模仿学习泛化能力差，强化学习样本效率低且不稳定
- 采用竞争性双策略框架，让模仿与强化学习代理在训练中交互，避免梯度冲突
- 在nuScenes数据集上碰撞率降低18%，泛化能力和长尾场景性能提升

## 摘要（原文）

> End-to-end autonomous driving models trained solely with imitation learning
> (IL) often suffer from poor generalization. In contrast, reinforcement learning
> (RL) promotes exploration through reward maximization but faces challenges such
> as sample inefficiency and unstable convergence. A natural solution is to
> combine IL and RL. Moving beyond the conventional two-stage paradigm (IL
> pretraining followed by RL fine-tuning), we propose CoIRL-AD, a competitive
> dual-policy framework that enables IL and RL agents to interact during
> training. CoIRL-AD introduces a competition-based mechanism that facilitates
> knowledge exchange while preventing gradient conflicts. Experiments on the
> nuScenes dataset show an 18% reduction in collision rate compared to baselines,
> along with stronger generalization and improved performance on long-tail
> scenarios. Code is available at: https://github.com/SEU-zxj/CoIRL-AD.

