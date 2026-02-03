---
layout: default
title: Automated Discontinuity Set Characterisation in Enclosed Rock Face Point Clouds Using Single-Shot Filtering and Cyclic Orientation Transformation
---

# Automated Discontinuity Set Characterisation in Enclosed Rock Face Point Clouds Using Single-Shot Filtering and Cyclic Orientation Transformation
**arXiv**：[2602.01783v1](https://arxiv.org/abs/2602.01783) · [PDF](https://arxiv.org/pdf/2602.01783.pdf)  
**作者**：Dibyayan Patra, Pasindu Ranasinghe, Bikram Banerjee, Simit Raval  

**一句话要点**：提出单次滤波与循环方位变换方法，以自动表征封闭岩面点云中的结构不连续面集

**关键词**：点云处理, 结构不连续面表征, 单次滤波, 循环方位变换, 层次聚类, 岩体稳定性评估

## 3 点简述
- 核心问题：自动表征封闭岩面点云中的结构不连续面集，以评估岩体稳定性与安全。
- 方法要点：采用单次滤波抑制噪声，循环方位变换处理极坐标数据，结合层次聚类自动识别不连续面集。
- 实验或效果：在真实矿场数据上验证，方位估计误差低于3°，优于现有自动结构映射技术。

## 摘要（原文）

> Characterisation of structural discontinuity sets in exposed rock faces of underground mine cavities is essential for assessing rock-mass stability, excavation safety, and operational efficiency. UAV and other mobile laser-scanning techniques provide efficient means of collecting point clouds from rock faces. However, the development of a robust and efficient approach for automatic characterisation of discontinuity sets in real-world scenarios, like fully enclosed rock faces in cavities, remains an open research problem. In this study, a new approach is proposed for automatic discontinuity set characterisation that uses a single-shot filtering strategy, an innovative cyclic orientation transformation scheme and a hierarchical clustering technique. The single-shot filtering step isolates planar regions while robustly suppressing noise and high-curvature artefacts in one pass using a signal-processing technique. To address the limitations of Cartesian clustering on polar orientation data, a cyclic orientation transformation scheme is developed, enabling accurate representation of dip angle and dip direction in Cartesian space. The transformed orientations are then characterised into sets using a hierarchical clustering technique, which handles varying density distributions and identifies clusters without requiring user-defined set numbers. The accuracy of the method is validated on real-world mine stope and against ground truth obtained using manually handpicked discontinuity planes identified with the Virtual Compass tool, as well as widely used automated structure mapping techniques. The proposed approach outperforms the other techniques by exhibiting the lowest mean absolute error in estimating discontinuity set orientations in real-world stope data with errors of 1.95° and 2.20° in nominal dip angle and dip direction, respectively, and dispersion errors lying below 3°.

