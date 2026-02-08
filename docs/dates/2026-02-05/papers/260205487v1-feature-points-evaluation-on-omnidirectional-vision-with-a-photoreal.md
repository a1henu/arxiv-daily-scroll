---
layout: default
title: Feature points evaluation on omnidirectional vision with a photorealistic fisheye sequence -- A report on experiments done in 2014
---

# Feature points evaluation on omnidirectional vision with a photorealistic fisheye sequence -- A report on experiments done in 2014
**arXiv**：[2602.05487v1](https://arxiv.org/abs/2602.05487) · [PDF](https://arxiv.org/pdf/2602.05487.pdf)  
**作者**：Julien Moreau, S. Ambellouis, Yassine Ruichek  

**一句话要点**：评估鱼眼图像特征点检测与描述方法，支持车载鱼眼视觉自标定与里程计

**关键词**：鱼眼图像, 特征点检测, 视觉里程计, 自标定, 数据集

## 3 点简述
- 核心问题：鱼眼图像特征点检测与描述在自标定中面临先有鸡还是先有蛋的循环依赖问题
- 方法要点：提供PFSeq数据集和详细实验，比较标准特征算法在鱼眼图像上的性能
- 实验或效果：未提出新算法，但为鱼眼视觉里程计和立体视觉提供实验基准，数据集公开可用

## 摘要（原文）

> What is this report: This is a scientific report, contributing with a detailed bibliography, a dataset which we will call now PFSeq for ''Photorealistic Fisheye Sequence'' and make available at https://doi.org/10. 57745/DYIVVU, and comprehensive experiments. This work should be considered as a draft, and has been done during my PhD thesis ''Construction of 3D models from fisheye video data-Application to the localisation in urban area'' in 2014 [Mor16]. These results have never been published. The aim was to find the best features detector and descriptor for fisheye images, in the context of selfcalibration, with cameras mounted on the top of a car and aiming at the zenith (to proceed then fisheye visual odometry and stereovision in urban scenes). We face a chicken and egg problem, because we can not take advantage of an accurate projection model for an optimal features detection and description, and we rightly need good features to perform the calibration (i.e. to compute the accurate projection model of the camera). What is not this report: It does not contribute with new features algorithm. It does not compare standard features algorithms to algorithms designed for omnidirectional images (unfortunately). It has not been peer-reviewed. Discussions have been translated and enhanced but the experiments have not been run again and the report has not been updated accordingly to the evolution of the state-of-the-art (read this as a 2014 report).

