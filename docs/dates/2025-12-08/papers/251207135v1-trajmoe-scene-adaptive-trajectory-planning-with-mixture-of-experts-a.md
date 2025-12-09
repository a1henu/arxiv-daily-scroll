---
layout: default
title: TrajMoE: Scene-Adaptive Trajectory Planning with Mixture of Experts and Reinforcement Learning
---

# TrajMoE: Scene-Adaptive Trajectory Planning with Mixture of Experts and Reinforcement Learning
**arXiv**：[2512.07135v1](https://arxiv.org/abs/2512.07135) · [PDF](https://arxiv.org/pdf/2512.07135.pdf)  
**作者**：Zebin Xing, Pengxuan Yang, Linbo Wang, Yichen Zhang, Yiming Hu, Yupeng Zheng, Junli Wang, Yinfeng Gao, Guang Li, Kun Ma, Long Chen, Zhongpu Xia, Qichao Zhang, Hangjun Ye, Dongbin Zhao  

**一句话要点**：提出TrajMoE，通过混合专家和强化学习实现场景自适应轨迹规划

**关键词**：自动驾驶, 轨迹规划, 混合专家, 强化学习, 场景自适应

## 3 点简述
- 核心问题：现有自动驾驶轨迹规划方法忽视场景差异和缺乏策略驱动的轨迹评估机制
- 方法要点：使用MoE为不同场景定制轨迹先验，并利用强化学习微调轨迹评分
- 实验或效果：在navsim ICCV基准测试中得分51.08，排名第三

## 摘要（原文）

> Current autonomous driving systems often favor end-to-end frameworks, which take sensor inputs like images and learn to map them into trajectory space via neural networks. Previous work has demonstrated that models can achieve better planning performance when provided with a prior distribution of possible trajectories. However, these approaches often overlook two critical aspects: 1) The appropriate trajectory prior can vary significantly across different driving scenarios. 2) Their trajectory evaluation mechanism lacks policy-driven refinement, remaining constrained by the limitations of one-stage supervised training. To address these issues, we explore improvements in two key areas. For problem 1, we employ MoE to apply different trajectory priors tailored to different scenarios. For problem 2, we utilize Reinforcement Learning to fine-tune the trajectory scoring mechanism. Additionally, we integrate models with different perception backbones to enhance perceptual features. Our integrated model achieved a score of 51.08 on the navsim ICCV benchmark, securing third place.

