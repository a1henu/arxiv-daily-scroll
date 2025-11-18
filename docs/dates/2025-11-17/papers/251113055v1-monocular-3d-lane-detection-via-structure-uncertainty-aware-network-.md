---
layout: default
title: Monocular 3D Lane Detection via Structure Uncertainty-Aware Network with Curve-Point Queries
---

# Monocular 3D Lane Detection via Structure Uncertainty-Aware Network with Curve-Point Queries
**arXiv**：[2511.13055v1](https://arxiv.org/abs/2511.13055) · [PDF](https://arxiv.org/pdf/2511.13055.pdf)  
**作者**：Ruixin Liu, Zejian Yuan  

**一句话要点**：提出MonoUnc以解决单目3D车道检测中的结构不确定性问题

**关键词**：单目3D车道检测, 不确定性建模, 曲线点查询, 3D高斯匹配, 鸟瞰图无关, 评估指标

## 3 点简述
- 核心问题：单目3D车道检测存在观测噪声导致的不确定性，现有方法简化几何假设，无法捕捉真实场景结构变化。
- 方法要点：基于曲线点查询动态生成嵌入，建模3D高斯段以估计局部结构和不确定性。
- 实验或效果：在ONCE-3DLanes和OpenLane数据集上超越SoTA，并引入新评估指标量化全局和局部误差。

## 摘要（原文）

> Monocular 3D lane detection is challenged by aleatoric uncertainty arising from inherent observation noise. Existing methods rely on simplified geometric assumptions, such as independent point predictions or global planar modeling, failing to capture structural variations and aleatoric uncertainty in real-world scenarios. In this paper, we propose MonoUnc, a bird's-eye view (BEV)-free 3D lane detector that explicitly models aleatoric uncertainty informed by local lane structures. Specifically, 3D lanes are projected onto the front-view (FV) space and approximated by parametric curves. Guided by curve predictions, curve-point query embeddings are dynamically generated for lane point predictions in 3D space. Each segment formed by two adjacent points is modeled as a 3D Gaussian, parameterized by the local structure and uncertainty estimations. Accordingly, a novel 3D Gaussian matching loss is designed to constrain these parameters jointly. Experiments on the ONCE-3DLanes and OpenLane datasets demonstrate that MonoUnc outperforms previous state-of-the-art (SoTA) methods across all benchmarks under stricter evaluation criteria. Additionally, we propose two comprehensive evaluation metrics for ONCE-3DLanes, calculating the average and maximum bidirectional Chamfer distances to quantify global and local errors. Codes are released at https://github.com/lrx02/MonoUnc.

