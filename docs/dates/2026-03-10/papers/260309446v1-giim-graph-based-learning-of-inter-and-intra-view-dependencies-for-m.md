---
layout: default
title: GIIM: Graph-based Learning of Inter- and Intra-view Dependencies for Multi-view Medical Image Diagnosis
---

# GIIM: Graph-based Learning of Inter- and Intra-view Dependencies for Multi-view Medical Image Diagnosis
**arXiv**：[2603.09446v1](https://arxiv.org/abs/2603.09446) · [PDF](https://arxiv.org/pdf/2603.09446.pdf)  
**作者**：Tran Bao Sam, Hung Vu, Dao Trung Kien, Tran Dat Dang, Van Ha Tang, Steven Truong  

**一句话要点**：提出GIIM图学习方法，以建模多视图医学图像诊断中的视图内和视图间依赖关系。

**关键词**：多视图医学图像诊断, 图学习, 视图内依赖, 视图间动态, 缺失数据处理, 计算机辅助诊断

## 3 点简述
- 核心问题：现有多视图CADx方法忽略异常在单视图内和跨视图间的复杂依赖关系，且数据不完整影响预测可靠性。
- 方法要点：GIIM基于图学习，同时捕获视图内依赖和视图间动态变化，并集成技术处理缺失数据。
- 实验或效果：在CT、MRI和乳腺X光等多种模态上评估，GIIM显著提升诊断准确性和鲁棒性。

## 摘要（原文）

> Computer-aided diagnosis (CADx) has become vital in medical imaging, but automated systems often struggle to replicate the nuanced process of clinical interpretation. Expert diagnosis requires a comprehensive analysis of how abnormalities relate to each other across various views and time points, but current multi-view CADx methods frequently overlook these complex dependencies. Specifically, they fail to model the crucial relationships within a single view and the dynamic changes lesions exhibit across different views. This limitation, combined with the common challenge of incomplete data, greatly reduces their predictive reliability. To address these gaps, we reframe the diagnostic task as one of relationship modeling and propose GIIM, a novel graph-based approach. Our framework is uniquely designed to simultaneously capture both critical intra-view dependencies between abnormalities and inter-view dynamics. Furthermore, it ensures diagnostic robustness by incorporating specific techniques to effectively handle missing data, a common clinical issue. We demonstrate the generality of this approach through extensive evaluations on diverse imaging modalities, including CT, MRI, and mammography. The results confirm that our GIIM model significantly enhances diagnostic accuracy and robustness over existing methods, establishing a more effective framework for future CADx systems.

