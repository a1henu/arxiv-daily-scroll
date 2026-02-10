---
layout: default
title: Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction
---

# Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction
**arXiv**：[2602.09016v1](https://arxiv.org/abs/2602.09016) · [PDF](https://arxiv.org/pdf/2602.09016.pdf)  
**作者**：Hao Phung, Hadar Averbuch-Elor  

**一句话要点**：提出Raster2Seq方法，通过序列生成解决复杂平面图重建问题

**关键词**：平面图重建, 序列生成, 自回归解码, 可学习锚点, 向量图形表示

## 3 点简述
- 核心问题：现有技术难以准确重建包含多房间和复杂多边形结构的平面图。
- 方法要点：将重建任务建模为序列到序列问题，使用自回归解码器和可学习锚点指导角点预测。
- 实验或效果：在多个标准基准测试中达到最优性能，并展示了对挑战性数据集的强泛化能力。

## 摘要（原文）

> Reconstructing a structured vector-graphics representation from a rasterized floorplan image is typically an important prerequisite for computational tasks involving floorplans such as automated understanding or CAD workflows. However, existing techniques struggle in faithfully generating the structure and semantics conveyed by complex floorplans that depict large indoor spaces with many rooms and a varying numbers of polygon corners. To this end, we propose Raster2Seq, framing floorplan reconstruction as a sequence-to-sequence task in which floorplan elements--such as rooms, windows, and doors--are represented as labeled polygon sequences that jointly encode geometry and semantics. Our approach introduces an autoregressive decoder that learns to predict the next corner conditioned on image features and previously generated corners using guidance from learnable anchors. These anchors represent spatial coordinates in image space, hence allowing for effectively directing the attention mechanism to focus on informative image regions. By embracing the autoregressive mechanism, our method offers flexibility in the output format, enabling for efficiently handling complex floorplans with numerous rooms and diverse polygon structures. Our method achieves state-of-the-art performance on standard benchmarks such as Structure3D, CubiCasa5K, and Raster2Graph, while also demonstrating strong generalization to more challenging datasets like WAFFLE, which contain diverse room structures and complex geometric variations.

