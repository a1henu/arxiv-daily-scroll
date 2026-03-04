---
layout: default
title: Proactive Guiding Strategy for Item-side Fairness in Interactive Recommendation
---

# Proactive Guiding Strategy for Item-side Fairness in Interactive Recommendation
**arXiv**：[2603.03094v1](https://arxiv.org/abs/2603.03094) · [PDF](https://arxiv.org/pdf/2603.03094.pdf)  
**作者**：Chongjun Xia, Xiaoyu Shi, Hong Xie, Xianzhi Wang, yun lu, Mingsheng Shang  

**一句话要点**：提出HRL4PFG框架，通过分层强化学习主动引导用户偏好以解决交互推荐中长尾物品公平性问题。

**关键词**：交互推荐, 物品侧公平性, 分层强化学习, 长尾物品, 用户偏好引导, 推荐系统

## 3 点简述
- 核心问题：现有方法直接推荐长尾物品导致用户偏好与推荐不匹配，降低用户参与度和推荐效果。
- 方法要点：采用分层强化学习，宏观过程基于多步反馈生成公平引导目标，微观过程实时调整推荐以平衡用户偏好与公平性。
- 实验或效果：在交互推荐环境中，相比先进方法，显著提升累积交互奖励和最大用户交互长度。

## 摘要（原文）

> Item-side fairness is crucial for ensuring the fair exposure of long-tail items in interactive recommender systems. Existing approaches promote the exposure of long-tail items by directly incorporating them into recommended results. This causes misalignment between user preferences and the recommended long-tail items, which hinders long-term user engagement and reduces the effectiveness of recommendations. We aim for a proactive fairness-guiding strategy, which actively guides user preferences toward long-tail items while preserving user satisfaction during the interactive recommendation process. To this end, we propose HRL4PFG, an interactive recommendation framework that leverages hierarchical reinforcement learning to guide user preferences toward long-tail items progressively. HRL4PFG operates through a macro-level process that generates fairness-guided targets based on multi-step feedback, and a micro-level process that fine-tunes recommendations in real time according to both these targets and evolving user preferences. Extensive experiments show that HRL4PFG improves cumulative interaction rewards and maximum user interaction length by a larger margin when compared with state-of-the-art methods in interactive recommendation environments.

