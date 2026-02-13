---
layout: default
title: LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training
---

# LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training
**arXiv**：[2602.11686v1](https://arxiv.org/abs/2602.11686) · [PDF](https://arxiv.org/pdf/2602.11686.pdf)  
**作者**：Xinyi Liu, Yujie Wang, Fangcheng Fu, Xuefeng Xiao, Huixia Li, Jiashi Li, Bin Cui  

**一句话要点**：提出LAER-MoE框架以解决MoE训练中专家负载不平衡问题

**关键词**：专家并行, 负载平衡, MoE训练, 通信优化, 分布式训练

## 3 点简述
- 核心问题：MoE训练中动态路由导致专家负载严重不平衡，成为训练瓶颈。
- 方法要点：引入FSEP并行范式，通过参数分区和All-to-All通信实现专家参数灵活重布局。
- 实验或效果：在A100集群上实验，相比现有系统加速最高达1.69倍。

## 摘要（原文）

> Expert parallelism is vital for effectively training Mixture-of-Experts (MoE) models, enabling different devices to host distinct experts, with each device processing different input data. However, during expert parallel training, dynamic routing results in significant load imbalance among experts: a handful of overloaded experts hinder overall iteration, emerging as a training bottleneck.
>   In this paper, we introduce LAER-MoE, an efficient MoE training framework. The core of LAER-MoE is a novel parallel paradigm, Fully Sharded Expert Parallel (FSEP), which fully partitions each expert parameter by the number of devices and restores partial experts at expert granularity through All-to-All communication during training. This allows for flexible re-layout of expert parameters during training to enhance load balancing. In particular, we perform fine-grained scheduling of communication operations to minimize communication overhead. Additionally, we develop a load balancing planner to formulate re-layout strategies of experts and routing schemes for tokens during training. We perform experiments on an A100 cluster, and the results indicate that our system achieves up to 1.69x acceleration compared to the current state-of-the-art training systems. Source code available at https://github.com/PKU-DAIR/Hetu-Galvatron/tree/laer-moe.

