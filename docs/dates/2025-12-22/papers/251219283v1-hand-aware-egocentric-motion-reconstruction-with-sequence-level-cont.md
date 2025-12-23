---
layout: default
title: Hand-Aware Egocentric Motion Reconstruction with Sequence-Level Context
---

# Hand-Aware Egocentric Motion Reconstruction with Sequence-Level Context
**arXiv**：[2512.19283v1](https://arxiv.org/abs/2512.19283) · [PDF](https://arxiv.org/pdf/2512.19283.pdf)  
**作者**：Kyungwon Cho, Hanbyul Joo  

**一句话要点**：提出HaMoS框架，利用头轨迹和间歇手部线索解决第一人称视频中全身运动估计的模糊性问题。

**关键词**：第一人称运动重建, 手部感知, 扩散模型, 序列级上下文, 局部注意力, 数据增强

## 3 点简述
- 核心问题：第一人称视角下身体大部分不可见，现有方法依赖头轨迹或假设连续手部跟踪，导致运动估计不准确或不现实。
- 方法要点：基于扩散模型，结合头轨迹和间歇手部线索，引入序列级上下文如身体形状和视野，使用局部注意力高效推断长序列。
- 实验或效果：在公开基准测试中达到最先进精度和时间平滑度，提升野外第一人称3D运动理解的可靠性。

## 摘要（原文）

> Egocentric vision systems are becoming widely available, creating new opportunities for human-computer interaction. A core challenge is estimating the wearer's full-body motion from first-person videos, which is crucial for understanding human behavior. However, this task is difficult since most body parts are invisible from the egocentric view. Prior approaches mainly rely on head trajectories, leading to ambiguity, or assume continuously tracked hands, which is unrealistic for lightweight egocentric devices. In this work, we present HaMoS, the first hand-aware, sequence-level diffusion framework that directly conditions on both head trajectory and intermittently visible hand cues caused by field-of-view limitations and occlusions, as in real-world egocentric devices. To overcome the lack of datasets pairing diverse camera views with human motion, we introduce a novel augmentation method that models such real-world conditions. We also demonstrate that sequence-level contexts such as body shape and field-of-view are crucial for accurate motion reconstruction, and thus employ local attention to infer long sequences efficiently. Experiments on public benchmarks show that our method achieves state-of-the-art accuracy and temporal smoothness, demonstrating a practical step toward reliable in-the-wild egocentric 3D motion understanding.

