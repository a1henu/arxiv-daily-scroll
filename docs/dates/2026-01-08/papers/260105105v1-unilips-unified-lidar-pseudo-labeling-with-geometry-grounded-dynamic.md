---
layout: default
title: UniLiPs: Unified LiDAR Pseudo-Labeling with Geometry-Grounded Dynamic Scene Decomposition
---

# UniLiPs: Unified LiDAR Pseudo-Labeling with Geometry-Grounded Dynamic Scene Decomposition
**arXiv**：[2601.05105v1](https://arxiv.org/abs/2601.05105) · [PDF](https://arxiv.org/pdf/2601.05105.pdf)  
**作者**：Filippo Ghilotti, Samuel Brucker, Nahku Saidy, Matteo Matteucci, Mario Bijelic, Felix Heide  

**一句话要点**：提出UniLiPs方法，利用几何一致性从无标签LiDAR数据生成3D伪标签，以降低自动驾驶感知成本。

**关键词**：LiDAR伪标签, 几何一致性, 自动驾驶感知, 多模态融合, 无监督学习, 3D语义分割

## 3 点简述
- 核心问题：无标签LiDAR数据在自动驾驶中因标注成本高而难以利用，阻碍感知研究。
- 方法要点：基于时间几何一致性，融合文本和2D视觉模型线索，通过迭代更新实现几何-语义一致性，并检测移动物体。
- 实验或效果：在三个数据集上验证，优于现有伪标签方法，提升深度预测精度，如80-150米范围MAE降低51.5%。

## 摘要（原文）

> Unlabeled LiDAR logs, in autonomous driving applications, are inherently a gold mine of dense 3D geometry hiding in plain sight - yet they are almost useless without human labels, highlighting a dominant cost barrier for autonomous-perception research. In this work we tackle this bottleneck by leveraging temporal-geometric consistency across LiDAR sweeps to lift and fuse cues from text and 2D vision foundation models directly into 3D, without any manual input. We introduce an unsupervised multi-modal pseudo-labeling method relying on strong geometric priors learned from temporally accumulated LiDAR maps, alongside with a novel iterative update rule that enforces joint geometric-semantic consistency, and vice-versa detecting moving objects from inconsistencies. Our method simultaneously produces 3D semantic labels, 3D bounding boxes, and dense LiDAR scans, demonstrating robust generalization across three datasets. We experimentally validate that our method compares favorably to existing semantic segmentation and object detection pseudo-labeling methods, which often require additional manual supervision. We confirm that even a small fraction of our geometrically consistent, densified LiDAR improves depth prediction by 51.5% and 22.0% MAE in the 80-150 and 150-250 meters range, respectively.

