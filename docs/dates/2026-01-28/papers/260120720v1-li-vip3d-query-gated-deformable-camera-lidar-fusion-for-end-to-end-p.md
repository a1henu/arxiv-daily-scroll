---
layout: default
title: Li-ViP3D++: Query-Gated Deformable Camera-LiDAR Fusion for End-to-End Perception and Trajectory Prediction
---

# Li-ViP3D++: Query-Gated Deformable Camera-LiDAR Fusion for End-to-End Perception and Trajectory Prediction
**arXiv**：[2601.20720v1](https://arxiv.org/abs/2601.20720) · [PDF](https://arxiv.org/pdf/2601.20720.pdf)  
**作者**：Matej Halinkovic, Nina Masarykova, Alexey Vinel, Marek Galinski  

**一句话要点**：提出Li-ViP3D++，通过查询门控可变形融合实现端到端感知与轨迹预测，提升自动驾驶性能。

**关键词**：端到端感知预测, 相机-LiDAR融合, 查询门控融合, 自动驾驶, 轨迹预测, 可变形注意力

## 3 点简述
- 核心问题：现有模块化感知预测模型信息流受限，相机与LiDAR融合常依赖启发式对齐，导致信息利用不足和偏差。
- 方法要点：引入查询门控可变形融合，在查询空间自适应加权视觉与几何线索，实现端到端检测、跟踪和轨迹预测。
- 实验或效果：在nuScenes数据集上，提升EPA和mAP，减少误报，运行速度优于前代模型。

## 摘要（原文）

> End-to-end perception and trajectory prediction from raw sensor data is one of the key capabilities for autonomous driving. Modular pipelines restrict information flow and can amplify upstream errors. Recent query-based, fully differentiable perception-and-prediction (PnP) models mitigate these issues, yet the complementarity of cameras and LiDAR in the query-space has not been sufficiently explored. Models often rely on fusion schemes that introduce heuristic alignment and discrete selection steps which prevent full utilization of available information and can introduce unwanted bias. We propose Li-ViP3D++, a query-based multimodal PnP framework that introduces Query-Gated Deformable Fusion (QGDF) to integrate multi-view RGB and LiDAR in query space. QGDF (i) aggregates image evidence via masked attention across cameras and feature levels, (ii) extracts LiDAR context through fully differentiable BEV sampling with learned per-query offsets, and (iii) applies query-conditioned gating to adaptively weight visual and geometric cues per agent. The resulting architecture jointly optimizes detection, tracking, and multi-hypothesis trajectory forecasting in a single end-to-end model. On nuScenes, Li-ViP3D++ improves end-to-end behavior and detection quality, achieving higher EPA (0.335) and mAP (0.502) while substantially reducing false positives (FP ratio 0.147), and it is faster than the prior Li-ViP3D variant (139.82 ms vs. 145.91 ms). These results indicate that query-space, fully differentiable camera-LiDAR fusion can increase robustness of end-to-end PnP without sacrificing deployability.

