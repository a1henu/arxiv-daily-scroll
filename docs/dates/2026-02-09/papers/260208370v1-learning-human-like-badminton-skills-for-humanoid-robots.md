---
layout: default
title: Learning Human-Like Badminton Skills for Humanoid Robots
---

# Learning Human-Like Badminton Skills for Humanoid Robots
**arXiv**：[2602.08370v1](https://arxiv.org/abs/2602.08370) · [PDF](https://arxiv.org/pdf/2602.08370.pdf)  
**作者**：Yeke Chen, Shihao Dong, Xiaoyu Ji, Jingkai Sun, Zeren Luo, Liu Zhao, Jiahui Zhang, Wanyue Li, Ji Ma, Bowen Xu, Yimin Han, Yudong Zhao, Peng Lu  

**一句话要点**：提出模仿到交互框架，实现人形机器人零样本模拟到真实羽毛球技能迁移

**关键词**：人形机器人, 模仿学习, 强化学习, 模拟到真实迁移, 羽毛球技能, 对抗先验

## 3 点简述
- 核心问题：人形机器人需在羽毛球等高要求运动中整合全身协调与精确击球，但现有方法难以兼顾运动模仿与物理感知功能。
- 方法要点：采用渐进强化学习，从人类数据建立运动先验，通过对抗先验稳定动力学，并引入流形扩展策略泛化击球点。
- 实验或效果：在仿真中掌握多种技能，并首次实现人形机器人零样本模拟到真实迁移，复现人类运动员的动感与精度。

## 摘要（原文）

> Realizing versatile and human-like performance in high-demand sports like badminton remains a formidable challenge for humanoid robotics. Unlike standard locomotion or static manipulation, this task demands a seamless integration of explosive whole-body coordination and precise, timing-critical interception. While recent advances have achieved lifelike motion mimicry, bridging the gap between kinematic imitation and functional, physics-aware striking without compromising stylistic naturalness is non-trivial. To address this, we propose Imitation-to-Interaction, a progressive reinforcement learning framework designed to evolve a robot from a "mimic" to a capable "striker." Our approach establishes a robust motor prior from human data, distills it into a compact, model-based state representation, and stabilizes dynamics via adversarial priors. Crucially, to overcome the sparsity of expert demonstrations, we introduce a manifold expansion strategy that generalizes discrete strike points into a dense interaction volume. We validate our framework through the mastery of diverse skills, including lifts and drop shots, in simulation. Furthermore, we demonstrate the first zero-shot sim-to-real transfer of anthropomorphic badminton skills to a humanoid robot, successfully replicating the kinetic elegance and functional precision of human athletes in the physical world.

