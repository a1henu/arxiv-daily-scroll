---
layout: default
title: RELATE: A Reinforcement Learning-Enhanced LLM Framework for Advertising Text Generation
---

# RELATE: A Reinforcement Learning-Enhanced LLM Framework for Advertising Text Generation
**arXiv**：[2602.11780v1](https://arxiv.org/abs/2602.11780) · [PDF](https://arxiv.org/pdf/2602.11780.pdf)  
**作者**：Jinfang Wang, Jiajie Liu, Jianwei Wu, Ziqin Luo, Zhen Chen, Chunlei Li, Biao Han, Tao Deng, Yi Li, Shuanglong Li, Lin Liu  

**一句话要点**：提出RELATE强化学习框架，统一广告文本生成与目标对齐以提升转化率。

**关键词**：广告文本生成, 强化学习, 端到端框架, 转化率优化, 政策约束

## 3 点简述
- 现有两阶段广告文本生成系统存在优化目标不一致和漏斗效率低的问题。
- RELATE通过强化学习将性能和合规目标整合到生成过程中，使用多维奖励建模。
- 实验和在线部署显示RELATE在严格政策约束下显著提升点击转化率。

## 摘要（原文）

> In online advertising, advertising text plays a critical role in attracting user engagement and driving advertiser value. Existing industrial systems typically follow a two-stage paradigm, where candidate texts are first generated and subsequently aligned with online performance metrics such as click-through rate(CTR). This separation often leads to misaligned optimization objectives and low funnel efficiency, limiting global optimality.
>   To address these limitations, we propose RELATE, a reinforcement learning-based end-to-end framework that unifies generation and objective alignment within a single model. Instead of decoupling text generation from downstream metric alignment, RELATE integrates performance and compliance objectives directly into the generation process via policy learning. To better capture ultimate advertiser value beyond click-level signals, We incorporate conversion-oriented metrics into the objective and jointly model them with compliance constraints as multi-dimensional rewards, enabling the model to generate high-quality ad texts that improve conversion performance under policy constraints.
>   Extensive experiments on large-scale industrial datasets demonstrate that RELATE consistently outperforms baselines. Furthermore, online deployment on a production advertising platform yields statistically significant improvements in click-through conversion rate(CTCVR) under strict policy constraints, validating the robustness and real-world effectiveness of the proposed framework.

