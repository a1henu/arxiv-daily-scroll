---
layout: default
title: PRAM-R: A Perception-Reasoning-Action-Memory Framework with LLM-Guided Modality Routing for Adaptive Autonomous Driving
---

# PRAM-R: A Perception-Reasoning-Action-Memory Framework with LLM-Guided Modality Routing for Adaptive Autonomous Driving
**arXiv**：[2603.04222v1](https://arxiv.org/abs/2603.04222) · [PDF](https://arxiv.org/pdf/2603.04222.pdf)  
**作者**：Yi Zhang, Xian Zhang, Saisi Zhao, Yinglei Song, Chengdong Wu, Nenad Petrovic, Alois Knoll  

**一句话要点**：提出PRAM-R框架，通过LLM引导模态路由实现自适应自动驾驶，以降低计算成本。

**关键词**：自动驾驶, 多模态感知, 模态路由, LLM引导, 分层记忆, 自适应系统

## 3 点简述
- 核心问题：多模态感知在自动驾驶中计算成本高，所有传感器持续活动不必要。
- 方法要点：采用异步双循环设计，LLM路由器基于环境上下文选择模态，分层记忆模块保持时间一致性。
- 实验或效果：在nuScenes数据集上验证，模态减少6.22%，轨迹精度与全模态基线相当。

## 摘要（原文）

> Multimodal perception enables robust autonomous driving but incurs unnecessary computational cost when all sensors remain active. This paper presents PRAM-R, a unified Perception-Reasoning-Action-Memory framework with LLM-Guided Modality Routing for adaptive autonomous driving. PRAM-R adopts an asynchronous dual-loop design: a fast reactive loop for perception and control, and a slow deliberative loop for reasoning-driven modality selection and memory updates. An LLM router selects and weights modalities using environmental context and sensor diagnostics, while a hierarchical memory module preserves temporal consistency and supports long-term adaptation. We conduct a two-stage evaluation: (1) synthetic stress tests for stability analysis and (2) real-world validation on the nuScenes dataset. Synthetic stress tests confirm 87.2% reduction in routing oscillations via hysteresis-based stabilization. Real-world validation on nuScenes shows 6.22% modality reduction with 20% memory recall while maintaining comparable trajectory accuracy to full-modality baselines in complex urban scenarios. Our work demonstrates that LLM-augmented architectures with hierarchical memory achieve efficient, adaptive multimodal perception in autonomous driving.

