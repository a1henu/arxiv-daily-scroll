---
layout: default
title: Grasp to Act: Dexterous Grasping for Tool Use in Dynamic Settings
---

# Grasp to Act: Dexterous Grasping for Tool Use in Dynamic Settings
**arXiv**：[2602.20466v1](https://arxiv.org/abs/2602.20466) · [PDF](https://arxiv.org/pdf/2602.20466.pdf)  
**作者**：Harsh Gupta, Mohammad Amin Mirzaee, Wenzhen Yuan  

**一句话要点**：提出Grasp-to-Act系统，结合物理优化与强化学习，实现动态工具使用中的灵巧抓取稳定控制。

**关键词**：灵巧抓取, 动态工具使用, 强化学习控制, 仿真到现实迁移, 物理优化

## 3 点简述
- 核心问题：现有抓取方法在动态外力（如冲击、扭矩）下易失效，难以适应真实工具使用场景。
- 方法要点：融合基于物理的抓取优化和基于强化学习的自适应控制，通过人类演示生成配置并实时修正关节动作。
- 实验或效果：在五种动态任务中实现零样本仿真到现实迁移，减少滑移并提高任务完成率，优于基线方法。

## 摘要（原文）

> Achieving robust grasping with dexterous hands remains challenging, especially when manipulation involves dynamic forces such as impacts, torques, and continuous resistance--situations common in real-world tool use. Existing methods largely optimize grasps for static geometric stability and often fail once external forces arise during manipulation. We present Grasp-to-Act, a hybrid system that combines physics-based grasp optimization with reinforcement-learning-based grasp adaptation to maintain stable grasps throughout functional manipulation tasks. Our method synthesizes robust grasp configurations informed by human demonstrations and employs an adaptive controller that residually issues joint corrections to prevent in-hand slip while tracking the object trajectory. Grasp-to-Act enables robust zero-shot sim-to-real transfer across five dynamic tool-use tasks--hammering, sawing, cutting, stirring, and scooping--consistently outperforming baselines. Across simulation and real-world hardware trials with a 16-DoF dexterous hand, our method reduces translational and rotational in-hand slip and achieves the highest task completion rates, demonstrating stable functional grasps under dynamic, contact-rich conditions.

