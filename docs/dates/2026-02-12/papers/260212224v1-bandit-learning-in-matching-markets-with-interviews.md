---
layout: default
title: Bandit Learning in Matching Markets with Interviews
---

# Bandit Learning in Matching Markets with Interviews
**arXiv**：[2602.12224v1](https://arxiv.org/abs/2602.12224) · [PDF](https://arxiv.org/pdf/2602.12224.pdf)  
**作者**：Amirmahdi Mirfakhar, Xuchuang Wang, Mengfan Xu, Hedyeh Beyhaghi, Mohammad Hajiesmaili  

**一句话要点**：提出基于访谈的匹配市场多臂老虎机学习框架，支持战略延迟以处理双方不确定性。

**关键词**：匹配市场, 多臂老虎机学习, 战略延迟, 去中心化学习, 时间无关遗憾

## 3 点简述
- 研究匹配市场中偏好评估不切实际的问题，将访谈建模为低成本提示以揭示部分偏好信息。
- 扩展企业行动空间以允许战略延迟，支持去中心化学习，无需协调即可从次优雇佣中恢复。
- 设计集中式和去中心化算法，实现时间无关的遗憾，优于无访谈学习稳定匹配的O(log T)遗憾界。

## 摘要（原文）

> Two-sided matching markets rely on preferences from both sides, yet it is often impractical to evaluate preferences. Participants, therefore, conduct a limited number of interviews, which provide early, noisy impressions and shape final decisions. We study bandit learning in matching markets with interviews, modeling interviews as \textit{low-cost hints} that reveal partial preference information to both sides. Our framework departs from existing work by allowing firm-side uncertainty: firms, like agents, may be unsure of their own preferences and can make early hiring mistakes by hiring less preferred agents. To handle this, we extend the firm's action space to allow \emph{strategic deferral} (choosing not to hire in a round), enabling recovery from suboptimal hires and supporting decentralized learning without coordination. We design novel algorithms for (i) a centralized setting with an omniscient interview allocator and (ii) decentralized settings with two types of firm-side feedback. Across all settings, our algorithms achieve time-independent regret, a substantial improvement over the $O(\log T)$ regret bounds known for learning stable matchings without interviews. Also, under mild structured markets, decentralized performance matches the centralized counterpart up to polynomial factors in the number of agents and firms.

