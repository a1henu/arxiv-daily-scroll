---
layout: default
title: Reducing the labeling burden in time-series mapping using Common Ground: a semi-automated approach to tracking changes in land cover and species over time
---

# Reducing the labeling burden in time-series mapping using Common Ground: a semi-automated approach to tracking changes in land cover and species over time
**arXiv**：[2602.04373v1](https://arxiv.org/abs/2602.04373) · [PDF](https://arxiv.org/pdf/2602.04373.pdf)  
**作者**：Geethen Singh, Jasper A Slingsby, Tamara B Robinson, Glenn Moncrieff  

**一句话要点**：提出Common Ground半自动化方法，以减少时间序列遥感分类中的标注负担

**关键词**：时间序列遥感分类, 半监督学习, 变化检测, 标注效率, 生态监测, 多传感器应用

## 3 点简述
- 核心问题：遥感数据分类依赖更新标注，但动态或偏远生态系统中收集新标注成本高且困难
- 方法要点：利用时间稳定区域作为隐式监督，结合变化检测和半监督学习实现时间泛化
- 实验或效果：在入侵树种映射中，相比朴素时间迁移提升21-40%，相比黄金标准提升10-16%

## 摘要（原文）

> Reliable classification of Earth Observation data depends on consistent, up-to-date reference labels. However, collecting new labelled data at each time step remains expensive and logistically difficult, especially in dynamic or remote ecological systems. As a response to this challenge, we demonstrate that a model with access to reference data solely from time step t0 can perform competitively on both t0 and a future time step t1, outperforming models trained separately on time-specific reference data (the gold standard). This finding suggests that effective temporal generalization can be achieved without requiring manual updates to reference labels beyond the initial time step t0. Drawing on concepts from change detection and semi-supervised learning (SSL), the most performant approach, "Common Ground", uses a semi-supervised framework that leverages temporally stable regions-areas with little to no change in spectral or semantic characteristics between time steps-as a source of implicit supervision for dynamic regions. We evaluate this strategy across multiple classifiers, sensors (Landsat-8, Sentinel-2 satellite multispectral and airborne imaging spectroscopy), and ecological use cases. For invasive tree species mapping, we observed a 21-40% improvement in classification accuracy using Common Ground compared to naive temporal transfer, where models trained at a single time step are directly applied to a future time step. We also observe a 10 -16% higher accuracy for the introduced approach compared to a gold-standard approach. In contrast, when broad land cover categories were mapped across Europe, we observed a more modest 2% increase in accuracy compared to both the naive and gold-standard approaches. These results underscore the effectiveness of combining stable reference screening with SSL for scalable and label-efficient multi-temporal remote sensing classification.

