---
layout: default
title: Space Object Detection using Multi-frame Temporal Trajectory Completion Method
---

# Space Object Detection using Multi-frame Temporal Trajectory Completion Method
**arXiv**：[2510.19220v1](https://arxiv.org/abs/2510.19220) · [PDF](https://arxiv.org/pdf/2510.19220.pdf)  
**作者**：Xiaoqing Lan, Biqiao Xin, Bingshu Wang, Han Zhang, Laixian Zhang  

**一句话要点**：提出多帧时序轨迹补全方法以解决GEO空间目标检测中的弱信号和背景干扰问题

**关键词**：空间目标检测, 多帧时序分析, 轨迹补全, 小波变换, 匈牙利算法, 后处理优化

## 3 点简述
- 核心问题：GEO空间目标在光学成像中信号弱、背景复杂，检测困难。
- 方法要点：使用小波变换增强目标特征，匈牙利算法进行跨帧匹配，后处理优化轨迹。
- 实验或效果：在SpotGEO数据集上F1分数达90.14%，验证方法有效性。

## 摘要（原文）

> Space objects in Geostationary Earth Orbit (GEO) present significant
> detection challenges in optical imaging due to weak signals, complex stellar
> backgrounds, and environmental interference. In this paper, we enhance
> high-frequency features of GEO targets while suppressing background noise at
> the single-frame level through wavelet transform. Building on this, we propose
> a multi-frame temporal trajectory completion scheme centered on the Hungarian
> algorithm for globally optimal cross-frame matching. To effectively mitigate
> missing and false detections, a series of key steps including temporal matching
> and interpolation completion, temporal-consistency-based noise filtering, and
> progressive trajectory refinement are designed in the post-processing pipeline.
> Experimental results on the public SpotGEO dataset demonstrate the
> effectiveness of the proposed method, achieving an F_1 score of 90.14%.

