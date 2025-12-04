---
layout: default
title: Difference Decomposition Networks for Infrared Small Target Detection
---

# Difference Decomposition Networks for Infrared Small Target Detection
**arXiv**：[2512.03470v1](https://arxiv.org/abs/2512.03470) · [PDF](https://arxiv.org/pdf/2512.03470.pdf)  
**作者**：Chen Hu, Mingyu Zhou, Shuai Yuan, Hongbo Hu, Xiangyu Qiu, Junhai Luo, Tian Pu, Xiyin Li  

**一句话要点**：提出差异分解网络以解决红外小目标检测中目标纹理缺失和背景干扰问题。

**关键词**：红外小目标检测, 基分解模块, 时空差异分解网络, U形架构, 运动信息融合, 多帧检测

## 3 点简述
- 核心问题：红外小目标检测面临目标纹理不明显和背景杂波严重的挑战，导致目标被背景掩盖。
- 方法要点：基于基分解提出可扩展的轻量模块BDM，并扩展为SD²M、SD³M和TD²M，构建SD²Net和STD²Net网络。
- 实验或效果：在SISTD和MISTD数据集上实现SOTA性能，STD²Net在MISTD上mIoU达87.68%，优于SD²Net的64.97%。

## 摘要（原文）

> Infrared small target detection (ISTD) faces two major challenges: a lack of discernible target texture and severe background clutter, which results in the background obscuring the target. To enhance targets and suppress backgrounds, we propose the Basis Decomposition Module (BDM) as an extensible and lightweight module based on basis decomposition, which decomposes a complex feature into several basis features and enhances certain information while eliminating redundancy. Extending BDM leads to a series of modules, including the Spatial Difference Decomposition Module (SD$^\mathrm{2}$M), Spatial Difference Decomposition Downsampling Module (SD$^\mathrm{3}$M), and Temporal Difference Decomposition Module (TD$^\mathrm{2}$M). Based on these modules, we develop the Spatial Difference Decomposition Network (SD$^\mathrm{2}$Net) for single-frame ISTD (SISTD) and the Spatiotemporal Difference Decomposition Network (STD$^\mathrm{2}$Net) for multi-frame ISTD (MISTD). SD$^\mathrm{2}$Net integrates SD$^\mathrm{2}$M and SD$^\mathrm{3}$M within an adapted U-shaped architecture. We employ TD$^\mathrm{2}$M to introduce motion information, which transforms SD$^\mathrm{2}$Net into STD$^\mathrm{2}$Net. Extensive experiments on SISTD and MISTD datasets demonstrate state-of-the-art (SOTA) performance. On the SISTD task, SD$^\mathrm{2}$Net performs well compared to most established networks. On the MISTD datasets, STD$^\mathrm{2}$Net achieves a mIoU of 87.68\%, outperforming SD$^\mathrm{2}$Net, which achieves a mIoU of 64.97\%. Our codes are available: https://github.com/greekinRoma/IRSTD_HC_Platform.

