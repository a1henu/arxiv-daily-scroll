---
layout: default
title: SpatialLock: Precise Spatial Control in Text-to-Image Synthesis
---

# SpatialLock: Precise Spatial Control in Text-to-Image Synthesis
**arXiv**：[2511.04112v1](https://arxiv.org/abs/2511.04112) · [PDF](https://arxiv.org/pdf/2511.04112.pdf)  
**作者**：Biao Liu, Yuanzhi Liang  

**一句话要点**：提出SpatialLock框架以解决文本到图像合成中对象定位不精确的问题

**关键词**：文本到图像合成, 对象定位, 空间控制, 注意力机制, 感知监督

## 3 点简述
- 核心问题：现有方法未能充分利用位置信息，导致对象空间布局理解不足
- 方法要点：结合PoI和PoG组件，通过注意力层和感知监督实现空间控制
- 实验或效果：在多个数据集上IOU得分超过0.9，达到新最优性能

## 摘要（原文）

> Text-to-Image (T2I) synthesis has made significant advancements in recent
> years, driving applications such as generating datasets automatically. However,
> precise control over object localization in generated images remains a
> challenge. Existing methods fail to fully utilize positional information,
> leading to an inadequate understanding of object spatial layouts. To address
> this issue, we propose SpatialLock, a novel framework that leverages perception
> signals and grounding information to jointly control the generation of spatial
> locations. SpatialLock incorporates two components: Position-Engaged Injection
> (PoI) and Position-Guided Learning (PoG). PoI directly integrates spatial
> information through an attention layer, encouraging the model to learn the
> grounding information effectively. PoG employs perception-based supervision to
> further refine object localization. Together, these components enable the model
> to generate objects with precise spatial arrangements and improve the visual
> quality of the generated images. Experiments show that SpatialLock sets a new
> state-of-the-art for precise object positioning, achieving IOU scores above 0.9
> across multiple datasets.

