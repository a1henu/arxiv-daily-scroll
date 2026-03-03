---
layout: default
title: CharacterFlywheel: Scaling Iterative Improvement of Engaging and Steerable LLMs in Production
---

# CharacterFlywheel: Scaling Iterative Improvement of Engaging and Steerable LLMs in Production
**arXiv**：[2603.01973v1](https://arxiv.org/abs/2603.01973) · [PDF](https://arxiv.org/pdf/2603.01973.pdf)  
**作者**：Yixin Nie, Lin Guan, Zhongyao Ma, Anchit Gupta, Yipin Zhou, Xiao Li, Zhengping Zhou, Raymond Zeng, Gelin Zhou, Shigan Chu, Ajay Thampi, Wancen Mu, Nathan Shuster, Ketong Wang, Lin Chen, Jason Brewer, Derek Hao Hu, Alexander McCauley, Jason Weston, Sem Park, Na Zhang, Kevin Tang  

**一句话要点**：提出CharacterFlywheel迭代飞轮过程，以优化生产社交聊天应用中的大型语言模型

**关键词**：大型语言模型优化, 迭代飞轮过程, 社交聊天应用, 用户参与度提升, 可控性改进, 生产部署

## 3 点简述
- 核心问题：在Instagram、WhatsApp和Messenger等生产社交聊天应用中，如何持续改进大型语言模型的用户参与度和可控性。
- 方法要点：基于LLaMA 3.1，通过数据策展、奖励建模、监督微调、强化学习和离线在线评估，迭代优化15代模型。
- 实验或效果：2024年7月至2025年4月部署中，8个新模型中有7个提升参与度，最高提升8.8%参与广度和19.4%参与深度，指令遵循从59.2%增至84.8%。

## 摘要（原文）

> This report presents CharacterFlywheel, an iterative flywheel process for improving large language models (LLMs) in production social chat applications across Instagram, WhatsApp, and Messenger. Starting from LLaMA 3.1, we refined models across 15 generations using data from both internal and external real-user traffic. Through continuous deployments from July 2024 to April 2025, we conducted controlled 7-day A/B tests showing consistent engagement improvements: 7 of 8 newly deployed models demonstrated positive lift over the baseline, with the strongest performers achieving up to 8.8% improvement in engagement breadth and 19.4% in engagement depth. We also observed substantial gains in steerability, with instruction following increasing from 59.2% to 84.8% and instruction violations decreasing from 26.6% to 5.8%. We detail the CharacterFlywheel process which integrates data curation, reward modeling to estimate and interpolate the landscape of engagement metrics, supervised fine-tuning (SFT), reinforcement learning (RL), and both offline and online evaluation to ensure reliable progress at each optimization step. We also discuss our methods for overfitting prevention and navigating production dynamics at scale. These contributions advance the scientific rigor and understanding of LLMs in social applications serving millions of users.

