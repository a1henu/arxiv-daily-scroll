---
layout: default
title: PlantTraitNet: An Uncertainty-Aware Multimodal Framework for Global-Scale Plant Trait Inference from Citizen Science Data
---

# PlantTraitNet: An Uncertainty-Aware Multimodal Framework for Global-Scale Plant Trait Inference from Citizen Science Data
**arXiv**：[2511.06943v1](https://arxiv.org/abs/2511.06943) · [PDF](https://arxiv.org/pdf/2511.06943.pdf)  
**作者**：Ayushi Sharma, Johanna Trost, Daniel Lusk, Johannes Dollinger, Julian Schrader, Christian Rossi, Javier Lopatin, Etienne Laliberté, Simon Haberstroh, Jana Eichel, Daniel Mederer, Jose Miguel Cerda-Paredes, Shyam S. Phartyal, Lisa-Maricia Schwarz, Anja Linstädter, Maria Conceição Caldeira, Teja Kattenborn  

**一句话要点**：提出PlantTraitNet以从公民科学照片中推断全球植物性状

**关键词**：植物性状推断, 多模态深度学习, 不确定性感知, 公民科学数据, 全球地图生成, 弱监督学习

## 3 点简述
- 核心问题：全球植物性状地图受限于实地测量成本高和覆盖稀疏。
- 方法要点：使用多模态多任务不确定性感知深度学习框架进行弱监督预测。
- 实验或效果：在独立数据上验证，优于现有全球性状产品。

## 摘要（原文）

> Global plant maps of plant traits, such as leaf nitrogen or plant height, are
> essential for understanding ecosystem processes, including the carbon and
> energy cycles of the Earth system. However, existing trait maps remain limited
> by the high cost and sparse geographic coverage of field-based measurements.
> Citizen science initiatives offer a largely untapped resource to overcome these
> limitations, with over 50 million geotagged plant photographs worldwide
> capturing valuable visual information on plant morphology and physiology. In
> this study, we introduce PlantTraitNet, a multi-modal, multi-task
> uncertainty-aware deep learning framework that predictsfour key plant traits
> (plant height, leaf area, specific leaf area, and nitrogen content) from
> citizen science photos using weak supervision. By aggregating individual trait
> predictions across space, we generate global maps of trait distributions. We
> validate these maps against independent vegetation survey data (sPlotOpen) and
> benchmark them against leading global trait products. Our results show that
> PlantTraitNet consistently outperforms existing trait maps across all evaluated
> traits, demonstrating that citizen science imagery, when integrated with
> computer vision and geospatial AI, enables not only scalable but also more
> accurate global trait mapping. This approach offers a powerful new pathway for
> ecological research and Earth system modeling.

