---
layout: default
title: Choose What to Observe: Task-Aware Semantic-Geometric Representations for Visuomotor Policy
---

# Choose What to Observe: Task-Aware Semantic-Geometric Representations for Visuomotor Policy
**arXiv**：[2603.07875v1](https://arxiv.org/abs/2603.07875) · [PDF](https://arxiv.org/pdf/2603.07875.pdf)  
**作者**：Haoran Ding, Liang Ma, Yaxun Yang, Wen Yang, Tianyu Liu, Anqing Duan, Xiaodan Liang, Dezhen Song, Ivan Laptev, Yoshihiko Nakamura  

**一句话要点**：提出任务感知观察接口，通过语义-几何表示提升视觉运动策略在分布外外观变化下的鲁棒性。

**关键词**：视觉运动策略, 语义分割, 几何表示, 鲁棒性提升, 分布外泛化

## 3 点简述
- 核心问题：视觉运动策略易受原始RGB观测中无关视觉因素影响，导致外观变化下行为脆弱。
- 方法要点：基于开放词汇任务实体分割，构建语义颜色重绘和深度注入的统一图像式表示。
- 实验或效果：在多个基准和策略骨干上保持分布内性能，显著提升分布外视觉偏移的鲁棒性。

## 摘要（原文）

> Visuomotor policies learned from demonstrations often overfit to nuisance visual factors in raw RGB observations, resulting in brittle behavior under appearance shifts such as background changes and object recoloring. We propose a task-aware observation interface that canonicalizes visual input into a shared representation, improving robustness to out-of-distribution (OOD) appearance changes without modifying or fine-tuning the policy. Given an RGB image and an open-vocabulary specification of task-relevant entities, we use SAM3 to segment the target object and robot/gripper. We construct an L0 observation by repainting segmented entities with predefined semantic colors on a constant background. For tasks requiring stronger geometric cues, we further inject monocular depth from Depth Anything 3 into the segmented regions via depth-guided overwrite, yielding a unified semantic--geometric observation (L1) that remains a standard 3-channel, image-like input. We evaluate on RoboMimic (Lift), ManiSkill YCB grasping under clutter, four RLBench tasks under controlled appearance shifts, and two real-world Franka tasks (ReachX and CloseCabinet). Across benchmarks and policy backbones (Flow Matching Policy and SmolVLA), our interface preserves in-distribution performance while substantially improving robustness under OOD visual shifts.

