---
layout: default
title: User-Centric Object Navigation: A Benchmark with Integrated User Habits for Personalized Embodied Object Search
---

# User-Centric Object Navigation: A Benchmark with Integrated User Habits for Personalized Embodied Object Search
**arXiv**：[2602.06459v1](https://arxiv.org/abs/2602.06459) · [PDF](https://arxiv.org/pdf/2602.06459.pdf)  
**作者**：Hongcheng Wang, Jinyu Zhu, Hao Dong  

**一句话要点**：提出用户中心对象导航基准，集成用户习惯以解决个性化家庭环境中的对象搜索问题。

**关键词**：用户中心对象导航, 个性化机器人导航, 习惯检索模块, 家庭环境对象搜索, 基准数据集

## 3 点简述
- 现有对象导航基准忽略用户特定放置习惯，限制代理在个性化环境中的适应性。
- 引入UcON基准，包含约22,600个用户习惯和489个对象类别，并设计习惯检索模块辅助导航决策。
- 实验显示当前方法在习惯驱动放置下性能下降，而集成用户习惯能持续提升成功率。

## 摘要（原文）

> In the evolving field of robotics, the challenge of Object Navigation (ON) in household environments has attracted significant interest. Existing ON benchmarks typically place objects in locations guided by general scene priors, without accounting for the specific placement habits of individual users. This omission limits the adaptability of navigation agents in personalized household environments. To address this, we introduce User-centric Object Navigation (UcON), a new benchmark that incorporates user-specific object placement habits, referred to as user habits. This benchmark requires agents to leverage these user habits for more informed decision-making during navigation. UcON encompasses approximately 22,600 user habits across 489 object categories. UcON is, to our knowledge, the first benchmark that explicitly formalizes and evaluates habit-conditioned object navigation at scale and covers the widest range of target object categories. Additionally, we propose a habit retrieval module to extract and utilize habits related to target objects, enabling agents to infer their likely locations more effectively. Experimental results demonstrate that current SOTA methods exhibit substantial performance degradation under habit-driven object placement, while integrating user habits consistently improves success rates. Code is available at https://github.com/whcpumpkin/User-Centric-Object-Navigation.

