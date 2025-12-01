---
layout: default
title: Learning to Predict Aboveground Biomass from RGB Images with 3D Synthetic Scenes
---

# Learning to Predict Aboveground Biomass from RGB Images with 3D Synthetic Scenes
**arXiv**：[2511.23249v1](https://arxiv.org/abs/2511.23249) · [PDF](https://arxiv.org/pdf/2511.23249.pdf)  
**作者**：Silvia Zuffi  

**一句话要点**：提出基于单张地面RGB图像预测地上生物量的学习方法，利用3D合成场景数据实现森林监测。

**关键词**：地上生物量估计, RGB图像分析, 3D合成场景, 密集预测, 森林监测, 公民科学

## 3 点简述
- 核心问题：传统地上生物量估计方法依赖人工测量或遥感，在密集植被中受限，需更高效解决方案。
- 方法要点：将预测任务定义为密集预测，引入生物量密度图，利用合成3D数据集训练模型从RGB图像直接估计生物量。
- 实验或效果：在合成数据上中位误差为1.22 kg/m²，真实图像上为1.94 kg/m²，首次实现单RGB图像直接估计生物量。

## 摘要（原文）

> Forests play a critical role in global ecosystems by supporting biodiversity and mitigating climate change via carbon sequestration. Accurate aboveground biomass (AGB) estimation is essential for assessing carbon storage and wildfire fuel loads, yet traditional methods rely on labor-intensive field measurements or remote sensing approaches with significant limitations in dense vegetation. In this work, we propose a novel learning-based method for estimating AGB from a single ground-based RGB image. We frame this as a dense prediction task, introducing AGB density maps, where each pixel represents tree biomass normalized by the plot area and each tree's image area. We leverage the recently introduced synthetic 3D SPREAD dataset, which provides realistic forest scenes with per-image tree attributes (height, trunk and canopy diameter) and instance segmentation masks. Using these assets, we compute AGB via allometric equations and train a model to predict AGB density maps, integrating them to recover the AGB estimate for the captured scene. Our approach achieves a median AGB estimation error of 1.22 kg/m^2 on held-out SPREAD data and 1.94 kg/m^2 on a real-image dataset. To our knowledge, this is the first method to estimate aboveground biomass directly from a single RGB image, opening up the possibility for a scalable, interpretable, and cost-effective solution for forest monitoring, while also enabling broader participation through citizen science initiatives.

