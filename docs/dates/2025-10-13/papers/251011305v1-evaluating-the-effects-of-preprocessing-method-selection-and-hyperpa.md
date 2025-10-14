---
layout: default
title: Evaluating the effects of preprocessing, method selection, and hyperparameter tuning on SAR-based flood mapping and water depth estimation
---

# Evaluating the effects of preprocessing, method selection, and hyperparameter tuning on SAR-based flood mapping and water depth estimation
**arXiv**：[2510.11305v1](https://arxiv.org/abs/2510.11305) · [PDF](https://arxiv.org/pdf/2510.11305.pdf)  
**作者**：Jean-Paul Travert, Cédric Goeury, Sébastien Boyaval, Vito Bacchi, Fabrice Zaoui  

**一句话要点**：评估预处理、方法选择与超参数调优对SAR洪水制图和水深估计的影响

**关键词**：SAR图像处理, 洪水制图, 水深估计, 超参数调优, 集成方法, 不确定性分析

## 3 点简述
- 核心问题：SAR图像洪水制图和水深估计中方法选择与超参数调优的不确定性影响。
- 方法要点：采用集成方法评估预处理、洪水制图和水深估计步骤及其超参数。
- 实验或效果：基于法国加龙河洪水事件，结果显示方法选择对洪水范围和水深估计有显著影响。

## 摘要（原文）

> Flood mapping and water depth estimation from Synthetic Aperture Radar (SAR)
> imagery are crucial for calibrating and validating hydraulic models. This study
> uses SAR imagery to evaluate various preprocessing (especially speckle noise
> reduction), flood mapping, and water depth estimation methods. The impact of
> the choice of method at different steps and its hyperparameters is studied by
> considering an ensemble of preprocessed images, flood maps, and water depth
> fields. The evaluation is conducted for two flood events on the Garonne River
> (France) in 2019 and 2021, using hydrodynamic simulations and in-situ
> observations as reference data. Results show that the choice of speckle filter
> alters flood extent estimations with variations of several square kilometers.
> Furthermore, the selection and tuning of flood mapping methods also affect
> performance. While supervised methods outperformed unsupervised ones, tuned
> unsupervised approaches (such as local thresholding or change detection) can
> achieve comparable results. The compounded uncertainty from preprocessing and
> flood mapping steps also introduces high variability in the water depth field
> estimates. This study highlights the importance of considering the entire
> processing pipeline, encompassing preprocessing, flood mapping, and water depth
> estimation methods and their associated hyperparameters. Rather than relying on
> a single configuration, adopting an ensemble approach and accounting for
> methodological uncertainty should be privileged. For flood mapping, the method
> choice has the most influence. For water depth estimation, the most influential
> processing step was the flood map input resulting from the flood mapping step
> and the hyperparameters of the methods.

