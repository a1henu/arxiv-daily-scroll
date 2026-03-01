---
layout: default
title: VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale
---

# VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale
**arXiv**：[2602.23361v1](https://arxiv.org/abs/2602.23361) · [PDF](https://arxiv.org/pdf/2602.23361.pdf)  
**作者**：Sven Elflein, Ruilong Li, Sérgio Agostinho, Zan Gojcic, Laura Leal-Taixé, Qunjie Zhou, Aljosa Osep  

**一句话要点**：提出VGG-T³以解决离线前馈3D重建中计算和内存需求随输入图像数量二次增长的问题。

**关键词**：3D重建, 离线前馈方法, 测试时训练, 线性缩放, 场景表示, 视觉定位

## 3 点简述
- 核心问题：离线前馈方法因场景几何的变长键值空间表示导致计算和内存需求随输入图像数量二次增长。
- 方法要点：通过测试时训练将变长键值空间蒸馏为固定大小的多层感知机，实现线性缩放。
- 实验或效果：在1千张图像集合上仅需54秒重建，比基于softmax注意力的基线快11.6倍，点云重建误差显著优于其他线性时间方法。

## 摘要（原文）

> We present a scalable 3D reconstruction model that addresses a critical limitation in offline feed-forward methods: their computational and memory requirements grow quadratically w.r.t. the number of input images. Our approach is built on the key insight that this bottleneck stems from the varying-length Key-Value (KV) space representation of scene geometry, which we distill into a fixed-size Multi-Layer Perceptron (MLP) via test-time training. VGG-T$^3$ (Visual Geometry Grounded Test Time Training) scales linearly w.r.t. the number of input views, similar to online models, and reconstructs a $1k$ image collection in just $54$ seconds, achieving a $11.6\times$ speed-up over baselines that rely on softmax attention. Since our method retains global scene aggregation capability, our point map reconstruction error outperforming other linear-time methods by large margins. Finally, we demonstrate visual localization capabilities of our model by querying the scene representation with unseen images.

