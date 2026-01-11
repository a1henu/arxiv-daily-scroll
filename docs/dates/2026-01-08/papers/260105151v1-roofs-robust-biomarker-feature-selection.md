---
layout: default
title: ROOFS: RObust biOmarker Feature Selection
---

# ROOFS: RObust biOmarker Feature Selection
**arXiv**：[2601.05151v1](https://arxiv.org/abs/2601.05151) · [PDF](https://arxiv.org/pdf/2601.05151.pdf)  
**作者**：Anastasiia Bakhmach, Paul Dufossé, Andrea Vaglio, Florence Monville, Laurent Greillier, Fabrice Barlési, Sébastien Benzekry  

**一句话要点**：提出ROOFS包以解决生物医学数据中特征选择方法选择难题

**关键词**：特征选择, 生物医学数据分析, Python包, 基准测试, 临床模型, 鲁棒性评估

## 3 点简述
- 核心问题：高维特征、小样本、多重共线性和缺失值使特征选择复杂且性能不稳定
- 方法要点：ROOFS包通过基准测试评估多种特征选择方法，生成包含预测性能、稳定性和可靠性等指标的全面报告
- 实验或效果：在PIONeeR临床试验数据中，识别出基于t检验和逻辑回归p值联合的过滤方法为最优，优于LASSO等常用方法

## 摘要（原文）

> Feature selection (FS) is essential for biomarker discovery and in the analysis of biomedical datasets. However, challenges such as high-dimensional feature space, low sample size, multicollinearity, and missing values make FS non-trivial. Moreover, FS performances vary across datasets and predictive tasks. We propose roofs, a Python package available at https://gitlab.inria.fr/compo/roofs, designed to help researchers in the choice of FS method adapted to their problem. Roofs benchmarks multiple FS methods on the user's data and generates reports that summarize a comprehensive set of evaluation metrics, including downstream predictive performance estimated using optimism correction, stability, reliability of individual features, and true positive and false positive rates assessed on semi-synthetic data with a simulated outcome. We demonstrate the utility of roofs on data from the PIONeeR clinical trial, aimed at identifying predictors of resistance to anti-PD-(L)1 immunotherapy in lung cancer. The PIONeeR dataset contained 374 multi-source blood and tumor biomarkers from 435 patients. A reduced subset of 214 features was obtained through iterative variance inflation factor pre-filtering. Of the 34 FS methods gathered in roofs, we evaluated 23 in combination with 11 classifiers (253 models in total) and identified a filter based on the union of Benjamini-Hochberg false discovery rate-adjusted p-values from t-test and logistic regression as the optimal approach, outperforming other methods including the widely used LASSO. We conclude that comprehensive benchmarking with roofs has the potential to improve the robustness and reproducibility of FS discoveries and increase the translational value of clinical models.

