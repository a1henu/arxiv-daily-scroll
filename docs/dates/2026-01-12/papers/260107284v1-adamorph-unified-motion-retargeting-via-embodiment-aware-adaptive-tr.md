---
layout: default
title: AdaMorph: Unified Motion Retargeting via Embodiment-Aware Adaptive Transformers
---

# AdaMorph: Unified Motion Retargeting via Embodiment-Aware Adaptive Transformers
**arXiv**：[2601.07284v1](https://arxiv.org/abs/2601.07284) · [PDF](https://arxiv.org/pdf/2601.07284.pdf)  
**作者**：Haoyu Zhang, Shibo Jin, Lvsong Li, Jun Li, Liang Lin, Xiaodong He, Zecui Zeng  

**一句话要点**：提出AdaMorph框架，通过自适应变换器统一将人类运动重定向到异构机器人

**关键词**：运动重定向, 自适应变换器, 条件生成, 机器人控制, 零样本泛化

## 3 点简述
- 核心问题：异构机器人间运动重定向因运动学和动力学差异而困难，现有方法需训练特定模型，扩展性差
- 方法要点：将重定向视为条件生成任务，使用自适应层归一化动态调制特征空间，确保物理合理性
- 实验或效果：在12个人形机器人上验证，实现零样本泛化，保持运动动态本质

## 摘要（原文）

> Retargeting human motion to heterogeneous robots is a fundamental challenge in robotics, primarily due to the severe kinematic and dynamic discrepancies between varying embodiments. Existing solutions typically resort to training embodiment-specific models, which scales poorly and fails to exploit shared motion semantics. To address this, we present AdaMorph, a unified neural retargeting framework that enables a single model to adapt human motion to diverse robot morphologies. Our approach treats retargeting as a conditional generation task. We map human motion into a morphology-agnostic latent intent space and utilize a dual-purpose prompting mechanism to condition the generation. Instead of simple input concatenation, we leverage Adaptive Layer Normalization (AdaLN) to dynamically modulate the decoder's feature space based on embodiment constraints. Furthermore, we enforce physical plausibility through a curriculum-based training objective that ensures orientation and trajectory consistency via integration. Experimental results on 12 distinct humanoid robots demonstrate that AdaMorph effectively unifies control across heterogeneous topologies, exhibiting strong zero-shot generalization to unseen complex motions while preserving the dynamic essence of the source behaviors.

