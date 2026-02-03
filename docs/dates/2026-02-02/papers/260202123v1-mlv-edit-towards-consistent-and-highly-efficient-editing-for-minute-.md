---
layout: default
title: MLV-Edit: Towards Consistent and Highly Efficient Editing for Minute-Level Videos
---

# MLV-Edit: Towards Consistent and Highly Efficient Editing for Minute-Level Videos
**arXiv**：[2602.02123v1](https://arxiv.org/abs/2602.02123) · [PDF](https://arxiv.org/pdf/2602.02123.pdf)  
**作者**：Yangyi Cao, Yuanhang Li, Lan Chen, Qi Mao  

**一句话要点**：提出MLV-Edit框架，以解决分钟级视频编辑中的计算开销和时序一致性问题。

**关键词**：分钟级视频编辑, 时序一致性, 分治策略, 运动校正, 结构漂移抑制, 训练免费框架

## 3 点简述
- 核心问题：现有方法难以扩展到长视频，因计算开销大且难以保持全局时序一致性。
- 方法要点：采用分治策略，结合Velocity Blend模块校正运动不一致，Attention Sink模块抑制结构漂移。
- 实验或效果：实验表明MLV-Edit在时序稳定性和语义保真度上优于现有方法。

## 摘要（原文）

> We propose MLV-Edit, a training-free, flow-based framework that address the unique challenges of minute-level video editing. While existing techniques excel in short-form video manipulation, scaling them to long-duration videos remains challenging due to prohibitive computational overhead and the difficulty of maintaining global temporal consistency across thousands of frames. To address this, MLV-Edit employs a divide-and-conquer strategy for segment-wise editing, facilitated by two core modules: Velocity Blend rectifies motion inconsistencies at segment boundaries by aligning the flow fields of adjacent chunks, eliminating flickering and boundary artifacts commonly observed in fragmented video processing; and Attention Sink anchors local segment features to global reference frames, effectively suppressing cumulative structural drift. Extensive quantitative and qualitative experiments demonstrate that MLV-Edit consistently outperforms state-of-the-art methods in terms of temporal stability and semantic fidelity.

