---
layout: default
title: HoloEv-Net: Efficient Event-based Action Recognition via Holographic Spatial Embedding and Global Spectral Gating
---

# HoloEv-Net: Efficient Event-based Action Recognition via Holographic Spatial Embedding and Global Spectral Gating
**arXiv**：[2602.04182v1](https://arxiv.org/abs/2602.04182) · [PDF](https://arxiv.org/pdf/2602.04182.pdf)  
**作者**：Weidong Hao  

**一句话要点**：提出HoloEv-Net，通过全息空间嵌入和全局谱门控，高效解决事件相机动作识别中的冗余和谱信息利用不足问题。

**关键词**：事件相机动作识别, 全息空间嵌入, 全局谱门控, 紧凑时空表示, 高效计算, 边缘部署

## 3 点简述
- 核心问题：事件相机动作识别存在密集体素表示计算冗余、多分支结构冗余和全局运动谱信息利用不足。
- 方法要点：引入紧凑全息时空表示，将空间线索嵌入时间-高度视图；设计全局谱门控模块，利用FFT进行频域全局令牌混合。
- 实验或效果：在多个数据集上实现SOTA性能，轻量版大幅减少参数和计算量，适合边缘部署。

## 摘要（原文）

> Event-based Action Recognition (EAR) has attracted significant attention due to the high temporal resolution and high dynamic range of event cameras. However, existing methods typically suffer from (i) the computational redundancy of dense voxel representations, (ii) structural redundancy inherent in multi-branch architectures, and (iii) the under-utilization of spectral information in capturing global motion patterns. To address these challenges, we propose an efficient EAR framework named HoloEv-Net. First, to simultaneously tackle representation and structural redundancies, we introduce a Compact Holographic Spatiotemporal Representation (CHSR). Departing from computationally expensive voxel grids, CHSR implicitly embeds horizontal spatial cues into the Time-Height (T-H) view, effectively preserving 3D spatiotemporal contexts within a 2D representation. Second, to exploit the neglected spectral cues, we design a Global Spectral Gating (GSG) module. By leveraging the Fast Fourier Transform (FFT) for global token mixing in the frequency domain, GSG enhances the representation capability with negligible parameter overhead. Extensive experiments demonstrate the scalability and effectiveness of our framework. Specifically, HoloEv-Net-Base achieves state-of-the-art performance on THU-EACT-50-CHL, HARDVS and DailyDVS-200, outperforming existing methods by 10.29%, 1.71% and 6.25%, respectively. Furthermore, our lightweight variant, HoloEv-Net-Small, delivers highly competitive accuracy while offering extreme efficiency, reducing parameters by 5.4 times, FLOPs by 300times, and latency by 2.4times compared to heavy baselines, demonstrating its potential for edge deployment.

