---
layout: default
title: Reflectance Multispectral Imaging for Soil Composition Estimation and USDA Texture Classification
---

# Reflectance Multispectral Imaging for Soil Composition Estimation and USDA Texture Classification
**arXiv**：[2602.22829v1](https://arxiv.org/abs/2602.22829) · [PDF](https://arxiv.org/pdf/2602.22829.pdf)  
**作者**：G. A. S. L Ranasinghe, J. A. S. T. Jayakody, M. C. L. De Silva, G. Thilakarathne, G. M. R. I. Godaliyadda, H. M. V. R. Herath, M. P. B. Ekanayake, S. K. Navaratnarajah  

**一句话要点**：提出基于反射多光谱成像的土壤成分估计与USDA质地分类方法，以解决传统测试缓慢且成本高的问题。

**关键词**：多光谱成像, 土壤质地分类, USDA质地三角形, 回归模型, 非破坏性检测, 精准农业

## 3 点简述
- 核心问题：土壤质地传统检测方法缓慢、劳动密集，现有传感技术成本高或分辨率不足，难以支持田间规模部署。
- 方法要点：开发低成本多光谱成像系统（365-940 nm，13个波段），结合回归模型估计黏土、粉土、砂土百分比，并直接或间接分类USDA质地类别。
- 实验或效果：在混合数据上评估，成分预测R²达0.99，质地分类准确率超过99%，表明方法准确、非破坏且适合田间部署。

## 摘要（原文）

> Soil texture is a foundational attribute that governs water availability and erosion in agriculture, as well as load bearing capacity, deformation response, and shrink-swell risk in geotechnical engineering. Yet texture is still typically determined by slow and labour intensive laboratory particle size tests, while many sensing alternatives are either costly or too coarse to support routine field scale deployment. This paper proposes a robust and field deployable multispectral imaging (MSI) system and machine learning framework for predicting soil composition and the United States Department of Agriculture (USDA) texture classes. The proposed system uses a cost effective in-house MSI device operating from 365 nm to 940 nm to capture thirteen spectral bands, which effectively capture the spectral properties of soil texture. Regression models use the captured spectral properties to estimate clay, silt, and sand percentages, while a direct classifier predicts one of the twelve USDA textural classes. Indirect classification is obtained by mapping the regressed compositions to texture classes via the USDA soil texture triangle. The framework is evaluated on mixture data by mixing clay, silt, and sand in varying proportions, using the USDA classification triangle as a basis. Experimental results show that the proposed approach achieves a coefficient of determination R^2 up to 0.99 for composition prediction and over 99% accuracy for texture classification. These findings indicate that MSI combined with data-driven modeling can provide accurate, non-destructive, and field deployable soil texture characterization suitable for geotechnical screening and precision agriculture.

