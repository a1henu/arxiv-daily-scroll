---
layout: default
title: RL-VLA$^3$: Reinforcement Learning VLA Accelerating via Full Asynchronism
---

# RL-VLA$^3$: Reinforcement Learning VLA Accelerating via Full Asynchronism
**arXiv**：[2602.05765v1](https://arxiv.org/abs/2602.05765) · [PDF](https://arxiv.org/pdf/2602.05765.pdf)  
**作者**：Zhong Guan, Haoran Sun, Yongjian Guo, Shuai Di, Xiaodong Bai, Jing Long, Tianyun Zhao, Mingxi Luo, Chen Zhou, Yucheng Guo, Qiming Yang, Wanting Xu, Wen Huang, Yunxuan Ma, Hongke Zhao, Likang Wu, Xiaotie Deng, Xi Xiao, Sheng Wen, Yicheng Gong, Junwu Xiong  

**一句话要点**：提出全异步强化学习框架以加速视觉-语言-动作模型训练

**关键词**：视觉-语言-动作模型, 强化学习, 异步训练, 吞吐量优化, 多GPU扩展

## 3 点简述
- 核心问题：现有同步训练框架导致资源利用率低和吞吐量瓶颈
- 方法要点：设计多级解耦架构，实现环境交互、策略生成和模型更新的全异步并行
- 实验或效果：在LIBERO基准上吞吐量提升最高达59.25%，优化后可达126.67%

## 摘要（原文）

> In recent years, Vision-Language-Action (VLA) models have emerged as a crucial pathway towards general embodied intelligence, yet their training efficiency has become a key bottleneck. Although existing reinforcement learning (RL)-based training frameworks like RLinf can enhance model generalization, they still rely on synchronous execution, leading to severe resource underutilization and throughput limitations during environment interaction, policy generation (rollout), and model update phases (actor). To overcome this challenge, this paper, for the first time, proposes and implements a fully-asynchronous policy training framework encompassing the entire pipeline from environment interaction, rollout generation, to actor policy updates. Systematically drawing inspiration from asynchronous optimization ideas in large model RL, our framework designs a multi-level decoupled architecture. This includes asynchronous parallelization of environment interaction and trajectory collection, streaming execution for policy generation, and decoupled scheduling for training updates. We validated the effectiveness of our method across diverse VLA models and environments. On the LIBERO benchmark, the framework achieves throughput improvements of up to 59.25\% compared to existing synchronous strategies. When deeply optimizing separation strategies, throughput can be increased by as much as 126.67\%. We verified the effectiveness of each asynchronous component via ablation studies. Scaling law validation across 8 to 256 GPUs demonstrates our method's excellent scalability under most conditions.

