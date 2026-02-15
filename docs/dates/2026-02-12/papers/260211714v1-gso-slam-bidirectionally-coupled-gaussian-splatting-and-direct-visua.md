---
layout: default
title: GSO-SLAM: Bidirectionally Coupled Gaussian Splatting and Direct Visual Odometry
---

# GSO-SLAM: Bidirectionally Coupled Gaussian Splatting and Direct Visual Odometry
**arXiv**：[2602.11714v1](https://arxiv.org/abs/2602.11714) · [PDF](https://arxiv.org/pdf/2602.11714.pdf)  
**作者**：Jiung Yeon, Seongbo Ha, Hyeonwoo Yu  

**一句话要点**：提出GSO-SLAM，通过双向耦合视觉里程计与高斯泼溅实现实时单目稠密SLAM。

**关键词**：单目SLAM, 高斯泼溅, 视觉里程计, 期望最大化, 实时重建, 稠密建图

## 3 点简述
- 核心问题：现有SLAM方法在耦合跟踪与建图时存在计算成本高或冗余问题。
- 方法要点：在期望最大化框架下联合优化，同步精炼半稠密深度估计与高斯场景表示。
- 实验或效果：实时运行，在重建场景几何/光度保真度与跟踪精度上达到先进水平。

## 摘要（原文）

> We propose GSO-SLAM, a real-time monocular dense SLAM system that leverages Gaussian scene representation. Unlike existing methods that couple tracking and mapping with a unified scene, incurring computational costs, or loosely integrate them with well-structured tracking frameworks, introducing redundancies, our method bidirectionally couples Visual Odometry (VO) and Gaussian Splatting (GS). Specifically, our approach formulates joint optimization within an Expectation-Maximization (EM) framework, enabling the simultaneous refinement of VO-derived semi-dense depth estimates and the GS representation without additional computational overhead. Moreover, we present Gaussian Splat Initialization, which utilizes image information, keyframe poses, and pixel associations from VO to produce close approximations to the final Gaussian scene, thereby eliminating the need for heuristic methods. Through extensive experiments, we validate the effectiveness of our method, showing that it not only operates in real time but also achieves state-of-the-art geometric/photometric fidelity of the reconstructed scene and tracking accuracy.

