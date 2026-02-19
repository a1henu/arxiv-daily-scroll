---
layout: default
title: VETime: Vision Enhanced Zero-Shot Time Series Anomaly Detection
---

# VETime: Vision Enhanced Zero-Shot Time Series Anomaly Detection
**arXiv**：[2602.16681v1](https://arxiv.org/abs/2602.16681) · [PDF](https://arxiv.org/pdf/2602.16681.pdf)  
**作者**：Yingyuan Yang, Tian Lan, Yifei Gao, Yimeng Lu, Wenjun He, Meng Wang, Chenghao Liu, Chen Zhang  

**一句话要点**：提出VETime框架，通过视觉-时序对齐与融合解决零样本时间序列异常检测中的点与上下文异常识别难题。

**关键词**：时间序列异常检测, 零样本学习, 多模态融合, 视觉-时序对齐, 对比学习

## 3 点简述
- 核心问题：现有基础模型在时间序列异常检测中面临点异常定位与全局上下文感知的权衡，导致信息瓶颈。
- 方法要点：引入可逆图像转换和补丁级时序对齐模块，结合异常窗口对比学习和任务自适应多模态融合，统一视觉与时序模态。
- 实验或效果：在零样本场景下显著优于现有方法，实现高定位精度且计算开销低于视觉基方法。

## 摘要（原文）

> Time-series anomaly detection (TSAD) requires identifying both immediate Point Anomalies and long-range Context Anomalies. However, existing foundation models face a fundamental trade-off: 1D temporal models provide fine-grained pointwise localization but lack a global contextual perspective, while 2D vision-based models capture global patterns but suffer from information bottlenecks due to a lack of temporal alignment and coarse-grained pointwise detection. To resolve this dilemma, we propose VETime, the first TSAD framework that unifies temporal and visual modalities through fine-grained visual-temporal alignment and dynamic fusion. VETime introduces a Reversible Image Conversion and a Patch-Level Temporal Alignment module to establish a shared visual-temporal timeline, preserving discriminative details while maintaining temporal sensitivity. Furthermore, we design an Anomaly Window Contrastive Learning mechanism and a Task-Adaptive Multi-Modal Fusion to adaptively integrate the complementary perceptual strengths of both modalities. Extensive experiments demonstrate that VETime significantly outperforms state-of-the-art models in zero-shot scenarios, achieving superior localization precision with lower computational overhead than current vision-based approaches. Code available at: https://github.com/yyyangcoder/VETime.

