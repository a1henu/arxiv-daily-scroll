---
layout: default
title: Grounding Generated Videos in Feasible Plans via World Models
---

# Grounding Generated Videos in Feasible Plans via World Models
**arXiv**：[2602.01960v1](https://arxiv.org/abs/2602.01960) · [PDF](https://arxiv.org/pdf/2602.01960.pdf)  
**作者**：Christos Ziakas, Amir Bar, Alessandra Russo  

**一句话要点**：提出GVP-WM方法，通过世界模型将视频生成计划接地为可行动作序列

**关键词**：视频生成规划, 世界模型, 轨迹优化, 零样本学习, 物理约束

## 3 点简述
- 问题：大规模视频生成模型作为零样本视觉规划器时，常违反时间一致性和物理约束
- 方法：利用动作条件世界模型，通过视频引导潜在共位优化，将视频计划接地到可行轨迹
- 效果：在导航和操作模拟任务中，从违反约束的视频中恢复可行长时程计划

## 摘要（原文）

> Large-scale video generative models have shown emerging capabilities as zero-shot visual planners, yet video-generated plans often violate temporal consistency and physical constraints, leading to failures when mapped to executable actions. To address this, we propose Grounding Video Plans with World Models (GVP-WM), a planning method that grounds video-generated plans into feasible action sequences using a learned action-conditioned world model. At test-time, GVP-WM first generates a video plan from initial and goal observations, then projects the video guidance onto the manifold of dynamically feasible latent trajectories via video-guided latent collocation. In particular, we formulate grounding as a goal-conditioned latent-space trajectory optimization problem that jointly optimizes latent states and actions under world-model dynamics, while preserving semantic alignment with the video-generated plan. Empirically, GVP-WM recovers feasible long-horizon plans from zero-shot image-to-video-generated and motion-blurred videos that violate physical constraints, across navigation and manipulation simulation tasks.

