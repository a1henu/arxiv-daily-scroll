---
layout: default
title: Continual GUI Agents
---

# Continual GUI Agents
**arXiv**：[2601.20732v1](https://arxiv.org/abs/2601.20732) · [PDF](https://arxiv.org/pdf/2601.20732.pdf)  
**作者**：Ziwei Liu, Borui Kang, Hangjie Yuan, Zixiang Zhao, Wei Li, Yifan Zhu, Tao Feng  

**一句话要点**：提出GUI-AiF强化微调框架以解决GUI代理在动态环境中的持续学习问题

**关键词**：GUI代理, 持续学习, 强化微调, 动态环境, 交互点对齐

## 3 点简述
- 核心问题：GUI代理在动态数据分布（如新域或分辨率）下性能下降，现有方法因交互点和区域多样性而失效
- 方法要点：引入GUI-AiF框架，通过APR-iF和ARR-iF奖励稳定学习，对齐动态交互点和区域
- 实验或效果：实验显示GUI-AiF超越现有基线，建立了首个GUI代理持续学习框架

## 摘要（原文）

> As digital environments (data distribution) are in flux, with new GUI data arriving over time-introducing new domains or resolutions-agents trained on static environments deteriorate in performance. In this work, we introduce Continual GUI Agents, a new task that requires GUI agents to perform continual learning under shifted domains and resolutions. We find existing methods fail to maintain stable grounding as GUI distributions shift over time, due to the diversity of UI interaction points and regions in fluxing scenarios. To address this, we introduce GUI-Anchoring in Flux (GUI-AiF), a new reinforcement fine-tuning framework that stabilizes continual learning through two novel rewards: Anchoring Point Reward in Flux (APR-iF) and Anchoring Region Reward in Flux (ARR-iF). These rewards guide the agents to align with shifting interaction points and regions, mitigating the tendency of existing reward strategies to over-adapt to static grounding cues (e.g., fixed coordinates or element scales). Extensive experiments show GUI-AiF surpasses state-of-the-art baselines. Our work establishes the first continual learning framework for GUI agents, revealing the untapped potential of reinforcement fine-tuning for continual GUI Agents.

