---
layout: default
title: GSM-GS: Geometry-Constrained Single and Multi-view Gaussian Splatting for Surface Reconstruction
---

# GSM-GS: Geometry-Constrained Single and Multi-view Gaussian Splatting for Surface Reconstruction
**arXiv**：[2602.12796v1](https://arxiv.org/abs/2602.12796) · [PDF](https://arxiv.org/pdf/2602.12796.pdf)  
**作者**：Xiao Ren, Yu Liu, Ning An, Jian Cheng, Xin Qiao, He Kong  

**一句话要点**：提出GSM-GS框架，通过单视图自适应加权和多视图几何约束提升表面重建精度

**关键词**：高斯泼溅, 表面重建, 单视图优化, 多视图优化, 几何约束, 点云关联

## 3 点简述
- 核心问题：高斯点云的无结构特性导致复杂表面细节重建不准确，高频细节易丢失。
- 方法要点：单视图优化基于图像梯度分区，自适应加权保留纹理丰富区域；多视图优化引入几何引导的跨视图关联，增强一致性。
- 实验或效果：在公开数据集上验证，实现竞争性渲染质量和几何重建，提升重建保真度。

## 摘要（原文）

> Recently, 3D Gaussian Splatting has emerged as a prominent research direction owing to its ultrarapid training speed and high-fidelity rendering capabilities. However, the unstructured and irregular nature of Gaussian point clouds poses challenges to reconstruction accuracy. This limitation frequently causes high-frequency detail loss in complex surface microstructures when relying solely on routine strategies. To address this limitation, we propose GSM-GS: a synergistic optimization framework integrating single-view adaptive sub-region weighting constraints and multi-view spatial structure refinement. For single-view optimization, we leverage image gradient features to partition scenes into texture-rich and texture-less sub-regions. The reconstruction quality is enhanced through adaptive filtering mechanisms guided by depth discrepancy features. This preserves high-weight regions while implementing a dual-branch constraint strategy tailored to regional texture variations, thereby improving geometric detail characterization. For multi-view optimization, we introduce a geometry-guided cross-view point cloud association method combined with a dynamic weight sampling strategy. This constructs 3D structural normal constraints across adjacent point cloud frames, effectively reinforcing multi-view consistency and reconstruction fidelity. Extensive experiments on public datasets demonstrate that our method achieves both competitive rendering quality and geometric reconstruction. See our interactive project page

