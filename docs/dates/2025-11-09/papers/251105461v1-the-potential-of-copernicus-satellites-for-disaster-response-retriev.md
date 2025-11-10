---
layout: default
title: The Potential of Copernicus Satellites for Disaster Response: Retrieving Building Damage from Sentinel-1 and Sentinel-2
---

# The Potential of Copernicus Satellites for Disaster Response: Retrieving Building Damage from Sentinel-1 and Sentinel-2
**arXiv**：[2511.05461v1](https://arxiv.org/abs/2511.05461) · [PDF](https://arxiv.org/pdf/2511.05461.pdf)  
**作者**：Olivier Dietrich, Merlin Alfredsson, Emilia Arens, Nando Metzger, Torben Peters, Linus Scheibenreif, Jan Dirk Wegner, Konrad Schindler  

**一句话要点**：提出xBD-S12数据集与模型，利用Sentinel卫星图像进行建筑损伤评估。

**关键词**：建筑损伤评估, Sentinel卫星图像, xBD-S12数据集, 灾害响应, 中等分辨率遥感

## 3 点简述
- 核心问题：自然灾害后快速评估建筑损伤，但高分辨率图像可用性有限。
- 方法要点：构建xBD-S12数据集，结合Sentinel-1和Sentinel-2图像训练模型。
- 实验或效果：在10米分辨率下能较好检测损伤，复杂模型泛化能力未知。

## 摘要（原文）

> Natural disasters demand rapid damage assessment to guide humanitarian
> response. Here, we investigate whether medium-resolution Earth observation
> images from the Copernicus program can support building damage assessment,
> complementing very-high resolution imagery with often limited availability. We
> introduce xBD-S12, a dataset of 10,315 pre- and post-disaster image pairs from
> both Sentinel-1 and Sentinel-2, spatially and temporally aligned with the
> established xBD benchmark. In a series of experiments, we demonstrate that
> building damage can be detected and mapped rather well in many disaster
> scenarios, despite the moderate 10$\,$m ground sampling distance. We also find
> that, for damage mapping at that resolution, architectural sophistication does
> not seem to bring much advantage: more complex model architectures tend to
> struggle with generalization to unseen disasters, and geospatial foundation
> models bring little practical benefit. Our results suggest that Copernicus
> images are a viable data source for rapid, wide-area damage assessment and
> could play an important role alongside VHR imagery. We release the xBD-S12
> dataset, code, and trained models to support further research.

