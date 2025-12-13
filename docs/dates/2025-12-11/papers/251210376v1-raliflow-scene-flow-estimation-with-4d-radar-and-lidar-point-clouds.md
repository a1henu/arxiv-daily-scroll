---
layout: default
title: RaLiFlow: Scene Flow Estimation with 4D Radar and LiDAR Point Clouds
---

# RaLiFlow: Scene Flow Estimation with 4D Radar and LiDAR Point Clouds
**arXiv**：[2512.10376v1](https://arxiv.org/abs/2512.10376) · [PDF](https://arxiv.org/pdf/2512.10376.pdf)  
**作者**：Jingyun Fu, Zhiyu Xiang, Na Zhao  

**一句话要点**：提出RaLiFlow框架，通过4D雷达与LiDAR融合解决场景流估计问题

**关键词**：场景流估计, 雷达-LiDAR融合, 跨模态学习, 动态感知, 自动驾驶感知

## 3 点简述
- 核心问题：缺乏雷达-LiDAR融合场景流数据集与方法，雷达数据噪声大、分辨率低
- 方法要点：构建雷达-LiDAR数据集，设计DBCF模块和损失函数实现跨模态动态信息融合
- 实验或效果：在重构数据集上显著优于单模态方法，提升动态前景区域估计一致性

## 摘要（原文）

> Recent multimodal fusion methods, integrating images with LiDAR point clouds, have shown promise in scene flow estimation. However, the fusion of 4D millimeter wave radar and LiDAR remains unexplored. Unlike LiDAR, radar is cheaper, more robust in various weather conditions and can detect point-wise velocity, making it a valuable complement to LiDAR. However, radar inputs pose challenges due to noise, low resolution, and sparsity. Moreover, there is currently no dataset that combines LiDAR and radar data specifically for scene flow estimation. To address this gap, we construct a Radar-LiDAR scene flow dataset based on a public real-world automotive dataset. We propose an effective preprocessing strategy for radar denoising and scene flow label generation, deriving more reliable flow ground truth for radar points out of the object boundaries. Additionally, we introduce RaLiFlow, the first joint scene flow learning framework for 4D radar and LiDAR, which achieves effective radar-LiDAR fusion through a novel Dynamic-aware Bidirectional Cross-modal Fusion (DBCF) module and a carefully designed set of loss functions. The DBCF module integrates dynamic cues from radar into the local cross-attention mechanism, enabling the propagation of contextual information across modalities. Meanwhile, the proposed loss functions mitigate the adverse effects of unreliable radar data during training and enhance the instance-level consistency in scene flow predictions from both modalities, particularly for dynamic foreground areas. Extensive experiments on the repurposed scene flow dataset demonstrate that our method outperforms existing LiDAR-based and radar-based single-modal methods by a significant margin.

