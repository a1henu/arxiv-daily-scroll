---
layout: default
title: CHMv2: Improvements in Global Canopy Height Mapping using DINOv3
---

# CHMv2: Improvements in Global Canopy Height Mapping using DINOv3
**arXiv**：[2603.06382v1](https://arxiv.org/abs/2603.06382) · [PDF](https://arxiv.org/pdf/2603.06382.pdf)  
**作者**：John Brandt, Seungeun Yi, Jamie Tolan, Xinyuan Li, Peter Potapov, Jessica Ertel, Justine Spore, Huy V. Vo, Michaël Ramamonjisoa, Patrick Labatut, Piotr Bojanowski, Camille Couprie  

**一句话要点**：提出CHMv2，基于DINOv3改进全球冠层高度映射，以解决ALS数据不均问题。

**关键词**：冠层高度映射, DINOv3, 深度估计, 全球森林监测, 光学卫星图像, ALS训练数据

## 3 点简述
- 核心问题：全球冠层高度测量依赖ALS，但数据分布不均，影响森林碳量评估。
- 方法要点：利用DINOv3构建深度估计模型，通过大规模多样化训练数据和优化损失函数提升精度。
- 实验或效果：验证显示CHMv2在独立ALS测试和GEDI/ICESat-2观测中表现一致，减少高林偏差。

## 摘要（原文）

> Accurate canopy height information is essential for quantifying forest carbon, monitoring restoration and degradation, and assessing habitat structure, yet high-fidelity measurements from airborne laser scanning (ALS) remain unevenly available globally. Here we present CHMv2, a global, meter-resolution canopy height map derived from high-resolution optical satellite imagery using a depth-estimation model built on DINOv3 and trained against ALS canopy height models. Compared to existing products, CHMv2 substantially improves accuracy, reduces bias in tall forests, and better preserves fine-scale structure such as canopy edges and gaps. These gains are enabled by a large expansion of geographically diverse training data, automated data curation and registration, and a loss formulation and data sampling strategy tailored to canopy height distributions. We validate CHMv2 against independent ALS test sets and against tens of millions of GEDI and ICESat-2 observations, demonstrating consistent performance across major forest biomes.

