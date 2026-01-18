---
layout: default
title: Lunar-G2R: Geometry-to-Reflectance Learning for High-Fidelity Lunar BRDF Estimation
---

# Lunar-G2R: Geometry-to-Reflectance Learning for High-Fidelity Lunar BRDF Estimation
**arXiv**：[2601.10449v1](https://arxiv.org/abs/2601.10449) · [PDF](https://arxiv.org/pdf/2601.10449.pdf)  
**作者**：Clementine Grethen, Nicolas Menga, Roland Brochard, Geraldine Morin, Simone Gasparini, Jeremy Lebreton, Manuel Sanchez Gestido  

**一句话要点**：提出Lunar-G2R框架，从地形几何直接预测月球表面空间变化BRDF参数，以提升渲染保真度。

**关键词**：月球表面渲染, 空间变化BRDF估计, 几何到反射学习, 可微分渲染, 数字高程模型, 光测误差优化

## 3 点简述
- 核心问题：现有月球渲染模型参数估计困难，无法捕捉局部反射变化，限制光测真实感。
- 方法要点：基于U-Net和可微分渲染，从数字高程模型学习空间变化BRDF，无需多视图图像或专用硬件。
- 实验或效果：在Tycho陨石坑测试中，光测误差降低38%，PSNR、SSIM和感知相似度均优于基线。

## 摘要（原文）

> We address the problem of estimating realistic, spatially varying reflectance for complex planetary surfaces such as the lunar regolith, which is critical for high-fidelity rendering and vision-based navigation. Existing lunar rendering pipelines rely on simplified or spatially uniform BRDF models whose parameters are difficult to estimate and fail to capture local reflectance variations, limiting photometric realism. We propose Lunar-G2R, a geometry-to-reflectance learning framework that predicts spatially varying BRDF parameters directly from a lunar digital elevation model (DEM), without requiring multi-view imagery, controlled illumination, or dedicated reflectance-capture hardware at inference time. The method leverages a U-Net trained with differentiable rendering to minimize photometric discrepancies between real orbital images and physically based renderings under known viewing and illumination geometry. Experiments on a geographically held-out region of the Tycho crater show that our approach reduces photometric error by 38 % compared to a state-of-the-art baseline, while achieving higher PSNR and SSIM and improved perceptual similarity, capturing fine-scale reflectance variations absent from spatially uniform models. To our knowledge, this is the first method to infer a spatially varying reflectance model directly from terrain geometry.

