---
layout: default
title: Tether: Autonomous Functional Play with Correspondence-Driven Trajectory Warping
---

# Tether: Autonomous Functional Play with Correspondence-Driven Trajectory Warping
**arXiv**：[2603.03278v1](https://arxiv.org/abs/2603.03278) · [PDF](https://arxiv.org/pdf/2603.03278.pdf)  
**作者**：William Liang, Sam Wang, Hung-Ju Wang, Osbert Bastani, Yecheng Jason Ma, Dinesh Jayaraman  

**一句话要点**：提出Tether方法，通过对应驱动轨迹扭曲实现自主功能游戏，解决机器人交互学习中的数据效率和鲁棒性问题。

**关键词**：自主功能游戏, 轨迹扭曲, 语义关键点对应, 视觉语言模型, 数据高效学习, 机器人交互

## 3 点简述
- 核心问题：机器人自主交互学习需处理分布外状态并持续生成有用经验，传统方法依赖大量人工演示。
- 方法要点：设计开环策略，基于语义关键点对应扭曲源演示动作，结合视觉语言模型指导任务选择与改进循环。
- 实验或效果：在家庭多物体场景中，从少量演示启动，实现长时间自主多任务游戏，生成高质量数据提升闭环模仿策略性能。

## 摘要（原文）

> The ability to conduct and learn from interaction and experience is a central challenge in robotics, offering a scalable alternative to labor-intensive human demonstrations. However, realizing such "play" requires (1) a policy robust to diverse, potentially out-of-distribution environment states, and (2) a procedure that continuously produces useful robot experience. To address these challenges, we introduce Tether, a method for autonomous functional play involving structured, task-directed interactions. First, we design a novel open-loop policy that warps actions from a small set of source demonstrations (<=10) by anchoring them to semantic keypoint correspondences in the target scene. We show that this design is extremely data-efficient and robust even under significant spatial and semantic variations. Second, we deploy this policy for autonomous functional play in the real world via a continuous cycle of task selection, execution, evaluation, and improvement, guided by the visual understanding capabilities of vision-language models. This procedure generates diverse, high-quality datasets with minimal human intervention. In a household-like multi-object setup, our method is the first to perform many hours of autonomous multi-task play in the real world starting from only a handful of demonstrations. This produces a stream of data that consistently improves the performance of closed-loop imitation policies over time, ultimately yielding over 1000 expert-level trajectories and training policies competitive with those learned from human-collected demonstrations.

