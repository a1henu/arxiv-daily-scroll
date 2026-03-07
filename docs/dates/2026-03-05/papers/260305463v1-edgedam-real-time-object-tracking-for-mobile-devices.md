---
layout: default
title: EdgeDAM: Real-time Object Tracking for Mobile Devices
---

# EdgeDAM: Real-time Object Tracking for Mobile Devices
**arXiv**：[2603.05463v1](https://arxiv.org/abs/2603.05463) · [PDF](https://arxiv.org/pdf/2603.05463.pdf)  
**作者**：Syed Muhammad Raza, Syed Murtaza Hussain Abidi, Khawar Islam, Muhammad Ibrahim, Ajmal Saeed Mian  

**一句话要点**：提出EdgeDAM轻量检测引导跟踪框架，以解决移动设备上单目标跟踪在遮挡和干扰下的实时鲁棒性问题。

**关键词**：单目标跟踪, 移动设备跟踪, 干扰感知内存, 轻量跟踪框架, 实时性能, 检测引导跟踪

## 3 点简述
- 核心问题：现有干扰感知内存机制计算开销大，轻量跟踪器易受视觉相似干扰物影响，难以在资源受限设备上实现实时鲁棒跟踪。
- 方法要点：引入双缓冲干扰感知内存，结合最近感知内存和干扰解析内存，以及置信度驱动切换与保持框稳定机制，自适应激活检测和内存引导重识别。
- 实验或效果：在DiDi等五个基准测试中，提升遮挡和快速运动下的鲁棒性，在iPhone 15上达到25 FPS实时性能，DiDi数据集准确率88.2%。

## 摘要（原文）

> Single-object tracking (SOT) on edge devices is a critical computer vision task, requiring accurate and continuous target localization across video frames under occlusion, distractor interference, and fast motion. However, recent state-of-the-art distractor-aware memory mechanisms are largely built on segmentation-based trackers and rely on mask prediction and attention-driven memory updates, which introduce substantial computational overhead and limit real-time deployment on resource-constrained hardware; meanwhile, lightweight trackers sustain high throughput but are prone to drift when visually similar distractors appear. To address these challenges, we propose EdgeDAM, a lightweight detection-guided tracking framework that reformulates distractor-aware memory for bounding-box tracking under strict edge constraints. EdgeDAM introduces two key strategies: (1) Dual-Buffer Distractor-Aware Memory (DAM), which integrates a Recent-Aware Memory to preserve temporally consistent target hypotheses and a Distractor-Resolving Memory to explicitly store hard negative candidates and penalize their re-selection during recovery; and (2) Confidence-Driven Switching with Held-Box Stabilization, where tracker reliability and temporal consistency criteria adaptively activate detection and memory-guided re-identification during occlusion, while a held-box mechanism temporarily freezes and expands the estimate to suppress distractor contamination. Extensive experiments on five benchmarks, including the distractor-focused DiDi dataset, demonstrate improved robustness under occlusion and fast motion while maintaining real-time performance on mobile devices, achieving 88.2% accuracy on DiDi and 25 FPS on an iPhone 15. Code will be released.

