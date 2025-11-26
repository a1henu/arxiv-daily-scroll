---
layout: default
title: SX-GeoTree: Self-eXplaining Geospatial Regression Tree Incorporating the Spatial Similarity of Feature Attributions
---

# SX-GeoTree: Self-eXplaining Geospatial Regression Tree Incorporating the Spatial Similarity of Feature Attributions
**arXiv**：[2511.19845v1](https://arxiv.org/abs/2511.19845) · [PDF](https://arxiv.org/pdf/2511.19845.pdf)  
**作者**：Chaogui Kang, Lijian Luo, Qingfeng Guan, Yu Liu  

**一句话要点**：提出SX-GeoTree自解释地理空间回归树，以解决空间依赖捕捉和解释稳定性问题。

**关键词**：地理空间回归树, 自解释模型, 空间相似性, 模块化优化, SHAP归因, 地理加权回归

## 3 点简述
- 决策树在表格预测中难以捕捉空间依赖和提供稳定解释。
- 方法结合杂质减少、空间残差控制和基于网络模块化的解释鲁棒性优化。
- 实验显示预测精度接近决策树，同时提升空间残差均匀性和解释共识。

## 摘要（原文）

> Decision trees remain central for tabular prediction but struggle with (i) capturing spatial dependence and (ii) producing locally stable (robust) explanations. We present SX-GeoTree, a self-explaining geospatial regression tree that integrates three coupled objectives during recursive splitting: impurity reduction (MSE), spatial residual control (global Moran's I), and explanation robustness via modularity maximization on a consensus similarity network formed from (a) geographically weighted regression (GWR) coefficient distances (stimulus-response similarity) and (b) SHAP attribution distances (explanatory similarity). We recast local Lipschitz continuity of feature attributions as a network community preservation problem, enabling scalable enforcement of spatially coherent explanations without per-sample neighborhood searches. Experiments on two exemplar tasks (county-level GDP in Fujian, n=83; point-wise housing prices in Seattle, n=21,613) show SX-GeoTree maintains competitive predictive accuracy (within 0.01 $R^{2}$ of decision trees) while improving residual spatial evenness and doubling attribution consensus (modularity: Fujian 0.19 vs 0.09; Seattle 0.10 vs 0.05). Ablation confirms Moran's I and modularity terms are complementary; removing either degrades both spatial residual structure and explanation stability. The framework demonstrates how spatial similarity - extended beyond geometric proximity through GWR-derived local relationships - can be embedded in interpretable models, advancing trustworthy geospatial machine learning and offering a transferable template for domain-aware explainability.

