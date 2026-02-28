---
layout: default
title: AHBid: An Adaptable Hierarchical Bidding Framework for Cross-Channel Advertising
---

# AHBid: An Adaptable Hierarchical Bidding Framework for Cross-Channel Advertising
**arXiv**：[2602.22650v1](https://arxiv.org/abs/2602.22650) · [PDF](https://arxiv.org/pdf/2602.22650.pdf)  
**作者**：Xinxin Yang, Yangyang Tang, Yikun Zhou, Yaolei Liu, Yun Li, Bo Yang  

**一句话要点**：提出AHBid框架以解决跨渠道广告中动态预算分配与约束优化的挑战

**关键词**：跨渠道广告, 自动竞价, 扩散模型, 预算分配, 约束优化, 强化学习

## 3 点简述
- 核心问题：跨渠道广告环境复杂动态，现有优化方法缺乏灵活性，强化学习方法难以捕捉历史依赖。
- 方法要点：结合扩散模型生成规划与实时控制，通过约束执行和轨迹精炼机制提升适应性。
- 实验或效果：大规模离线与在线A/B测试显示，AHBid相比基线提升总回报13.57%。

## 摘要（原文）

> In online advertising, the inherent complexity and dynamic nature of advertising environments necessitate the use of auto-bidding services to assist advertisers in bid optimization. This complexity is further compounded in multi-channel scenarios, where effective allocation of budgets and constraints across channels with distinct behavioral patterns becomes critical for optimizing return on investment. Current approaches predominantly rely on either optimization-based strategies or reinforcement learning techniques. However, optimization-based methods lack flexibility in adapting to dynamic market conditions, while reinforcement learning approaches often struggle to capture essential historical dependencies and observational patterns within the constraints of Markov Decision Process frameworks. To address these limitations, we propose AHBid, an Adaptable Hierarchical Bidding framework that integrates generative planning with real-time control. The framework employs a high-level generative planner based on diffusion models to dynamically allocate budgets and constraints by effectively capturing historical context and temporal patterns. We introduce a constraint enforcement mechanism to ensure compliance with specified constraints, along with a trajectory refinement mechanism that enhances adaptability to environmental changes through the utilization of historical data. The system further incorporates a control-based bidding algorithm that synergistically combines historical knowledge with real-time information, significantly improving both adaptability and operational efficacy. Extensive experiments conducted on large-scale offline datasets and through online A/B tests demonstrate the effectiveness of AHBid, yielding a 13.57% increase in overall return compared to existing baselines.

