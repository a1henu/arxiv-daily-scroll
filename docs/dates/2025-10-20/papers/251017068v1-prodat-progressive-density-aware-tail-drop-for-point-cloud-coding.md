---
layout: default
title: ProDAT: Progressive Density-Aware Tail-Drop for Point Cloud Coding
---

# ProDAT: Progressive Density-Aware Tail-Drop for Point Cloud Coding
**arXiv**：[2510.17068v1](https://arxiv.org/abs/2510.17068) · [PDF](https://arxiv.org/pdf/2510.17068.pdf)  
**作者**：Zhe Luo, Wenjing Jia, Stuart Perry  

**一句话要点**：提出ProDAT密度感知尾丢机制，实现点云渐进式编码以应对带宽限制

**关键词**：点云编码, 渐进解码, 密度感知, 学习型压缩, 三维数据处理

## 3 点简述
- 核心问题：点云数据量大，固定潜在表示不支持渐进解码，阻碍资源受限环境应用
- 方法要点：利用密度信息指导自适应解码潜在特征和坐标，实现多比特率渐进编码
- 实验效果：在基准数据集上，ProDAT实现渐进编码，BD-rate提升超28.6%

## 摘要（原文）

> Three-dimensional (3D) point clouds are becoming increasingly vital in
> applications such as autonomous driving, augmented reality, and immersive
> communication, demanding real-time processing and low latency. However, their
> large data volumes and bandwidth constraints hinder the deployment of
> high-quality services in resource-limited environments. Progres- sive coding,
> which allows for decoding at varying levels of detail, provides an alternative
> by allowing initial partial decoding with subsequent refinement. Although
> recent learning-based point cloud geometry coding methods have achieved notable
> success, their fixed latent representation does not support progressive
> decoding. To bridge this gap, we propose ProDAT, a novel density-aware
> tail-drop mechanism for progressive point cloud coding. By leveraging density
> information as a guidance signal, latent features and coordinates are decoded
> adaptively based on their significance, therefore achieving progressive
> decoding at multiple bitrates using one single model. Experimental results on
> benchmark datasets show that the proposed ProDAT not only enables progressive
> coding but also achieves superior coding efficiency compared to
> state-of-the-art learning-based coding techniques, with over 28.6% BD-rate
> improvement for PSNR- D2 on SemanticKITTI and over 18.15% for ShapeNet

