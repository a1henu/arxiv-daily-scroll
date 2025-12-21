---
layout: default
title: SegGraph: Leveraging Graphs of SAM Segments for Few-Shot 3D Part Segmentation
---

# SegGraph: Leveraging Graphs of SAM Segments for Few-Shot 3D Part Segmentation
**arXiv**：[2512.16143v1](https://arxiv.org/abs/2512.16143) · [PDF](https://arxiv.org/pdf/2512.16143.pdf)  
**作者**：Yueyang Hu, Haiyong Jiang, Haoxuan Song, Jun Xiao, Hao Pan  

**一句话要点**：提出SegGraph框架，利用SAM分割图进行少样本3D部件分割

**关键词**：少样本学习, 3D部件分割, 分割图, 图神经网络, SAM模型, 几何特征学习

## 3 点简述
- 核心问题：现有方法在聚合2D基础模型知识到3D时忽略几何结构或SAM高质量分组线索，导致欠分割和标签不一致。
- 方法要点：构建分割图，节点代表SAM分割段，边捕获空间关系，通过图神经网络传播特征以学习全局几何结构。
- 实验或效果：在PartNet-E上优于所有基线至少6.9% mIoU，在小部件和边界上表现优异，代码已开源。

## 摘要（原文）

> This work presents a novel framework for few-shot 3D part segmentation. Recent advances have demonstrated the significant potential of 2D foundation models for low-shot 3D part segmentation. However, it is still an open problem that how to effectively aggregate 2D knowledge from foundation models to 3D. Existing methods either ignore geometric structures for 3D feature learning or neglects the high-quality grouping clues from SAM, leading to under-segmentation and inconsistent part labels. We devise a novel SAM segment graph-based propagation method, named SegGraph, to explicitly learn geometric features encoded within SAM's segmentation masks. Our method encodes geometric features by modeling mutual overlap and adjacency between segments while preserving intra-segment semantic consistency. We construct a segment graph, conceptually similar to an atlas, where nodes represent segments and edges capture their spatial relationships (overlap/adjacency). Each node adaptively modulates 2D foundation model features, which are then propagated via a graph neural network to learn global geometric structures. To enforce intra-segment semantic consistency, we map segment features to 3D points with a novel view-direction-weighted fusion attenuating contributions from low-quality segments. Extensive experiments on PartNet-E demonstrate that our method outperforms all competing baselines by at least 6.9 percent mIoU. Further analysis reveals that SegGraph achieves particularly strong performance on small components and part boundaries, demonstrating its superior geometric understanding. The code is available at: https://github.com/YueyangHu2000/SegGraph.

