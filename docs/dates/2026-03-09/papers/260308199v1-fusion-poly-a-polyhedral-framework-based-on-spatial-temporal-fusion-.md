---
layout: default
title: Fusion-Poly: A Polyhedral Framework Based on Spatial-Temporal Fusion for 3D Multi-Object Tracking
---

# Fusion-Poly: A Polyhedral Framework Based on Spatial-Temporal Fusion for 3D Multi-Object Tracking
**arXiv**：[2603.08199v1](https://arxiv.org/abs/2603.08199) · [PDF](https://arxiv.org/pdf/2603.08199.pdf)  
**作者**：Xian Wu, Yitao Wu, Xiaoyu Li, Zijia Li, Lijun Zhao, Lining Sun  

**一句话要点**：提出Fusion-Poly框架，通过时空融合处理异步LiDAR-相机数据以提升3D多目标跟踪性能

**关键词**：3D多目标跟踪, 传感器融合, 异步数据处理, 轨迹估计, LiDAR-相机融合

## 3 点简述
- 核心问题：现有方法在同步时间戳进行空间融合，未充分利用异步传感器数据，限制跟踪频率和鲁棒性
- 方法要点：设计频率感知级联匹配、轨迹估计和全状态观测对齐模块，整合同步和异步观测
- 实验或效果：在nuScenes测试集上达到76.5% AMOTA，创下检测跟踪方法新纪录

## 摘要（原文）

> LiDAR-camera 3D multi-object tracking (MOT) combines rich visual semantics with accurate depth cues to improve trajectory consistency and tracking reliability. In practice, however, LiDAR and cameras operate at different sampling rates. To maintain temporal alignment, existing data pipelines usually synchronize heterogeneous sensor streams and annotate them at a reduced shared frequency, forcing most prior methods to perform spatial fusion only at synchronized timestamps through projection-based or learnable cross-sensor association. As a result, abundant asynchronous observations remain underexploited, despite their potential to support more frequent association and more robust trajectory estimation over short temporal intervals.
>   To address this limitation, we propose Fusion-Poly, a spatial-temporal fusion framework for 3D MOT that integrates asynchronous LiDAR and camera data. Fusion-Poly associates trajectories with multi-modal observations at synchronized timestamps and with single-modal observations at asynchronous timestamps, enabling higher-frequency updates of motion and existence states. The framework contains three key components: a frequency-aware cascade matching module that adapts to synchronized and asynchronous frames according to available detection modalities; a frequency-aware trajectory estimation module that maintains trajectories through high-frequency motion prediction, differential updates, and confidence-calibrated lifecycle management; and a full-state observation alignment module that improves cross-modal consistency at synchronized timestamps by optimizing image-projection errors.
>   On the nuScenes test set, Fusion-Poly achieves 76.5% AMOTA, establishing a new state of the art among tracking-by-detection 3D MOT methods. Extensive ablation studies further validate the effectiveness of each component. Code will be released.

