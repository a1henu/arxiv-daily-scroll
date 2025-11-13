---
layout: default
title: SasMamba: A Lightweight Structure-Aware Stride State Space Model for 3D Human Pose Estimation
---

# SasMamba: A Lightweight Structure-Aware Stride State Space Model for 3D Human Pose Estimation
**arXiv**：[2511.08872v1](https://arxiv.org/abs/2511.08872) · [PDF](https://arxiv.org/pdf/2511.08872.pdf)  
**作者**：Hu Cui, Wenqiang Hua, Renjing Huang, Shurui Jia, Tessai Hayama  

**一句话要点**：提出SasMamba以解决3D人体姿态估计中空间结构破坏问题

**关键词**：3D人体姿态估计, 状态空间模型, 结构感知卷积, 跨步扫描, 轻量级模型

## 3 点简述
- 现有SSM方法将2D姿态序列展平，破坏空间结构并混淆时空特征
- 采用结构感知时空卷积和跨步扫描策略，建模局部和全局姿态信息
- 模型参数少，在3D姿态估计中性能竞争，代码已开源

## 摘要（原文）

> Recently, the Mamba architecture based on State Space Models (SSMs) has gained attention in 3D human pose estimation due to its linear complexity and strong global modeling capability. However, existing SSM-based methods typically apply manually designed scan operations to flatten detected 2D pose sequences into purely temporal sequences, either locally or globally. This approach disrupts the inherent spatial structure of human poses and entangles spatial and temporal features, making it difficult to capture complex pose dependencies. To address these limitations, we propose the Skeleton Structure-Aware Stride SSM (SAS-SSM), which first employs a structure-aware spatiotemporal convolution to dynamically capture essential local interactions between joints, and then applies a stride-based scan strategy to construct multi-scale global structural representations. This enables flexible modeling of both local and global pose information while maintaining linear computational complexity. Built upon SAS-SSM, our model SasMamba achieves competitive 3D pose estimation performance with significantly fewer parameters compared to existing hybrid models. The source code is available at https://hucui2022.github.io/sasmamba_proj/.

