---
layout: default
title: TopoMaskV3: 3D Mask Head with Dense Offset and Height Predictions for Road Topology Understanding
---

# TopoMaskV3: 3D Mask Head with Dense Offset and Height Predictions for Road Topology Understanding
**arXiv**：[2603.01558v1](https://arxiv.org/abs/2603.01558) · [PDF](https://arxiv.org/pdf/2603.01558.pdf)  
**作者**：Muhammet Esat Kalfaoglu, Halil Ibrahim Ozturk, Ozsel Kilinc, Alptekin Temizel  

**一句话要点**：提出TopoMaskV3，通过密集偏移和高度预测头实现鲁棒的3D道路拓扑理解。

**关键词**：道路拓扑理解, 3D预测, 密集预测头, 地理数据泄漏, 长距离基准, 掩码表示

## 3 点简述
- 核心问题：现有基于掩码的方法限于2D预测，存在离散化伪影，需参数化头融合。
- 方法要点：引入密集偏移场和高度图，在BEV分辨率内进行亚网格校正和直接3D估计。
- 实验或效果：在无地理重叠基准上达到28.5 OLS，优于先前方法，分析显示掩码表示对地理过拟合更鲁棒。

## 摘要（原文）

> Mask-based paradigms for road topology understanding, such as TopoMaskV2, offer a complementary alternative to query-based methods by generating centerlines via a dense rasterized intermediate representation. However, prior work was limited to 2D predictions and suffered from severe discretization artifacts, necessitating fusion with parametric heads. We introduce TopoMaskV3, which advances this pipeline into a robust, standalone 3D predictor via two novel dense prediction heads: a dense offset field for sub-grid discretization correction within the existing BEV resolution, and a dense height map for direct 3D estimation. Beyond the architecture, we are the first to address geographic data leakage in road topology evaluation by introducing (1) geographically distinct splits to prevent memorization and ensure fair generalization, and (2) a long-range (+/-100 m) benchmark. TopoMaskV3 achieves state-of-the-art 28.5 OLS on this geographically disjoint benchmark, surpassing all prior methods. Our analysis shows that the mask representation is more robust to geographic overfitting than Bezier, while LiDAR fusion is most beneficial at long range and exhibits larger relative gains on the overlapping original split, suggesting overlap-induced memorization effects.

