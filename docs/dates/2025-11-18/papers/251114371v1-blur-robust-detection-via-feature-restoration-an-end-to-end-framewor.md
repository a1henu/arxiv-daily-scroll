---
layout: default
title: Blur-Robust Detection via Feature Restoration: An End-to-End Framework for Prior-Guided Infrared UAV Target Detection
---

# Blur-Robust Detection via Feature Restoration: An End-to-End Framework for Prior-Guided Infrared UAV Target Detection
**arXiv**：[2511.14371v1](https://arxiv.org/abs/2511.14371) · [PDF](https://arxiv.org/pdf/2511.14371.pdf)  
**作者**：Xiaolin Wang, Houzhang Fang, Qingshan Li, Lu Wang, Yi Chang, Luxin Yan  

**一句话要点**：提出JFD3框架以解决红外无人机图像运动模糊下的目标检测问题

**关键词**：红外目标检测, 运动模糊处理, 特征恢复, 双分支架构, 无人机图像, 端到端学习

## 3 点简述
- 红外无人机图像因运动模糊导致目标与背景对比度降低，影响检测性能
- 采用双分支架构，清晰分支指导模糊分支恢复特征，增强检测相关特征表示
- 在IRBlurUAV基准上实验，JFD3实现优越检测性能并保持实时效率

## 摘要（原文）

> Infrared unmanned aerial vehicle (UAV) target images often suffer from motion blur degradation caused by rapid sensor movement, significantly reducing contrast between target and background. Generally, detection performance heavily depends on the discriminative feature representation between target and background. Existing methods typically treat deblurring as a preprocessing step focused on visual quality, while neglecting the enhancement of task-relevant features crucial for detection. Improving feature representation for detection under blur conditions remains challenging. In this paper, we propose a novel Joint Feature-Domain Deblurring and Detection end-to-end framework, dubbed JFD3. We design a dual-branch architecture with shared weights, where the clear branch guides the blurred branch to enhance discriminative feature representation. Specifically, we first introduce a lightweight feature restoration network, where features from the clear branch serve as feature-level supervision to guide the blurred branch, thereby enhancing its distinctive capability for detection. We then propose a frequency structure guidance module that refines the structure prior from the restoration network and integrates it into shallow detection layers to enrich target structural information. Finally, a feature consistency self-supervised loss is imposed between the dual-branch detection backbones, driving the blurred branch to approximate the feature representations of the clear one. Wealso construct a benchmark, named IRBlurUAV, containing 30,000 simulated and 4,118 real infrared UAV target images with diverse motion blur. Extensive experiments on IRBlurUAV demonstrate that JFD3 achieves superior detection performance while maintaining real-time efficiency.

