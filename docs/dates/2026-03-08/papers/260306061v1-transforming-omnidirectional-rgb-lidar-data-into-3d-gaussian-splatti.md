---
layout: default
title: Transforming Omnidirectional RGB-LiDAR data into 3D Gaussian Splatting
---

# Transforming Omnidirectional RGB-LiDAR data into 3D Gaussian Splatting
**arXiv**：[2603.06061v1](https://arxiv.org/abs/2603.06061) · [PDF](https://arxiv.org/pdf/2603.06061.pdf)  
**作者**：Semin Bae, Hansol Lim, Jongseong Brad Choi  

**一句话要点**：提出全向RGB-LiDAR重用流程，将存档传感器日志转化为3D高斯溅射的初始化资产

**关键词**：3D高斯溅射, 全向传感器融合, 数字孪生构建, LiDAR初始化, 多模态配准, 存档数据重用

## 3 点简述
- 问题：全向RGB-LiDAR日志因非线性失真和密集点云导致SfM跟踪不可靠及计算开销大，数据利用率低
- 方法：集成ERP到立方体贴图转换和PRISM降采样，通过FPFH全局配准和ICP桥接多模态输入
- 效果：LiDAR增强初始化提升复杂场景3DGS渲染保真度，提供从标准日志创建数字孪生的确定性工作流

## 摘要（原文）

> The demand for large-scale digital twins is rapidly growing in robotics and autonomous driving. However, constructing these environments with 3D Gaussian Splatting (3DGS) usually requires expensive, purpose-built data collection. Meanwhile, deployed platforms routinely collect extensive omnidirectional RGB and LiDAR logs, but a significant portion of these sensor data is directly discarded or strictly underutilized due to transmission constraints and the lack of scalable reuse pipeline. In this paper, we present an omnidirectional RGB-LiDAR reuse pipeline that transforms these archived logs into robust initialization assets for 3DGS. Direct conversion of such raw logs introduces practical bottlenecks: inherent non-linear distortion leads to unreliable Structure-from-Motion (SfM) tracking, and dense, unorganized LiDAR clouds cause computational overhead during 3DGS optimization. To overcome these challenges, our pipeline strategically integrates an ERP-to-cubemap conversion module for deterministic spatial anchoring, alongside PRISM-a color stratified downsampling strategy. By bridging these multi-modal inputs via Fast Point Feature Histograms (FPFH) based global registration and Iterative Closest Point (ICP), our pipeline successfully repurposes a considerable fraction of discarded data into usable SfM geometry. Furthermore, our LiDAR-reinforced initialization consistently enhances the final 3DGS rendering fidelity in structurally complex scenes compared to vision-only baselines. Ultimately, this work provides a deterministic workflow for creating simulation-grade digital twins from standard archived sensor logs.

