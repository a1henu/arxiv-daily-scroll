---
layout: default
title: EAGLE: Episodic Appearance- and Geometry-aware Memory for Unified 2D-3D Visual Query Localization in Egocentric Vision
---

# EAGLE: Episodic Appearance- and Geometry-aware Memory for Unified 2D-3D Visual Query Localization in Egocentric Vision
**arXiv**：[2511.08007v1](https://arxiv.org/abs/2511.08007) · [PDF](https://arxiv.org/pdf/2511.08007.pdf)  
**作者**：Yifei Cao, Yu Liu, Guolong Wang, Zhu Liu, Kai Wang, Xianjie Zhang, Jizhe Yu, Xun Tu  

**一句话要点**：提出EAGLE框架，利用外观和几何感知记忆实现统一2D-3D视觉查询定位，解决自我中心视觉中的挑战。

**关键词**：自我中心视觉, 视觉查询定位, 记忆机制, 2D-3D统一, 外观变化建模, 几何感知

## 3 点简述
- 核心问题：自我中心视觉查询定位因相机运动、视角变化和外观变化而困难。
- 方法要点：结合外观感知元学习记忆和几何感知定位记忆，支持目标外观的长期和短期建模。
- 实验或效果：在Ego4D-VQ基准上实现最先进性能，提升检索精度和3D空间投影效率。

## 摘要（原文）

> Egocentric visual query localization is vital for embodied AI and VR/AR, yet remains challenging due to camera motion, viewpoint changes, and appearance variations. We present EAGLE, a novel framework that leverages episodic appearance- and geometry-aware memory to achieve unified 2D-3D visual query localization in egocentric vision. Inspired by avian memory consolidation, EAGLE synergistically integrates segmentation guided by an appearance-aware meta-learning memory (AMM), with tracking driven by a geometry-aware localization memory (GLM). This memory consolidation mechanism, through structured appearance and geometry memory banks, stores high-confidence retrieval samples, effectively supporting both long- and short-term modeling of target appearance variations. This enables precise contour delineation with robust spatial discrimination, leading to significantly improved retrieval accuracy. Furthermore, by integrating the VQL-2D output with a visual geometry grounded Transformer (VGGT), we achieve a efficient unification of 2D and 3D tasks, enabling rapid and accurate back-projection into 3D space. Our method achieves state-ofthe-art performance on the Ego4D-VQ benchmark.

