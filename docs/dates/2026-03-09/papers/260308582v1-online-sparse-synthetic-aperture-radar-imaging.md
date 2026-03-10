---
layout: default
title: Online Sparse Synthetic Aperture Radar Imaging
---

# Online Sparse Synthetic Aperture Radar Imaging
**arXiv**：[2603.08582v1](https://arxiv.org/abs/2603.08582) · [PDF](https://arxiv.org/pdf/2603.08582.pdf)  
**作者**：Conor Flynn, Radoslav Ivanov, Birsen Yazici  

**一句话要点**：提出在线快速迭代收缩阈值算法以解决合成孔径雷达在线稀疏成像中的计算与内存效率问题

**关键词**：合成孔径雷达成像, 在线稀疏重建, 快速迭代收缩阈值算法, 内存效率优化, 自动目标识别

## 3 点简述
- 核心问题：现代防御应用中，无人机需高效处理合成孔径雷达大数据，传统方法内存需求高。
- 方法要点：在线快速迭代收缩阈值算法通过稀疏编码增量重建场景，递归更新存储矩阵减少内存。
- 实验或效果：未知，但论文称该方法促进在线自动目标识别，比现有后收集方法更集成。

## 摘要（原文）

> With modern defense applications increasingly relying on inexpensive, autonomous drones, lies the major challenge of designing computationally and memory-efficient onboard algorithms to fulfill mission objectives. This challenge is particularly significant in Synthetic Aperture Radar (SAR), where large volumes of data must be collected and processed for downstream tasks. We propose an online reconstruction method, the Online Fast Iterative Shrinkage-Thresholding Algorithm (Online FISTA), which incrementally reconstructs a scene with limited data through sparse coding. Rather than requiring storage of all received signal data, the algorithm recursively updates storage matrices for each iteration, greatly reducing memory demands. Online SAR image reconstruction facilitates more complex downstream tasks, such as Automatic Target Recognition (ATR), in an online manner, resulting in a more versatile and integrated framework compared to existing post-collection reconstruction and ATR approaches.

