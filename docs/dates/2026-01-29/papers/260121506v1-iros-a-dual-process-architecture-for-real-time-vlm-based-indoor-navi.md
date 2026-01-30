---
layout: default
title: IROS: A Dual-Process Architecture for Real-Time VLM-Based Indoor Navigation
---

# IROS: A Dual-Process Architecture for Real-Time VLM-Based Indoor Navigation
**arXiv**：[2601.21506v1](https://arxiv.org/abs/2601.21506) · [PDF](https://arxiv.org/pdf/2601.21506.pdf)  
**作者**：Joonhee Lee, Hyunseung Shin, Jeonggil Ko  

**一句话要点**：提出IROS双进程架构，结合VLM推理与轻量模块，实现低成本硬件的实时室内导航。

**关键词**：室内导航, 视觉语言模型, 双过程架构, 实时系统, 语义理解, 低成本硬件

## 3 点简述
- 核心问题：现有室内导航方法难以兼顾实时响应与语义理解，VLM计算延迟高。
- 方法要点：基于双过程理论，分离快速反射决策与慢速深思推理，仅在必要时调用VLM。
- 实验或效果：在五个真实建筑中，相比连续VLM导航，决策准确率提升，延迟降低66%。

## 摘要（原文）

> Indoor mobile robot navigation requires fast responsiveness and robust semantic understanding, yet existing methods struggle to provide both. Classical geometric approaches such as SLAM offer reliable localization but depend on detailed maps and cannot interpret human-targeted cues (e.g., signs, room numbers) essential for indoor reasoning. Vision-Language-Action (VLA) models introduce semantic grounding but remain strictly reactive, basing decisions only on visible frames and failing to anticipate unseen intersections or reason about distant textual cues. Vision-Language Models (VLMs) provide richer contextual inference but suffer from high computational latency, making them unsuitable for real-time operation on embedded platforms. In this work, we present IROS, a real-time navigation framework that combines VLM-level contextual reasoning with the efficiency of lightweight perceptual modules on low-cost, on-device hardware. Inspired by Dual Process Theory, IROS separates fast reflexive decisions (System One) from slow deliberative reasoning (System Two), invoking the VLM only when necessary. Furthermore, by augmenting compact VLMs with spatial and textual cues, IROS delivers robust, human-like navigation with minimal latency. Across five real-world buildings, IROS improves decision accuracy and reduces latency by 66% compared to continuous VLM-based navigation.

