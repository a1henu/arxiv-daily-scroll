---
layout: default
title: ParkingTwin: Training-Free Streaming 3D Reconstruction for Parking-Lot Digital Twins
---

# ParkingTwin: Training-Free Streaming 3D Reconstruction for Parking-Lot Digital Twins
**arXiv**：[2601.13706v1](https://arxiv.org/abs/2601.13706) · [PDF](https://arxiv.org/pdf/2601.13706.pdf)  
**作者**：Xinhao Liu, Yu Wang, Xiansheng Guo, Gordon Owusu Boateng, Yu Cao, Haonan Si, Xingchen Guo, Nirwan Ansari  

**一句话要点**：提出ParkingTwin训练免费流式3D重建系统，用于停车场数字孪生，解决几何弱视差、动态遮挡和光照变化问题。

**关键词**：停车场数字孪生, 训练免费3D重建, 流式几何构造, 动态遮挡过滤, 光照鲁棒融合, 实时渲染系统

## 3 点简述
- 核心问题：稀疏前视导致弱视差几何不适定，动态遮挡和极端光照阻碍纹理融合，神经渲染需离线优化违反流式约束。
- 方法要点：使用OSM先验驱动几何构造生成TSDF，几何感知动态过滤实时剔除移动物体，CIELAB空间光照鲁棒融合减少接缝。
- 实验或效果：在GTX 1660上运行30+ FPS，SSIM 0.87提升16.0%，相比3DGS加速15倍并减少83.3% GPU内存。

## 摘要（原文）

> High-fidelity parking-lot digital twins provide essential priors for path planning, collision checking, and perception validation in Automated Valet Parking (AVP). Yet robot-oriented reconstruction faces a trilemma: sparse forward-facing views cause weak parallax and ill-posed geometry; dynamic occlusions and extreme lighting hinder stable texture fusion; and neural rendering typically needs expensive offline optimization, violating edge-side streaming constraints. We propose ParkingTwin, a training-free, lightweight system for online streaming 3D reconstruction. First, OSM-prior-driven geometric construction uses OpenStreetMap semantic topology to directly generate a metric-consistent TSDF, replacing blind geometric search with deterministic mapping and avoiding costly optimization. Second, geometry-aware dynamic filtering employs a quad-modal constraint field (normal/height/depth consistency) to reject moving vehicles and transient occlusions in real time. Third, illumination-robust fusion in CIELAB decouples luminance and chromaticity via adaptive L-channel weighting and depth-gradient suppression, reducing seams under abrupt lighting changes. ParkingTwin runs at 30+ FPS on an entry-level GTX 1660. On a 68,000 m^2 real-world dataset, it achieves SSIM 0.87 (+16.0%), delivers about 15x end-to-end speedup, and reduces GPU memory by 83.3% compared with state-of-the-art 3D Gaussian Splatting (3DGS) that typically requires high-end GPUs (RTX 4090D). The system outputs explicit triangle meshes compatible with Unity/Unreal digital-twin pipelines. Project page: https://mihoutao-liu.github.io/ParkingTwin/

