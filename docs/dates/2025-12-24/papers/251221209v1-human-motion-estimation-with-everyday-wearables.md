---
layout: default
title: Human Motion Estimation with Everyday Wearables
---

# Human Motion Estimation with Everyday Wearables
**arXiv**：[2512.21209v1](https://arxiv.org/abs/2512.21209) · [PDF](https://arxiv.org/pdf/2512.21209.pdf)  
**作者**：Siqi Zhu, Yixuan Li, Junfu Li, Qi Wu, Zan Wang, Haozhe Ma, Wei Liang  

**一句话要点**：提出EveryWear方法，基于日常可穿戴设备实现轻量级人体运动估计，解决穿戴性差、硬件昂贵和校准繁琐问题。

**关键词**：人体运动估计, 日常可穿戴设备, 多模态学习, 师生框架, 真实世界数据集

## 3 点简述
- 核心问题：现有基于设备的人体运动估计方法存在穿戴性差、硬件昂贵和校准繁琐，限制日常应用。
- 方法要点：使用智能手机、智能手表、耳机和智能眼镜等多模态数据，采用师生框架整合视觉和惯性信号，无需显式校准。
- 实验或效果：在Ego-Elec数据集上实验，模型优于基线，有效消除模拟到现实的差距，验证了实用性。

## 摘要（原文）

> While on-body device-based human motion estimation is crucial for applications such as XR interaction, existing methods often suffer from poor wearability, expensive hardware, and cumbersome calibration, which hinder their adoption in daily life. To address these challenges, we present EveryWear, a lightweight and practical human motion capture approach based entirely on everyday wearables: a smartphone, smartwatch, earbuds, and smart glasses equipped with one forward-facing and two downward-facing cameras, requiring no explicit calibration before use. We introduce Ego-Elec, a 9-hour real-world dataset covering 56 daily activities across 17 diverse indoor and outdoor environments, with ground-truth 3D annotations provided by the motion capture (MoCap), to facilitate robust research and benchmarking in this direction. Our approach employs a multimodal teacher-student framework that integrates visual cues from egocentric cameras with inertial signals from consumer devices. By training directly on real-world data rather than synthetic data, our model effectively eliminates the sim-to-real gap that constrains prior work. Experiments demonstrate that our method outperforms baseline models, validating its effectiveness for practical full-body motion estimation.

