---
layout: default
title: OpenFrontier: General Navigation with Visual-Language Grounded Frontiers
---

# OpenFrontier: General Navigation with Visual-Language Grounded Frontiers
**arXiv**：[2603.05377v1](https://arxiv.org/abs/2603.05377) · [PDF](https://arxiv.org/pdf/2603.05377.pdf)  
**作者**：Esteban Padilla, Boyang Sun, Marc Pollefeys, Hermann Blum  

**一句话要点**：提出OpenFrontier框架，以视觉-语言锚定前沿实现零训练开放世界导航

**关键词**：开放世界导航, 视觉-语言导航, 零样本学习, 稀疏子目标识别, 前沿锚定, 移动机器人

## 3 点简述
- 核心问题：传统导航依赖密集3D重建和手工目标度量，泛化能力受限
- 方法要点：将导航视为稀疏子目标识别问题，利用视觉-语言先验模型锚定前沿作为语义目标
- 实验或效果：在多个基准测试中展示强零样本性能，并在移动机器人上有效部署

## 摘要（原文）

> Open-world navigation requires robots to make decisions in complex everyday environments while adapting to flexible task requirements. Conventional navigation approaches often rely on dense 3D reconstruction and hand-crafted goal metrics, which limits their generalization across tasks and environments. Recent advances in vision--language navigation (VLN) and vision--language--action (VLA) models enable end-to-end policies conditioned on natural language, but typically require interactive training, large-scale data collection, or task-specific fine-tuning with a mobile agent. We formulate navigation as a sparse subgoal identification and reaching problem and observe that providing visual anchoring targets for high-level semantic priors enables highly efficient goal-conditioned navigation. Based on this insight, we select navigation frontiers as semantic anchors and propose OpenFrontier, a training-free navigation framework that seamlessly integrates diverse vision--language prior models. OpenFrontier enables efficient navigation with a lightweight system design, without dense 3D mapping, policy training, or model fine-tuning. We evaluate OpenFrontier across multiple navigation benchmarks and demonstrate strong zero-shot performance, as well as effective real-world deployment on a mobile robot.

