---
layout: default
title: DAGE: Dual-Stream Architecture for Efficient and Fine-Grained Geometry Estimation
---

# DAGE: Dual-Stream Architecture for Efficient and Fine-Grained Geometry Estimation
**arXiv**：[2603.03744v1](https://arxiv.org/abs/2603.03744) · [PDF](https://arxiv.org/pdf/2603.03744.pdf)  
**作者**：Tuan Duc Ngo, Jiahui Huang, Seoung Wug Oh, Kevin Blackburn-Matzen, Evangelos Kalogerakis, Chuang Gan, Joon-Young Lee  

**一句话要点**：提出双流架构DAGE以解决未标定多视图/视频中高效精细几何估计问题

**关键词**：双流Transformer, 几何估计, 多视图重建, 高分辨率处理, 相机姿态估计, 视频理解

## 3 点简述
- 核心问题：未标定多视图/视频中高分辨率长序列的几何与相机姿态估计挑战
- 方法要点：双流Transformer分离全局一致性与细节，低分辨率流高效估计相机，高分辨率流保留精细结构
- 实验或效果：支持2K输入，在视频几何估计与多视图重建中达到新SOTA，保持实用推理成本

## 摘要（原文）

> Estimating accurate, view-consistent geometry and camera poses from uncalibrated multi-view/video inputs remains challenging - especially at high spatial resolutions and over long sequences. We present DAGE, a dual-stream transformer whose main novelty is to disentangle global coherence from fine detail. A low-resolution stream operates on aggressively downsampled frames with alternating frame/global attention to build a view-consistent representation and estimate cameras efficiently, while a high-resolution stream processes the original images per-frame to preserve sharp boundaries and small structures. A lightweight adapter fuses these streams via cross-attention, injecting global context without disturbing the pretrained single-frame pathway. This design scales resolution and clip length independently, supports inputs up to 2K, and maintains practical inference cost. DAGE delivers sharp depth/pointmaps, strong cross-view consistency, and accurate poses, establishing new state-of-the-art results for video geometry estimation and multi-view reconstruction.

