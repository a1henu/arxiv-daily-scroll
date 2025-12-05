---
layout: default
title: Virtually Unrolling the Herculaneum Papyri by Diffeomorphic Spiral Fitting
---

# Virtually Unrolling the Herculaneum Papyri by Diffeomorphic Spiral Fitting
**arXiv**：[2512.04927v1](https://arxiv.org/abs/2512.04927) · [PDF](https://arxiv.org/pdf/2512.04927.pdf)  
**作者**：Paul Henderson  

**一句话要点**：提出基于可微螺旋拟合的自动表面建模方法，以虚拟展开赫库兰尼姆古卷

**关键词**：虚拟展开, CT扫描分析, 表面建模, 螺旋拟合, 古卷数字化, 自动化重建

## 3 点简述
- 核心问题：赫库兰尼姆古卷因碳化易碎，无法物理展开，需从CT扫描中自动重建卷曲表面。
- 方法要点：全局拟合显式参数模型到神经网络预测的卷曲路径，确保表面连续且可处理不可检测区域。
- 实验或效果：在高分辨率CT扫描上验证，成功展开大面积区域，性能优于现有自动化方法。

## 摘要（原文）

> The Herculaneum Papyri are a collection of rolled papyrus documents that were charred and buried by the famous eruption of Mount Vesuvius. They promise to contain a wealth of previously unseen Greek and Latin texts, but are extremely fragile and thus most cannot be unrolled physically. A solution to access these texts is virtual unrolling, where the papyrus surface is digitally traced out in a CT scan of the scroll, to create a flattened representation. This tracing is very laborious to do manually in gigavoxel-sized scans, so automated approaches are desirable. We present the first top-down method that automatically fits a surface model to a CT scan of a severely damaged scroll. We take a novel approach that globally fits an explicit parametric model of the deformed scroll to existing neural network predictions of where the rolled papyrus likely passes. Our method guarantees the resulting surface is a single continuous 2D sheet, even passing through regions where the surface is not detectable in the CT scan. We conduct comprehensive experiments on high-resolution CT scans of two scrolls, showing that our approach successfully unrolls large regions, and exceeds the performance of the only existing automated unrolling method suitable for this data.

