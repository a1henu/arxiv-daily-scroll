---
layout: default
title: A Statistical Approach for Modeling Irregular Multivariate Time Series with Missing Observations
---

# A Statistical Approach for Modeling Irregular Multivariate Time Series with Missing Observations
**arXiv**：[2602.19531v1](https://arxiv.org/abs/2602.19531) · [PDF](https://arxiv.org/pdf/2602.19531.pdf)  
**作者**：Dingyi Nie, Yixing Wu, C. -C. Jay Kuo  

**一句话要点**：提出基于时间无关统计特征的方法，以高效处理不规则多元时间序列分类问题。

**关键词**：不规则时间序列, 缺失值处理, 统计特征提取, 医疗预测, 分类任务, 计算效率

## 3 点简述
- 核心问题：不规则多元时间序列中的缺失值对预测建模构成挑战，尤其在医疗领域。
- 方法要点：提取每变量的均值、标准差及变化统计特征，消除时间轴，使用标准分类器。
- 实验或效果：在四个生物医学数据集上超越复杂模型，计算复杂度低，缺失模式可编码预测信号。

## 摘要（原文）

> Irregular multivariate time series with missing values present significant challenges for predictive modeling in domains such as healthcare. While deep learning approaches often focus on temporal interpolation or complex architectures to handle irregularities, we propose a simpler yet effective alternative: extracting time-agnostic summary statistics to eliminate the temporal axis. Our method computes four key features per variable-mean and standard deviation of observed values, as well as the mean and variability of changes between consecutive observations to create a fixed-dimensional representation. These features are then utilized with standard classifiers, such as logistic regression and XGBoost. Evaluated on four biomedical datasets (PhysioNet Challenge 2012, 2019, PAMAP2, and MIMIC-III), our approach achieves state-of-the-art performance, surpassing recent transformer and graph-based models by 0.5-1.7% in AUROC/AUPRC and 1.1-1.7% in accuracy/F1-score, while reducing computational complexity. Ablation studies demonstrate that feature extraction-not classifier choice-drives performance gains, and our summary statistics outperform raw/imputed input in most benchmarks. In particular, we identify scenarios where missing patterns themselves encode predictive signals, as in sepsis prediction (PhysioNet, 2019), where missing indicators alone can achieve 94.2% AUROC with XGBoost, only 1.6% lower than using original raw data as input. Our results challenge the necessity of complex temporal modeling when task objectives permit time-agnostic representations, providing an efficient and interpretable solution for irregular time series classification.

