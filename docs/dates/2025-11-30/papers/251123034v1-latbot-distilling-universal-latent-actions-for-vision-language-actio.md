---
layout: default
title: LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models
---

# LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models
**arXiv**：[2511.23034v1](https://arxiv.org/abs/2511.23034) · [PDF](https://arxiv.org/pdf/2511.23034.pdf)  
**作者**：Zuolei Li, Xingyu Gao, Xiaofan Wang, Jianlong Fu  

**一句话要点**：提出通用潜在动作学习框架，通过蒸馏提升视觉-语言-动作模型在机器人任务中的泛化能力。

**关键词**：潜在动作学习, 视觉-语言-动作模型, 机器人操作, 蒸馏训练, 物理先验, 少样本迁移

## 3 点简述
- 现有方法依赖视觉重建目标，忽略物理先验，导致学习通用表示性能不佳。
- 框架结合未来帧重建和动作序列预测，分解潜在动作为运动和场景令牌以过滤无关动态。
- 在仿真和真实机器人设置中实现强性能，仅需少量轨迹即可完成挑战性任务。

## 摘要（原文）

> Learning transferable latent actions from large-scale object manipulation videos can significantly enhance generalization in downstream robotics tasks, as such representations are agnostic to different robot embodiments. Existing approaches primarily rely on visual reconstruction objectives while neglecting physical priors, leading to sub-optimal performance in learning universal representations. To address these challenges, we propose a Universal Latent Action Learning framework that takes task instructions and multiple frames as inputs, and optimizes both future frame reconstruction and action sequence prediction. Unlike prior works, incorporating action predictions (e.g., gripper or hand trajectories and orientations) allows the model to capture richer physical priors such as real-world distances and orientations, thereby enabling seamless transferability to downstream tasks. We further decompose the latent actions into learnable motion and scene tokens to distinguish the robot's active movements from environmental changes, thus filtering out irrelevant dynamics. By distilling the learned latent actions into the latest VLA models, we achieve strong performance across both simulated (SIMPLER and LIBERO) and real-world robot settings. Notably, with only 10 real-world trajectories per task collected on a Franka robot, our approach successfully completes all five challenging tasks, demonstrating strong few-shot transferability in robotic manipulation.

