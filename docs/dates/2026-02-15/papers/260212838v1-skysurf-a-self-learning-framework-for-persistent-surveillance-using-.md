---
layout: default
title: SKYSURF: A Self-learning Framework for Persistent Surveillance using Cooperative Aerial Gliders
---

# SKYSURF: A Self-learning Framework for Persistent Surveillance using Cooperative Aerial Gliders
**arXiv**：[2602.12838v1](https://arxiv.org/abs/2602.12838) · [PDF](https://arxiv.org/pdf/2602.12838.pdf)  
**作者**：Houssem Eddine Mohamadi, Nadjia Kara  

**一句话要点**：提出基于合作滑翔无人机的自学习框架，以提升持久监视能力并降低能耗。

**关键词**：无人机持久监视, 合作滑翔, 自学习框架, 路径规划, 能耗优化, 非确定性代理

## 3 点简述
- 核心问题：小型无人机续航有限，影响持久监视应用。
- 方法要点：采用局部-全局行为管理、非确定性有限状态代理建模，结合任务规划和路径跟踪优化。
- 实验或效果：相比基准方法，目标检测提升两倍，六小时能耗仅约6%。

## 摘要（原文）

> The success of surveillance applications involving small unmanned aerial vehicles (UAVs) depends on how long the limited on-board power would persist. To cope with this challenge, alternative renewable sources of lift are sought. One promising solution is to extract energy from rising masses of buoyant air. This paper proposes a local-global behavioral management and decision-making approach for the autonomous deployment of soaring-capable UAVs. The cooperative UAVs are modeled as non-deterministic finite state-based rational agents. In addition to a mission planning module for assigning tasks and issuing dynamic navigation waypoints for a new path planning scheme, in which the concepts of visibility and prediction are applied to avoid the collisions. Moreover, a delayed learning and tuning strategy is employed optimize the gains of the path tracking controller. Rigorous comparative analyses carried out with three benchmarking baselines and 15 evolutionary algorithms highlight the adequacy of the proposed approach for maintaining the surveillance persistency (staying aloft for longer periods without landing) and maximizing the detection of targets (two times better than non-cooperative and semi-cooperative approaches) with less power consumption (almost 6% of battery consumed in six hours).

