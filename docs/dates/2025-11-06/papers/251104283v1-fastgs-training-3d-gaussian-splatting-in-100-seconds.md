---
layout: default
title: FastGS: Training 3D Gaussian Splatting in 100 Seconds
---

# FastGS: Training 3D Gaussian Splatting in 100 Seconds
**arXiv**：[2511.04283v1](https://arxiv.org/abs/2511.04283) · [PDF](https://arxiv.org/pdf/2511.04283.pdf)  
**作者**：Shiwei Ren, Tianci Wen, Yongchun Fang, Biao Lu  

**一句话要点**：提出FastGS以加速3D高斯溅射训练，基于多视图一致性优化高斯数量

**关键词**：3D高斯溅射, 训练加速, 多视图一致性, 高斯优化, 场景重建

## 3 点简述
- 核心问题：现有3D高斯溅射加速方法未有效调控高斯数量，导致计算冗余。
- 方法要点：设计基于多视图一致性的高斯致密化与剪枝策略，无需预算机制。
- 实验效果：在多个数据集上实现2-7倍训练加速，渲染质量可比。

## 摘要（原文）

> The dominant 3D Gaussian splatting (3DGS) acceleration methods fail to
> properly regulate the number of Gaussians during training, causing redundant
> computational time overhead. In this paper, we propose FastGS, a novel, simple,
> and general acceleration framework that fully considers the importance of each
> Gaussian based on multi-view consistency, efficiently solving the trade-off
> between training time and rendering quality. We innovatively design a
> densification and pruning strategy based on multi-view consistency, dispensing
> with the budgeting mechanism. Extensive experiments on Mip-NeRF 360, Tanks &
> Temples, and Deep Blending datasets demonstrate that our method significantly
> outperforms the state-of-the-art methods in training speed, achieving a
> 3.32$\times$ training acceleration and comparable rendering quality compared
> with DashGaussian on the Mip-NeRF 360 dataset and a 15.45$\times$ acceleration
> compared with vanilla 3DGS on the Deep Blending dataset. We demonstrate that
> FastGS exhibits strong generality, delivering 2-7$\times$ training acceleration
> across various tasks, including dynamic scene reconstruction, surface
> reconstruction, sparse-view reconstruction, large-scale reconstruction, and
> simultaneous localization and mapping. The project page is available at
> https://fastgs.github.io/

