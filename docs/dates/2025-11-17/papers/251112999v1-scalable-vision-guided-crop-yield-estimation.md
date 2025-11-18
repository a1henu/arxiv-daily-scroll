---
layout: default
title: Scalable Vision-Guided Crop Yield Estimation
---

# Scalable Vision-Guided Crop Yield Estimation
**arXiv**：[2511.12999v1](https://arxiv.org/abs/2511.12999) · [PDF](https://arxiv.org/pdf/2511.12999.pdf)  
**作者**：Harrison H. Li, Medhanie Irgau, Nabil Janmohamed, Karen Solveig Rieckmann, David B. Lobell  

**一句话要点**：提出基于预测驱动推理的视觉引导方法，以低成本图像提升作物产量估计精度。

**关键词**：作物产量估计, 预测驱动推理, 计算机视觉, 空间校准, 农业监测, 置信区间构建

## 3 点简述
- 核心问题：传统作物产量估计方法耗时，需高效补充数据以改进精度。
- 方法要点：训练计算机视觉模型预测产量，结合空间坐标学习控制函数进行校准。
- 实验或效果：在非洲水稻和玉米田验证，有效样本量最高提升73%，置信区间更短。

## 摘要（原文）

> Precise estimation and uncertainty quantification for average crop yields are critical for agricultural monitoring and decision making. Existing data collection methods, such as crop cuts in randomly sampled fields at harvest time, are relatively time-consuming. Thus, we propose an approach based on prediction-powered inference (PPI) to supplement these crop cuts with less time-consuming field photos. After training a computer vision model to predict the ground truth crop cut yields from the photos, we learn a ``control function" that recalibrates these predictions with the spatial coordinates of each field. This enables fields with photos but not crop cuts to be leveraged to improve the precision of zone-wide average yield estimates. Our control function is learned by training on a dataset of nearly 20,000 real crop cuts and photos of rice and maize fields in sub-Saharan Africa. To improve precision, we pool training observations across different zones within the same first-level subdivision of each country. Our final PPI-based point estimates of the average yield are provably asymptotically unbiased and cannot increase the asymptotic variance beyond that of the natural baseline estimator -- the sample average of the crop cuts -- as the number of fields grows. We also propose a novel bias-corrected and accelerated (BCa) bootstrap to construct accompanying confidence intervals. Even in zones with as few as 20 fields, the point estimates show significant empirical improvement over the baseline, increasing the effective sample size by as much as 73% for rice and by 12-23% for maize. The confidence intervals are accordingly shorter at minimal cost to empirical finite-sample coverage. This demonstrates the potential for relatively low-cost images to make area-based crop insurance more affordable and thus spur investment into sustainable agricultural practices.

