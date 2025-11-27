---
layout: default
title: UAVLight: A Benchmark for Illumination-Robust 3D Reconstruction in Unmanned Aerial Vehicle (UAV) Scenes
---

# UAVLight: A Benchmark for Illumination-Robust 3D Reconstruction in Unmanned Aerial Vehicle (UAV) Scenes
**arXiv**：[2511.21565v1](https://arxiv.org/abs/2511.21565) · [PDF](https://arxiv.org/pdf/2511.21565.pdf)  
**作者**：Kang Du, Xue Liao, Junpeng Xia, Chaozheng Guo, Yi Gu, Yirui Guan, Duotun Wang, ShengHuang, Zeyu Wang  

**一句话要点**：提出UAVLight基准以解决无人机场景中光照不一致对3D重建的影响

**关键词**：无人机3D重建, 光照鲁棒性, 多视图立体, 基准数据集, 室外场景, 神经渲染

## 3 点简述
- 核心问题：光照变化破坏多视图3D重建的恒定光照假设，导致几何漂移和颜色不一致
- 方法要点：在重复飞行路径下多时段采集数据，确保几何一致并引入自然光照变化
- 实验或效果：提供标准化评估协议，支持开发光照鲁棒的重建方法

## 摘要（原文）

> Illumination inconsistency is a fundamental challenge in multi-view 3D reconstruction. Variations in sunlight direction, cloud cover, and shadows break the constant-lighting assumption underlying both classical multi-view stereo (MVS) and structure from motion (SfM) pipelines and recent neural rendering methods, leading to geometry drift, color inconsistency, and shadow imprinting. This issue is especially critical in UAV-based reconstruction, where long flight durations and outdoor environments make lighting changes unavoidable. However, existing datasets either restrict capture to short time windows, thus lacking meaningful illumination diversity, or span months and seasons, where geometric and semantic changes confound the isolated study of lighting robustness. We introduce UAVLight, a controlled-yet-real benchmark for illumination-robust 3D reconstruction. Each scene is captured along repeatable, geo-referenced flight paths at multiple fixed times of day, producing natural lighting variation under consistent geometry, calibration, and viewpoints. With standardized evaluation protocols across lighting conditions, UAVLight provides a reliable foundation for developing and benchmarking reconstruction methods that are consistent, faithful, and relightable in real outdoor environments.

