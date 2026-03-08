---
layout: default
title: Person Detection and Tracking from an Overhead Crane LiDAR
---

# Person Detection and Tracking from an Overhead Crane LiDAR
**arXiv**：[2603.04938v1](https://arxiv.org/abs/2603.04938) · [PDF](https://arxiv.org/pdf/2603.04938.pdf)  
**作者**：Nilusha Jayawickrama, Henrik Toikka, Risto Ojala  

**一句话要点**：提出基于天车LiDAR的人员检测与跟踪方法，以解决工业室内场景中的领域偏移问题

**关键词**：天车LiDAR, 人员检测, 3D目标检测, 人员跟踪, 工业室内场景, 领域适应

## 3 点简述
- 核心问题：天车视角LiDAR数据与常见车载基准存在领域偏移，且缺乏公开训练数据
- 方法要点：构建特定场景数据集，适配3D检测器，并集成轻量级跟踪算法
- 实验或效果：在5米半径内平均精度达0.84，1米内提升至0.97，并验证实时可行性

## 摘要（原文）

> This paper investigates person detection and tracking in an industrial indoor workspace using a LiDAR mounted on an overhead crane. The overhead viewpoint introduces a strong domain shift from common vehicle-centric LiDAR benchmarks, and limited availability of suitable public training data. Henceforth, we curate a site-specific overhead LiDAR dataset with 3D human bounding-box annotations and adapt selected candidate 3D detectors under a unified training and evaluation protocol. We further integrate lightweight tracking-by-detection using AB3DMOT and SimpleTrack to maintain person identities over time. Detection performance is reported with distance-sliced evaluation to quantify the practical operating envelope of the sensing setup. The best adapted detector configurations achieve average precision (AP) up to 0.84 within a 5.0 m horizontal radius, increasing to 0.97 at 1.0 m, with VoxelNeXt and SECOND emerging as the most reliable backbones across this range. The acquired results contribute in bridging the domain gap between standard driving datasets and overhead sensing for person detection and tracking. We also report latency measurements, highlighting practical real-time feasibility. Finally, we release our dataset and implementations in GitHub to support further research

