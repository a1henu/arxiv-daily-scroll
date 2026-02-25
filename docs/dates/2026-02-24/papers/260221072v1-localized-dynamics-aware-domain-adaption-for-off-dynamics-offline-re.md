---
layout: default
title: Localized Dynamics-Aware Domain Adaption for Off-Dynamics Offline Reinforcement Learning
---

# Localized Dynamics-Aware Domain Adaption for Off-Dynamics Offline Reinforcement Learning
**arXiv**：[2602.21072v1](https://arxiv.org/abs/2602.21072) · [PDF](https://arxiv.org/pdf/2602.21072.pdf)  
**作者**：Zhangjie Xia, Yu Yang, Pan Xu  

**一句话要点**：提出LoDADA方法，通过局部动态感知域适应解决离动态离线强化学习中的数据重用问题。

**关键词**：离动态离线强化学习, 域适应, 动态不匹配, 数据聚类, 局部分布对齐, 离线策略学习

## 3 点简述
- 核心问题：离动态离线强化学习中，源域和目标域动态不匹配，现有方法全局处理或逐点过滤效率低。
- 方法要点：聚类源和目标数据，基于域判别估计簇级动态差异，保留小差异簇的源数据，过滤大差异簇。
- 实验或效果：在多种全局和局部动态偏移环境中，LoDADA优于现有方法，通过局部分布不匹配更好利用源数据。

## 摘要（原文）

> Off-dynamics offline reinforcement learning (RL) aims to learn a policy for a target domain using limited target data and abundant source data collected under different transition dynamics. Existing methods typically address dynamics mismatch either globally over the state space or via pointwise data filtering; these approaches can miss localized cross-domain similarities or incur high computational cost. We propose Localized Dynamics-Aware Domain Adaptation (LoDADA), which exploits localized dynamics mismatch to better reuse source data. LoDADA clusters transitions from source and target datasets and estimates cluster-level dynamics discrepancy via domain discrimination. Source transitions from clusters with small discrepancy are retained, while those from clusters with large discrepancy are filtered out. This yields a fine-grained and scalable data selection strategy that avoids overly coarse global assumptions and expensive per-sample filtering. We provide theoretical insights and extensive experiments across environments with diverse global and local dynamics shifts. Results show that LoDADA consistently outperforms state-of-the-art off-dynamics offline RL methods by better leveraging localized distribution mismatch.

