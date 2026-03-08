---
layout: default
title: EdgeDAM: Real-time Object Tracking for Mobile Devices
---

# EdgeDAM: Real-time Object Tracking for Mobile Devices
**arXiv**：[2603.05463v1](https://arxiv.org/abs/2603.05463) · [PDF](https://arxiv.org/pdf/2603.05463.pdf)  
**作者**：Syed Muhammad Raza, Syed Murtaza Hussain Abidi, Khawar Islam, Muhammad Ibrahim, Ajmal Saeed Mian  

**一句话要点**：提出EdgeDAM轻量检测引导跟踪框架，解决移动设备上单目标跟踪在遮挡和干扰下的实时性问题。

**关键词**：单目标跟踪, 移动设备, 干扰感知内存, 实时跟踪, 边界框跟踪, 轻量框架

## 3 点简述
- 核心问题：现有基于分割的干扰感知内存机制计算开销大，轻量跟踪器在视觉相似干扰下易漂移。
- 方法要点：引入双缓冲干扰感知内存和置信驱动切换机制，优化边界框跟踪。
- 实验或效果：在DiDi数据集上达到88.2%准确率，iPhone 15上实现25 FPS实时性能。

## 摘要（原文）

> Single-object tracking (SOT) on edge devices is a critical computer vision task, requiring accurate and continuous target localization across video frames under occlusion, distractor interference, and fast motion. However, recent state-of-the-art distractor-aware memory mechanisms are largely built on segmentation-based trackers and rely on mask prediction and attention-driven memory updates, which introduce substantial computational overhead and limit real-time deployment on resource-constrained hardware; meanwhile, lightweight trackers sustain high throughput but are prone to drift when visually similar distractors appear. To address these challenges, we propose EdgeDAM, a lightweight detection-guided tracking framework that reformulates distractor-aware memory for bounding-box tracking under strict edge constraints. EdgeDAM introduces two key strategies: (1) Dual-Buffer Distractor-Aware Memory (DAM), which integrates a Recent-Aware Memory to preserve temporally consistent target hypotheses and a Distractor-Resolving Memory to explicitly store hard negative candidates and penalize their re-selection during recovery; and (2) Confidence-Driven Switching with Held-Box Stabilization, where tracker reliability and temporal consistency criteria adaptively activate detection and memory-guided re-identification during occlusion, while a held-box mechanism temporarily freezes and expands the estimate to suppress distractor contamination. Extensive experiments on five benchmarks, including the distractor-focused DiDi dataset, demonstrate improved robustness under occlusion and fast motion while maintaining real-time performance on mobile devices, achieving 88.2% accuracy on DiDi and 25 FPS on an iPhone 15. Code will be released.

