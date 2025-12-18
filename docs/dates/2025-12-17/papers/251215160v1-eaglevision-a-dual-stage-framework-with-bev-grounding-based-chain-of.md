---
layout: default
title: EagleVision: A Dual-Stage Framework with BEV-grounding-based Chain-of-Thought for Spatial Intelligence
---

# EagleVision: A Dual-Stage Framework with BEV-grounding-based Chain-of-Thought for Spatial Intelligence
**arXiv**：[2512.15160v1](https://arxiv.org/abs/2512.15160) · [PDF](https://arxiv.org/pdf/2512.15160.pdf)  
**作者**：Jiaxu Wan, Xu Wang, Mengwei Xie, Hang Zhang, Mu Xu, Yang Han, Hong Zhang, Ding Yuan, Yifan Yang  

**一句话要点**：提出EagleVision双阶段框架，通过BEV基础链式思维解决空间智能中的感知与验证问题

**关键词**：空间智能, 链式思维, 鸟瞰图基础, 强化学习, 长视频理解, 关键帧选择

## 3 点简述
- 核心问题：现有方法空间一致性弱、视角多样性有限，且证据链难以追溯至支持视图
- 方法要点：采用宏观感知阶段选择关键帧，微观验证阶段基于BEV进行姿态查询与强化学习训练
- 实验或效果：在VSI-Bench上达到开源视觉语言模型中的最佳性能，展示强泛化空间理解能力

## 摘要（原文）

> Recent spatial intelligence approaches typically attach 3D cues to 2D reasoning pipelines or couple MLLMs with black-box reconstruction modules, leading to weak spatial consistency, limited viewpoint diversity, and evidence chains that cannot be traced back to supporting views. Frameworks for "thinking with images" (e.g., ChatGPT-o3 and DeepEyes) show that stepwise multimodal reasoning can emerge by interleaving hypothesis formation with active acquisition of visual evidence, but they do not address three key challenges in spatial Chain-of-Thought (CoT): building global space perception under strict token budgets, explicitly associating 3D hypotheses with video frames for verification, and designing spatially grounded rewards for reinforcement learning. To address these issues, we present EagleVision, a dual-stage framework for progressive spatial cognition through macro perception and micro verification. In the macro perception stage, EagleVision employs a semantics-perspective-fusion determinantal point process (SPF-DPP) to select a compact set of geometry- and semantics-aware keyframes from long videos under a fixed token budget. In the micro verification stage, we formalize spatial CoT as BEV-grounded pose querying: the agent iteratively predicts poses on a BEV plane, retrieves the nearest real frames, and is trained purely by reinforcement learning with a spatial grounding reward that scores the consistency between predicted poses and observed views. On VSI-Bench, EagleVision achieves state-of-the-art performance among open-source vision-language models, demonstrating strong and generalizable spatial understanding.

