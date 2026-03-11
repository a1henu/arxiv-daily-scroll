---
layout: default
title: SpaceSense-Bench: A Large-Scale Multi-Modal Benchmark for Spacecraft Perception and Pose Estimation
---

# SpaceSense-Bench: A Large-Scale Multi-Modal Benchmark for Spacecraft Perception and Pose Estimation
**arXiv**：[2603.09320v1](https://arxiv.org/abs/2603.09320) · [PDF](https://arxiv.org/pdf/2603.09320.pdf)  
**作者**：Aodi Wu, Jianhong Zuo, Zeyuan Zhao, Xubo Luo, Ruisuo Wang, Xue Wan  

**一句话要点**：提出SpaceSense-Bench大规模多模态基准，以解决航天器感知中数据不足和标注不完整的问题。

**关键词**：航天器感知, 多模态基准, 部件级语义分割, 姿态估计, 合成数据集, 零样本泛化

## 3 点简述
- 核心问题：自主空间操作需鲁棒的部件级语义理解和精确姿态估计，但真实数据收集困难，现有合成数据集目标多样性低、模态单一、标注不全。
- 方法要点：基于Unreal Engine 5高保真模拟，构建包含136个卫星模型、约70GB数据的多模态基准，提供RGB图像、深度图、LiDAR点云及密集7类部件级语义标签和6-DoF姿态真值。
- 实验或效果：基准测试五个任务，发现小部件感知和零样本泛化是瓶颈，增加训练卫星数量能显著提升新目标性能，凸显大规模数据集价值。

## 摘要（原文）

> Autonomous space operations such as on-orbit servicing and active debris removal demand robust part-level semantic understanding and precise relative navigation of target spacecraft, yet collecting large-scale real data in orbit remains impractical due to cost and access constraints. Existing synthetic datasets, moreover, suffer from limited target diversity, single-modality sensing, and incomplete ground-truth annotations. We present \textbf{SpaceSense-Bench}, a large-scale multi-modal benchmark for spacecraft perception encompassing 136~satellite models with approximately 70~GB of data. Each frame provides time-synchronized 1024$\times$1024 RGB images, millimeter-precision depth maps, and 256-beam LiDAR point clouds, together with dense 7-class part-level semantic labels at both the pixel and point level as well as accurate 6-DoF pose ground truth. The dataset is generated through a high-fidelity space simulation built in Unreal Engine~5 and a fully automated pipeline covering data acquisition, multi-stage quality control, and conversion to mainstream formats. We benchmark five representative tasks (object detection, 2D semantic segmentation, RGB--LiDAR fusion-based 3D point cloud segmentation, monocular depth estimation, and orientation estimation) and identify two key findings: (i)~perceiving small-scale components (\emph{e.g.}, thrusters and omni-antennas) and generalizing to entirely unseen spacecraft in a zero-shot setting remain critical bottlenecks for current methods, and (ii)~scaling up the number of training satellites yields substantial performance gains on novel targets, underscoring the value of large-scale, diverse datasets for space perception research. The dataset, code, and toolkit are publicly available at https://github.com/wuaodi/SpaceSense-Bench.

