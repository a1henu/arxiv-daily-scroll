---
layout: default
title: LiDAR Prompted Spatio-Temporal Multi-View Stereo for Autonomous Driving
---

# LiDAR Prompted Spatio-Temporal Multi-View Stereo for Autonomous Driving
**arXiv**：[2603.03765v1](https://arxiv.org/abs/2603.03765) · [PDF](https://arxiv.org/pdf/2603.03765.pdf)  
**作者**：Qihao Sun, Jiarun Liu, Ziqian Ni, Jianyun Xu, Tao Xie, Lijun Zhao, Ruifeng Li, Sheng Yang  

**一句话要点**：提出DriveMVS框架，利用LiDAR提示和时空解码器解决自动驾驶中多视角立体视觉的度量精度和一致性挑战。

**关键词**：多视角立体视觉, LiDAR提示, 时空一致性, 自动驾驶感知, 深度估计, 跨域泛化

## 3 点简述
- 核心问题：自动驾驶感知中多视角立体视觉的度量精度低、时空不一致和跨域泛化能力差。
- 方法要点：通过LiDAR作为几何提示锚定深度估计，结合三重线索融合和时空解码器提升鲁棒性和一致性。
- 实验或效果：在多个基准测试中达到最先进性能，展示高度量精度、时间稳定性和零样本跨域迁移能力。

## 摘要（原文）

> Accurate metric depth is critical for autonomous driving perception and simulation, yet current approaches struggle to achieve high metric accuracy, multi-view and temporal consistency, and cross-domain generalization. To address these challenges, we present DriveMVS, a novel multi-view stereo framework that reconciles these competing objectives through two key insights:
>   (1) Sparse but metrically accurate LiDAR observations can serve as geometric prompts to anchor depth estimation in absolute scale, and (2) deep fusion of diverse cues is essential for resolving ambiguities and enhancing robustness, while a spatio-temporal decoder ensures consistency across frames. Built upon these principles, DriveMVS embeds the LiDAR prompt in two ways: as a hard geometric prior that anchors the cost volume, and as soft feature-wise guidance fused by a triple-cue combiner. Regarding temporal consistency, DriveMVS employs a spatio-temporal decoder that jointly leverages geometric cues from the MVS cost volume and temporal context from neighboring frames. Experiments show that DriveMVS achieves state-of-the-art performance on multiple benchmarks, excelling in metric accuracy, temporal stability, and zero-shot cross-domain transfer, demonstrating its practical value for scalable, reliable autonomous driving systems.

