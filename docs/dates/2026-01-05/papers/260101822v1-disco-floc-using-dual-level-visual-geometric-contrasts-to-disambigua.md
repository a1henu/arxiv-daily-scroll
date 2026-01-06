---
layout: default
title: DisCo-FLoc: Using Dual-Level Visual-Geometric Contrasts to Disambiguate Depth-Aware Visual Floorplan Localization
---

# DisCo-FLoc: Using Dual-Level Visual-Geometric Contrasts to Disambiguate Depth-Aware Visual Floorplan Localization
**arXiv**：[2601.01822v1](https://arxiv.org/abs/2601.01822) · [PDF](https://arxiv.org/pdf/2601.01822.pdf)  
**作者**：Shiyong Meng, Tao Zou, Bolei Chen, Chaoxu Mu, Jianxin Wang  

**一句话要点**：提出DisCo-FLoc，利用双层级视觉-几何对比消除简约平面图中重复结构导致的定位歧义。

**关键词**：视觉平面图定位, 对比学习, 深度估计, 歧义消除, 几何匹配, 无监督学习

## 3 点简述
- 核心问题：简约平面图中重复结构导致视觉平面图定位歧义，现有方法依赖昂贵语义标注。
- 方法要点：基于深度估计预测候选定位，通过位置和方向层级对比学习匹配视觉特征与几何结构。
- 实验或效果：在两个标准基准上优于现有语义方法，显著提升鲁棒性和准确性。

## 摘要（原文）

> Since floorplan data is readily available, long-term persistent, and robust to changes in visual appearance, visual Floorplan Localization (FLoc) has garnered significant attention. Existing methods either ingeniously match geometric priors or utilize sparse semantics to reduce FLoc uncertainty. However, they still suffer from ambiguous FLoc caused by repetitive structures within minimalist floorplans. Moreover, expensive but limited semantic annotations restrict their applicability. To address these issues, we propose DisCo-FLoc, which utilizes dual-level visual-geometric Contrasts to Disambiguate depth-aware visual Floc, without requiring additional semantic labels. Our solution begins with a ray regression predictor tailored for ray-casting-based FLoc, predicting a series of FLoc candidates using depth estimation expertise. In addition, a novel contrastive learning method with position-level and orientation-level constraints is proposed to strictly match depth-aware visual features with the corresponding geometric structures in the floorplan. Such matches can effectively eliminate FLoc ambiguity and select the optimal imaging pose from FLoc candidates. Exhaustive comparative studies on two standard visual Floc benchmarks demonstrate that our method outperforms the state-of-the-art semantic-based method, achieving significant improvements in both robustness and accuracy.

