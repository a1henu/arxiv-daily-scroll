---
layout: default
title: LocBAM: Advancing 3D Patch-Based Image Segmentation by Integrating Location Contex
---

# LocBAM: Advancing 3D Patch-Based Image Segmentation by Integrating Location Contex
**arXiv**：[2601.14802v1](https://arxiv.org/abs/2601.14802) · [PDF](https://arxiv.org/pdf/2601.14802.pdf)  
**作者**：Donnate Hooft, Stefan M. Fischer, Cosmin Bercea, Jan C. Peeken, Julia A. Schnabel  

**一句话要点**：提出LocBAM注意力机制，通过整合位置上下文提升基于补丁的3D医学图像分割性能。

**关键词**：3D医学图像分割, 补丁方法, 位置上下文, 注意力机制, 低覆盖场景

## 3 点简述
- 核心问题：基于补丁的3D分割方法常忽略补丁在全局体积中的位置，限制解剖上下文重要时的性能。
- 方法要点：引入LocBAM注意力机制，显式处理空间信息以增强位置上下文。
- 实验或效果：在BTCV等数据集上验证，LocBAM稳定训练并提升分割，尤其在低覆盖场景下优于CoordConv。

## 摘要（原文）

> Patch-based methods are widely used in 3D medical image segmentation to address memory constraints in processing high-resolution volumetric data. However, these approaches often neglect the patch's location within the global volume, which can limit segmentation performance when anatomical context is important. In this paper, we investigate the role of location context in patch-based 3D segmentation and propose a novel attention mechanism, LocBAM, that explicitly processes spatial information. Experiments on BTCV, AMOS22, and KiTS23 demonstrate that incorporating location context stabilizes training and improves segmentation performance, particularly under low patch-to-volume coverage where global context is missing. Furthermore, LocBAM consistently outperforms classical coordinate encoding via CoordConv. Code is publicly available at https://github.com/compai-lab/2026-ISBI-hooft

