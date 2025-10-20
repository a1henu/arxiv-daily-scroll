---
layout: default
title: Towards Automated Chicken Deboning via Learning-based Dynamically-Adaptive 6-DoF Multi-Material Cutting
---

# Towards Automated Chicken Deboning via Learning-based Dynamically-Adaptive 6-DoF Multi-Material Cutting
**arXiv**：[2510.15376v1](https://arxiv.org/abs/2510.15376) · [PDF](https://arxiv.org/pdf/2510.15376.pdf)  
**作者**：Zhaodong Yang, Ai-Ping Hu, Harish Ravichandar  

**一句话要点**：提出基于力反馈的6自由度自适应切割策略，实现自动化鸡肩去骨。

**关键词**：多材料切割, 强化学习, 6自由度控制, 力反馈, 模拟到真实迁移, 机器人去骨

## 3 点简述
- 核心问题：鸡肩去骨需在遮挡、变形多材料关节中精确切割，避免骨接触风险。
- 方法要点：开发模拟器和物理测试台，训练残差强化学习策略，支持零样本迁移。
- 实验效果：策略在模拟、测试台和真实鸡肩中提升成功率，减少骨接触达4倍。

## 摘要（原文）

> Automating chicken shoulder deboning requires precise 6-DoF cutting through a
> partially occluded, deformable, multi-material joint, since contact with the
> bones presents serious health and safety risks. Our work makes both
> systems-level and algorithmic contributions to train and deploy a reactive
> force-feedback cutting policy that dynamically adapts a nominal trajectory and
> enables full 6-DoF knife control to traverse the narrow joint gap while
> avoiding contact with the bones. First, we introduce an open-source
> custom-built simulator for multi-material cutting that models coupling,
> fracture, and cutting forces, and supports reinforcement learning, enabling
> efficient training and rapid prototyping. Second, we design a reusable physical
> testbed to emulate the chicken shoulder: two rigid "bone" spheres with
> controllable pose embedded in a softer block, enabling rigorous and repeatable
> evaluation while preserving essential multi-material characteristics of the
> target problem. Third, we train and deploy a residual RL policy, with
> discretized force observations and domain randomization, enabling robust
> zero-shot sim-to-real transfer and the first demonstration of a learned policy
> that debones a real chicken shoulder. Our experiments in our simulator, on our
> physical testbed, and on real chicken shoulders show that our learned policy
> reliably navigates the joint gap and reduces undesired bone/cartilage contact,
> resulting in up to a 4x improvement over existing open-loop cutting baselines
> in terms of success rate and bone avoidance. Our results also illustrate the
> necessity of force feedback for safe and effective multi-material cutting. The
> project website is at https://sites.google.com/view/chickendeboning-2026.

