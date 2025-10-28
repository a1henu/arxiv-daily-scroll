---
layout: default
title: DPGLA: Bridging the Gap between Synthetic and Real Data for Unsupervised Domain Adaptation in 3D LiDAR Semantic Segmentation
---

# DPGLA: Bridging the Gap between Synthetic and Real Data for Unsupervised Domain Adaptation in 3D LiDAR Semantic Segmentation
**arXiv**：[2510.23525v1](https://arxiv.org/abs/2510.23525) · [PDF](https://arxiv.org/pdf/2510.23525.pdf)  
**作者**：Wanmeng Li, Simone Mosco, Daniel Fusaro, Alberto Pretto  

**一句话要点**：提出动态伪标签过滤与先验引导数据增强以提升3D LiDAR语义分割的无监督域适应性能

**关键词**：3D LiDAR语义分割, 无监督域适应, 动态伪标签过滤, 数据增强, 点云处理, 合成到真实迁移

## 3 点简述
- 核心问题：现有方法依赖固定置信阈值，未充分利用未标记数据，导致性能不佳。
- 方法要点：引入动态伪标签过滤和先导数据增强管道，减少合成与真实点云间的域偏移。
- 实验效果：在合成到真实点云分割任务中表现优异，消融研究验证模块有效性。

## 摘要（原文）

> Annotating real-world LiDAR point clouds for use in intelligent autonomous
> systems is costly. To overcome this limitation, self-training-based
> Unsupervised Domain Adaptation (UDA) has been widely used to improve point
> cloud semantic segmentation by leveraging synthetic point cloud data. However,
> we argue that existing methods do not effectively utilize unlabeled data, as
> they either rely on predefined or fixed confidence thresholds, resulting in
> suboptimal performance. In this paper, we propose a Dynamic Pseudo-Label
> Filtering (DPLF) scheme to enhance real data utilization in point cloud UDA
> semantic segmentation. Additionally, we design a simple and efficient
> Prior-Guided Data Augmentation Pipeline (PG-DAP) to mitigate domain shift
> between synthetic and real-world point clouds. Finally, we utilize data mixing
> consistency loss to push the model to learn context-free representations. We
> implement and thoroughly evaluate our approach through extensive comparisons
> with state-of-the-art methods. Experiments on two challenging synthetic-to-real
> point cloud semantic segmentation tasks demonstrate that our approach achieves
> superior performance. Ablation studies confirm the effectiveness of the DPLF
> and PG-DAP modules. We release the code of our method in this paper.

