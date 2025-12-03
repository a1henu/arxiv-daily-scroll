---
layout: default
title: Beyond Playtesting: A Generative Multi-Agent Simulation System for Massively Multiplayer Online Games
---

# Beyond Playtesting: A Generative Multi-Agent Simulation System for Massively Multiplayer Online Games
**arXiv**：[2512.02358v1](https://arxiv.org/abs/2512.02358) · [PDF](https://arxiv.org/pdf/2512.02358.pdf)  
**作者**：Ran Zhang, Kun Ouyang, Tiancheng Ma, Yida Yang, Dong Fang  

**一句话要点**：提出基于大语言模型的生成式多智能体模拟系统，以优化大型多人在线游戏的数值设计

**关键词**：大型多人在线游戏, 生成式智能体, 大语言模型, 监督微调, 强化学习, 数值设计优化

## 3 点简述
- 核心问题：传统MMO游戏优化方法依赖在线实验或简化模拟，成本高、保真度低，影响玩家体验
- 方法要点：通过监督微调和强化学习，利用真实玩家数据训练大语言模型，实现游戏特定领域的智能体决策
- 实验或效果：系统在实验中展示与真实玩家行为的高度一致性和对干预的合理因果响应，提供可靠、可解释的优化框架

## 摘要（原文）

> Optimizing numerical systems and mechanism design is crucial for enhancing player experience in Massively Multiplayer Online (MMO) games. Traditional optimization approaches rely on large-scale online experiments or parameter tuning over predefined statistical models, which are costly, time-consuming, and may disrupt player experience. Although simplified offline simulation systems are often adopted as alternatives, their limited fidelity prevents agents from accurately mimicking real player reasoning and reactions to interventions. To address these limitations, we propose a generative agent-based MMO simulation system empowered by Large Language Models (LLMs). By applying Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) on large-scale real player behavioral data, we adapt LLMs from general priors to game-specific domains, enabling realistic and interpretable player decision-making. In parallel, a data-driven environment model trained on real gameplay logs reconstructs dynamic in-game systems. Experiments demonstrate strong consistency with real-world player behaviors and plausible causal responses under interventions, providing a reliable, interpretable, and cost-efficient framework for data-driven numerical design optimization.

