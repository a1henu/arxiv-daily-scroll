---
layout: default
title: M-SGWR: Multiscale Similarity and Geographically Weighted Regression
---

# M-SGWR: Multiscale Similarity and Geographically Weighted Regression
**arXiv**：[2601.19888v1](https://arxiv.org/abs/2601.19888) · [PDF](https://arxiv.org/pdf/2601.19888.pdf)  
**作者**：M. Naser Lessani, Zhenlong Li, Manzhu Yu, Helen Greatrex, Chan Shen  

**一句话要点**：提出M-SGWR框架，结合地理邻近与属性相似性以改进空间回归建模。

**关键词**：空间回归, 地理加权回归, 多尺度建模, 属性相似性, 局部回归, 空间分析

## 3 点简述
- 核心问题：传统空间回归模型仅依赖地理邻近，难以捕捉全球化下的复杂空间交互。
- 方法要点：构建地理和属性权重矩阵，通过优化参数alpha灵活组合两者，支持多尺度效应。
- 实验或效果：模拟与实证应用显示，M-SGWR在拟合优度上优于GWR、SGWR和MGWR。

## 摘要（原文）

> The first law of geography is a cornerstone of spatial analysis, emphasizing that nearby and related locations tend to be more similar, however, defining what constitutes "near" and "related" remains challenging, as different phenomena exhibit distinct spatial patterns. Traditional local regression models, such as Geographically Weighted Regression (GWR) and Multiscale GWR (MGWR), quantify spatial relationships solely through geographic proximity. In an era of globalization and digital connectivity, however, geographic proximity alone may be insufficient to capture how locations are interconnected. To address this limitation, we propose a new multiscale local regression framework, termed M-SGWR, which characterizes spatial interaction across two dimensions: geographic proximity and attribute (variable) similarity. For each predictor, geographic and attribute-based weight matrices are constructed separately and then combined using an optimized parameter, alpha, which governs their relative contribution to local model fitting. Analogous to variable-specific bandwidths in MGWR, the optimal alpha varies by predictor, allowing the model to flexibly account for geographic, mixed, or non-spatial (remote similarity) effects. Results from two simulation experiments and one empirical application demonstrate that M-SGWR consistently outperforms GWR, SGWR, and MGWR across all goodness-of-fit metrics.

