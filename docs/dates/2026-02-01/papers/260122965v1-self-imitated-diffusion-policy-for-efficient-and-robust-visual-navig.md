---
layout: default
title: Self-Imitated Diffusion Policy for Efficient and Robust Visual Navigation
---

# Self-Imitated Diffusion Policy for Efficient and Robust Visual Navigation
**arXiv**：[2601.22965v1](https://arxiv.org/abs/2601.22965) · [PDF](https://arxiv.org/pdf/2601.22965.pdf)  
**作者**：Runhua Zhang, Junyi Hou, Changxu Cheng, Qiyi Chen, Tao Wang, Wuyue Zhao  

**一句话要点**：提出自模仿扩散策略以提升视觉导航的效率和鲁棒性

**关键词**：视觉导航, 扩散策略, 自模仿学习, 奖励引导, 实时部署, 轨迹规划

## 3 点简述
- 标准扩散策略依赖模仿学习，易继承专家演示的次优性和冗余，导致推理时需计算密集的生成后过滤流程
- SIDP引入奖励引导的自模仿机制，通过选择性模仿自身采样轨迹，鼓励策略高效生成高质量轨迹，减少对大量采样和后过滤的依赖
- 在模拟基准测试中显著优于先前方法，在Jetson Orin Nano上推理速度比基线NavDP快2.5倍，实现高效实时部署

## 摘要（原文）

> Diffusion policies (DP) have demonstrated significant potential in visual navigation by capturing diverse multi-modal trajectory distributions. However, standard imitation learning (IL), which most DP methods rely on for training, often inherits sub-optimality and redundancy from expert demonstrations, thereby necessitating a computationally intensive "generate-then-filter" pipeline that relies on auxiliary selectors during inference. To address these challenges, we propose Self-Imitated Diffusion Policy (SIDP), a novel framework that learns improved planning by selectively imitating a set of trajectories sampled from itself. Specifically, SIDP introduces a reward-guided self-imitation mechanism that encourages the policy to consistently produce high-quality trajectories efficiently, rather than outputs of inconsistent quality, thereby reducing reliance on extensive sampling and post-filtering. During training, we employ a reward-driven curriculum learning paradigm to mitigate inefficient data utility, and goal-agnostic exploration for trajectory augmentation to improve planning robustness. Extensive evaluations on a comprehensive simulation benchmark show that SIDP significantly outperforms previous methods, with real-world experiments confirming its effectiveness across multiple robotic platforms. On Jetson Orin Nano, SIDP delivers a 2.5$\times$ faster inference than the baseline NavDP, i.e., 110ms VS 273ms, enabling efficient real-time deployment.

