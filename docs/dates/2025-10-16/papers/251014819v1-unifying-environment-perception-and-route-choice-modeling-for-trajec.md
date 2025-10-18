---
layout: default
title: Unifying Environment Perception and Route Choice Modeling for Trajectory Representation Learning
---

# Unifying Environment Perception and Route Choice Modeling for Trajectory Representation Learning
**arXiv**：[2510.14819v1](https://arxiv.org/abs/2510.14819) · [PDF](https://arxiv.org/pdf/2510.14819.pdf)  
**作者**：Ji Cao, Yu Wang, Tongya Zheng, Zujie Ren, Canghong Jin, Gang Chen, Mingli Song  

**一句话要点**：提出PRTraj框架，统一环境感知与路径选择建模以改进轨迹表示学习

**关键词**：轨迹表示学习, 环境感知, 路径选择建模, 多粒度语义, 下游任务评估

## 3 点简述
- 现有轨迹表示学习方法忽略外部环境和内部路径选择行为，导致表示不完整
- PRTraj通过环境感知模块和路径选择编码器，捕获多粒度语义和决策序列
- 在3个真实数据集和5个下游任务中验证有效性，并展示强数据效率

## 摘要（原文）

> Trajectory Representation Learning (TRL) aims to encode raw trajectories into
> low-dimensional vectors, which can then be leveraged in various downstream
> tasks, including travel time estimation, location prediction, and trajectory
> similarity analysis. However, existing TRL methods suffer from a key oversight:
> treating trajectories as isolated spatio-temporal sequences, without
> considering the external environment and internal route choice behavior that
> govern their formation. To bridge this gap, we propose a novel framework that
> unifies comprehensive environment \textbf{P}erception and explicit
> \textbf{R}oute choice modeling for effective \textbf{Traj}ectory representation
> learning, dubbed \textbf{PRTraj}. Specifically, PRTraj first introduces an
> Environment Perception Module to enhance the road network by capturing
> multi-granularity environmental semantics from surrounding POI distributions.
> Building on this environment-aware backbone, a Route Choice Encoder then
> captures the route choice behavior inherent in each trajectory by modeling its
> constituent road segment transitions as a sequence of decisions. These
> route-choice-aware representations are finally aggregated to form the global
> trajectory embedding. Extensive experiments on 3 real-world datasets across 5
> downstream tasks validate the effectiveness and generalizability of PRTraj.
> Moreover, PRTraj demonstrates strong data efficiency, maintaining robust
> performance under few-shot scenarios. Our code is available at:
> https://anonymous.4open.science/r/PRTraj.

