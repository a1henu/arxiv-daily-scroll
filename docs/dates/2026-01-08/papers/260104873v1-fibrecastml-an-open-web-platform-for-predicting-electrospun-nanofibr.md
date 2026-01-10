---
layout: default
title: FibreCastML: An Open Web Platform for Predicting Electrospun Nanofibre Diameter Distributions
---

# FibreCastML: An Open Web Platform for Predicting Electrospun Nanofibre Diameter Distributions
**arXiv**：[2601.04873v1](https://arxiv.org/abs/2601.04873) · [PDF](https://arxiv.org/pdf/2601.04873.pdf)  
**作者**：Elisa Roldan, Kirstie Andrews, Stephen M. Richardson, Reyhaneh Fatahian, Glen Cooper, Rasool Erfani, Tasneem Sabir, Neil D. Reeves  

**一句话要点**：提出FibreCastML以预测静电纺丝纳米纤维直径分布，支持组织工程等应用优化。

**关键词**：静电纺丝, 纳米纤维直径分布预测, 机器学习框架, 可解释性分析, 组织工程, 数据驱动优化

## 3 点简述
- 核心问题：现有机器学习方法仅预测平均纤维直径，忽略影响支架性能的完整分布。
- 方法要点：基于六项标准参数训练非线性模型，使用元数据集和可解释性分析预测分布。
- 实验或效果：模型在多种聚合物上R²超0.91，实验验证显示预测与实测分布高度一致。

## 摘要（原文）

> Electrospinning is a scalable technique for producing fibrous scaffolds with tunable micro- and nanoscale architectures for applications in tissue engineering, drug delivery, and wound care. While machine learning (ML) has been used to support electrospinning process optimisation, most existing approaches predict only mean fibre diameters, neglecting the full diameter distribution that governs scaffold performance. This work presents FibreCastML, an open, distribution-aware ML framework that predicts complete fibre diameter spectra from routinely reported electrospinning parameters and provides interpretable insights into process structure relationships.
>   A meta-dataset comprising 68538 individual fibre diameter measurements extracted from 1778 studies across 16 biomedical polymers was curated. Six standard processing parameters, namely solution concentration, applied voltage, flow rate, tip to collector distance, needle diameter, and collector rotation speed, were used to train seven ML models using nested cross validation with leave one study out external folds. Model interpretability was achieved using variable importance analysis, SHapley Additive exPlanations, correlation matrices, and three dimensional parameter maps.
>   Non linear models consistently outperformed linear baselines, achieving coefficients of determination above 0.91 for several widely used polymers. Solution concentration emerged as the dominant global driver of fibre diameter distributions. Experimental validation across different electrospinning systems demonstrated close agreement between predicted and measured distributions. FibreCastML enables more reproducible and data driven optimisation of electrospun scaffold architectures.

