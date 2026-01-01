---
layout: default
title: Dynamic Policy Learning for Legged Robot with Simplified Model Pretraining and Model Homotopy Transfer
---

# Dynamic Policy Learning for Legged Robot with Simplified Model Pretraining and Model Homotopy Transfer
**arXiv**：[2512.24698v1](https://arxiv.org/abs/2512.24698) · [PDF](https://arxiv.org/pdf/2512.24698.pdf)  
**作者**：Dongyun Kang, Min-Gyu Kim, Tae-Gyu Song, Hajun Kim, Sehoon Ha, Hae-Won Park  

**一句话要点**：提出基于简化模型预训练和模型同伦迁移的延续学习框架，以高效生成和优化腿式机器人的动态行为。

**关键词**：腿式机器人, 强化学习, 模型同伦, 策略迁移, 动态运动生成, 简化模型预训练

## 3 点简述
- 核心问题：腿式机器人动态运动生成困难，强化学习需大量奖励调优或高质量演示，模型差异阻碍策略迁移。
- 方法要点：先使用单刚体模型预训练策略捕获核心运动模式，再通过模型同伦逐步迁移到全身模型，最小化性能损失。
- 实验或效果：在翻转和墙辅助机动等动态任务中验证，实现更快收敛和更稳定迁移，成功部署于真实四足机器人。

## 摘要（原文）

> Generating dynamic motions for legged robots remains a challenging problem. While reinforcement learning has achieved notable success in various legged locomotion tasks, producing highly dynamic behaviors often requires extensive reward tuning or high-quality demonstrations. Leveraging reduced-order models can help mitigate these challenges. However, the model discrepancy poses a significant challenge when transferring policies to full-body dynamics environments. In this work, we introduce a continuation-based learning framework that combines simplified model pretraining and model homotopy transfer to efficiently generate and refine complex dynamic behaviors. First, we pretrain the policy using a single rigid body model to capture core motion patterns in a simplified environment. Next, we employ a continuation strategy to progressively transfer the policy to the full-body environment, minimizing performance loss. To define the continuation path, we introduce a model homotopy from the single rigid body model to the full-body model by gradually redistributing mass and inertia between the trunk and legs. The proposed method not only achieves faster convergence but also demonstrates superior stability during the transfer process compared to baseline methods. Our framework is validated on a range of dynamic tasks, including flips and wall-assisted maneuvers, and is successfully deployed on a real quadrupedal robot.

