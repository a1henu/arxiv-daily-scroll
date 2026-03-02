---
layout: default
title: AoE: Always-on Egocentric Human Video Collection for Embodied AI
---

# AoE: Always-on Egocentric Human Video Collection for Embodied AI
**arXiv**：[2602.23893v1](https://arxiv.org/abs/2602.23893) · [PDF](https://arxiv.org/pdf/2602.23893.pdf)  
**作者**：Bowen Yang, Zishuo Li, Yang Sun, Changtao Miao, Yifan Yang, Man Luo, Xiaotong Yan, Feng Jiang, Jinchuan Shi, Yankai Fu, Ning Chen, Junkai Zhao, Pengwei Wang, Guocai Yao, Shanghang Zhang, Hao Chen, Zhe Li, Kai Zhu  

**一句话要点**：提出AoE系统以低成本收集大规模第一人称视频数据，解决具身AI数据稀缺问题。

**关键词**：第一人称视频, 具身AI, 数据收集, 云边协同, 智能手机应用

## 3 点简述
- 现有数据收集方法成本高、依赖复杂硬件，难以扩展。
- AoE利用智能手机和云边协同架构，实现低成本、场景无关的数据采集。
- 实验表明高质量第一人称数据显著提升真实世界泛化能力。

## 摘要（原文）

> Embodied foundation models require large-scale, high-quality real-world interaction data for pre-training and scaling. However, existing data collection methods suffer from high infrastructure costs, complex hardware dependencies, and limited interaction scope, making scalable expansion challenging. In fact, humans themselves are ideal physically embodied agents. Therefore, obtaining egocentric real-world interaction data from globally distributed "human agents" offers advantages of low cost and sustainability. To this end, we propose the Always-on Egocentric (AoE) data collection system, which aims to simplify hardware dependencies by leveraging humans themselves and their smartphones, enabling low-cost, highly efficient, and scene-agnostic real-world interaction data collection to address the challenge of data scarcity. Specifically, we first employ an ergonomic neck-mounted smartphone holder to enable low-barrier, large-scale egocentric data collection through a cloud-edge collaborative architecture. Second, we develop a cross-platform mobile APP that leverages on-device compute for real-time processing, while the cloud hosts automated labeling and filtering pipelines that transform raw videos into high-quality training data. Finally, the AoE system supports distributed Ego video data collection by anyone, anytime, and anywhere. We evaluate AoE on data preprocessing quality and downstream tasks, demonstrating that high-quality egocentric data significantly boosts real-world generalization.

