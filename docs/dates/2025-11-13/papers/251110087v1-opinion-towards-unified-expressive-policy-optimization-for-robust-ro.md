---
layout: default
title: Opinion: Towards Unified Expressive Policy Optimization for Robust Robot Learning
---

# Opinion: Towards Unified Expressive Policy Optimization for Robust Robot Learning
**arXiv**：[2511.10087v1](https://arxiv.org/abs/2511.10087) · [PDF](https://arxiv.org/pdf/2511.10087.pdf)  
**作者**：Haidong Huang, Haiyue Zhu. Jiayu Song, Xixin Zhao, Yaohua Zhou, Jiayi Zhang, Yuze Zhai, Xiaocong Li  

**一句话要点**：提出UEPO统一生成框架以解决机器人离线到在线强化学习中的模态覆盖不足和分布偏移问题

**关键词**：离线到在线强化学习, 扩散策略, 动态分歧正则化, 机器人学习, 数据增强, 泛化能力

## 3 点简述
- 核心问题：离线到在线强化学习中模态覆盖有限和在线适应时的分布偏移
- 方法要点：使用多种子动态感知扩散策略和动态分歧正则化机制
- 实验或效果：在D4RL基准上，运动任务提升5.9%，灵巧操作提升12.4%

## 摘要（原文）

> Offline-to-online reinforcement learning (O2O-RL) has emerged as a promising paradigm for safe and efficient robotic policy deployment but suffers from two fundamental challenges: limited coverage of multimodal behaviors and distributional shifts during online adaptation. We propose UEPO, a unified generative framework inspired by large language model pretraining and fine-tuning strategies. Our contributions are threefold: (1) a multi-seed dynamics-aware diffusion policy that efficiently captures diverse modalities without training multiple models; (2) a dynamic divergence regularization mechanism that enforces physically meaningful policy diversity; and (3) a diffusion-based data augmentation module that enhances dynamics model generalization. On the D4RL benchmark, UEPO achieves +5.9\% absolute improvement over Uni-O4 on locomotion tasks and +12.4\% on dexterous manipulation, demonstrating strong generalization and scalability.

