---
layout: default
title: 3D Scene Rendering with Multimodal Gaussian Splatting
---

# 3D Scene Rendering with Multimodal Gaussian Splatting
**arXiv**：[2602.17124v1](https://arxiv.org/abs/2602.17124) · [PDF](https://arxiv.org/pdf/2602.17124.pdf)  
**作者**：Chi-Shiang Gau, Konstantinos D. Polyzos, Athanasios Bacharis, Saketh Madhuvarasu, Tara Javidi  

**一句话要点**：提出融合射频传感与高斯泼溅的多模态框架，以提升恶劣条件下的3D场景渲染鲁棒性。

**关键词**：3D高斯泼溅, 多模态渲染, 射频传感, 场景重建, 鲁棒深度预测

## 3 点简述
- 传统视觉高斯泼溅依赖多视角初始化，在恶劣天气或遮挡下性能受限。
- 集成射频传感（如车载雷达）提供鲁棒深度测量，高效生成点云初始化高斯函数。
- 实验验证射频增强的高斯泼溅在结构精度和渲染保真度方面优于纯视觉方法。

## 摘要（原文）

> 3D scene reconstruction and rendering are core tasks in computer vision, with applications spanning industrial monitoring, robotics, and autonomous driving. Recent advances in 3D Gaussian Splatting (GS) and its variants have achieved impressive rendering fidelity while maintaining high computational and memory efficiency. However, conventional vision-based GS pipelines typically rely on a sufficient number of camera views to initialize the Gaussian primitives and train their parameters, typically incurring additional processing cost during initialization while falling short in conditions where visual cues are unreliable, such as adverse weather, low illumination, or partial occlusions. To cope with these challenges, and motivated by the robustness of radio-frequency (RF) signals to weather, lighting, and occlusions, we introduce a multimodal framework that integrates RF sensing, such as automotive radar, with GS-based rendering as a more efficient and robust alternative to vision-only GS rendering. The proposed approach enables efficient depth prediction from only sparse RF-based depth measurements, yielding a high-quality 3D point cloud for initializing Gaussian functions across diverse GS architectures. Numerical tests demonstrate the merits of judiciously incorporating RF sensing into GS pipelines, achieving high-fidelity 3D scene rendering driven by RF-informed structural accuracy.

