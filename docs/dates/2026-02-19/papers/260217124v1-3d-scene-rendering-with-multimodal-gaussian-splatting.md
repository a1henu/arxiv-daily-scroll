---
layout: default
title: 3D Scene Rendering with Multimodal Gaussian Splatting
---

# 3D Scene Rendering with Multimodal Gaussian Splatting
**arXiv**：[2602.17124v1](https://arxiv.org/abs/2602.17124) · [PDF](https://arxiv.org/pdf/2602.17124.pdf)  
**作者**：Chi-Shiang Gau, Konstantinos D. Polyzos, Athanasios Bacharis, Saketh Madhuvarasu, Tara Javidi  

**一句话要点**：提出多模态高斯泼溅框架，集成射频感知以增强恶劣条件下的3D场景渲染鲁棒性。

**关键词**：3D高斯泼溅, 多模态渲染, 射频感知, 场景重建, 鲁棒性增强

## 3 点简述
- 核心问题：传统视觉高斯泼溅依赖多视角图像，在恶劣天气、低光照或遮挡下渲染不可靠。
- 方法要点：结合射频信号（如汽车雷达）提供深度信息，高效初始化高斯函数，提升渲染鲁棒性。
- 实验或效果：数值测试显示，射频感知集成能提高结构准确性，实现高保真3D场景渲染。

## 摘要（原文）

> 3D scene reconstruction and rendering are core tasks in computer vision, with applications spanning industrial monitoring, robotics, and autonomous driving. Recent advances in 3D Gaussian Splatting (GS) and its variants have achieved impressive rendering fidelity while maintaining high computational and memory efficiency. However, conventional vision-based GS pipelines typically rely on a sufficient number of camera views to initialize the Gaussian primitives and train their parameters, typically incurring additional processing cost during initialization while falling short in conditions where visual cues are unreliable, such as adverse weather, low illumination, or partial occlusions. To cope with these challenges, and motivated by the robustness of radio-frequency (RF) signals to weather, lighting, and occlusions, we introduce a multimodal framework that integrates RF sensing, such as automotive radar, with GS-based rendering as a more efficient and robust alternative to vision-only GS rendering. The proposed approach enables efficient depth prediction from only sparse RF-based depth measurements, yielding a high-quality 3D point cloud for initializing Gaussian functions across diverse GS architectures. Numerical tests demonstrate the merits of judiciously incorporating RF sensing into GS pipelines, achieving high-fidelity 3D scene rendering driven by RF-informed structural accuracy.

