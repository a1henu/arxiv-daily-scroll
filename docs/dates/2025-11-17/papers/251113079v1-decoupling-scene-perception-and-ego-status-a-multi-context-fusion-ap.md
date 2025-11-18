---
layout: default
title: Decoupling Scene Perception and Ego Status: A Multi-Context Fusion Approach for Enhanced Generalization in End-to-End Autonomous Driving
---

# Decoupling Scene Perception and Ego Status: A Multi-Context Fusion Approach for Enhanced Generalization in End-to-End Autonomous Driving
**arXiv**：[2511.13079v1](https://arxiv.org/abs/2511.13079) · [PDF](https://arxiv.org/pdf/2511.13079.pdf)  
**作者**：Jiacheng Tang, Mingyue Feng, Jiachao Liu, Yaonong Wang, Jian Pu  

**一句话要点**：提出AdaptiveAD以解决端到端自动驾驶中过度依赖自车状态的问题

**关键词**：端到端自动驾驶, 场景感知解耦, 多上下文融合, BEV编码, 规划轨迹生成, 泛化能力

## 3 点简述
- 核心问题：现有架构中自车状态过早融合，导致规划模块过度依赖此捷径，影响泛化能力。
- 方法要点：采用双分支结构解耦场景感知与自车状态，并通过场景感知融合模块自适应整合决策。
- 实验或效果：在nuScenes数据集上实现最优开环规划性能，显著提升泛化能力。

## 摘要（原文）

> Modular design of planning-oriented autonomous driving has markedly advanced end-to-end systems. However, existing architectures remain constrained by an over-reliance on ego status, hindering generalization and robust scene understanding. We identify the root cause as an inherent design within these architectures that allows ego status to be easily leveraged as a shortcut. Specifically, the premature fusion of ego status in the upstream BEV encoder allows an information flow from this strong prior to dominate the downstream planning module. To address this challenge, we propose AdaptiveAD, an architectural-level solution based on a multi-context fusion strategy. Its core is a dual-branch structure that explicitly decouples scene perception and ego status. One branch performs scene-driven reasoning based on multi-task learning, but with ego status deliberately omitted from the BEV encoder, while the other conducts ego-driven reasoning based solely on the planning task. A scene-aware fusion module then adaptively integrates the complementary decisions from the two branches to form the final planning trajectory. To ensure this decoupling does not compromise multi-task learning, we introduce a path attention mechanism for ego-BEV interaction and add two targeted auxiliary tasks: BEV unidirectional distillation and autoregressive online mapping. Extensive evaluations on the nuScenes dataset demonstrate that AdaptiveAD achieves state-of-the-art open-loop planning performance. Crucially, it significantly mitigates the over-reliance on ego status and exhibits impressive generalization capabilities across diverse scenarios.

