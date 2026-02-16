---
layout: default
title: X-VORTEX: Spatio-Temporal Contrastive Learning for Wake Vortex Trajectory Forecasting
---

# X-VORTEX: Spatio-Temporal Contrastive Learning for Wake Vortex Trajectory Forecasting
**arXiv**：[2602.12869v1](https://arxiv.org/abs/2602.12869) · [PDF](https://arxiv.org/pdf/2602.12869.pdf)  
**作者**：Zhan Qu, Michael Färber  

**一句话要点**：提出X-VORTEX时空对比学习框架，以解决LiDAR点云序列中尾涡轨迹预测的稀疏性和动态性问题。

**关键词**：时空对比学习, 尾涡轨迹预测, LiDAR点云序列, 增强重叠理论, 物理感知表示, 稀疏传感器数据

## 3 点简述
- 核心问题：LiDAR扫描稀疏、尾涡特征随时间衰减，点级标注成本高，现有方法忽略时间结构。
- 方法要点：基于增强重叠理论，通过弱扰动和强增强序列对，学习物理感知表示，结合几何编码器和序列聚合器。
- 实验或效果：在百万级LiDAR扫描数据集上，仅用1%标注数据实现优于监督基线的尾涡中心定位和轨迹预测。

## 摘要（原文）

> Wake vortices are strong, coherent air turbulences created by aircraft, and they pose a major safety and capacity challenge for air traffic management. Tracking how vortices move, weaken, and dissipate over time from LiDAR measurements is still difficult because scans are sparse, vortex signatures fade as the flow breaks down under atmospheric turbulence and instabilities, and point-wise annotation is prohibitively expensive. Existing approaches largely treat each scan as an independent, fully supervised segmentation problem, which overlooks temporal structure and does not scale to the vast unlabeled archives collected in practice. We present X-VORTEX, a spatio-temporal contrastive learning framework grounded in Augmentation Overlap Theory that learns physics-aware representations from unlabeled LiDAR point cloud sequences. X-VORTEX addresses two core challenges: sensor sparsity and time-varying vortex dynamics. It constructs paired inputs from the same underlying flight event by combining a weakly perturbed sequence with a strongly augmented counterpart produced via temporal subsampling and spatial masking, encouraging the model to align representations across missing frames and partial observations. Architecturally, a time-distributed geometric encoder extracts per-scan features and a sequential aggregator models the evolving vortex state across variable-length sequences. We evaluate on a real-world dataset of over one million LiDAR scans. X-VORTEX achieves superior vortex center localization while using only 1% of the labeled data required by supervised baselines, and the learned representations support accurate trajectory forecasting.

