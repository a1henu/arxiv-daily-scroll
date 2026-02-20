---
layout: default
title: A feature-stable and explainable machine learning framework for trustworthy decision-making under incomplete clinical data
---

# A feature-stable and explainable machine learning framework for trustworthy decision-making under incomplete clinical data
**arXiv**：[2602.17364v1](https://arxiv.org/abs/2602.17364) · [PDF](https://arxiv.org/pdf/2602.17364.pdf)  
**作者**：Justyna Andrys-Olek, Paulina Tworek, Luca Gherardini, Mark W. Ruddock, Mary Jo Kurt, Peter Fitzgerald, Jose Sousa  

**一句话要点**：提出CACTUS框架以解决临床数据缺失下机器学习模型特征不稳定和可解释性不足的问题

**关键词**：可解释机器学习, 特征稳定性, 临床数据缺失, 决策支持, 血尿队列分析

## 3 点简述
- 核心问题：机器学习模型在临床数据缺失时特征不稳定，影响可信度和决策支持
- 方法要点：集成特征抽象、可解释分类和特征稳定性分析，量化特征随数据质量下降的保持一致性
- 实验或效果：在血尿队列中验证，CACTUS在预测性能竞争或更优的同时，特征稳定性显著高于随机森林和梯度提升方法

## 摘要（原文）

> Machine learning models are increasingly applied to biomedical data, yet their adoption in high stakes domains remains limited by poor robustness, limited interpretability, and instability of learned features under realistic data perturbations, such as missingness. In particular, models that achieve high predictive performance may still fail to inspire trust if their key features fluctuate when data completeness changes, undermining reproducibility and downstream decision-making. Here, we present CACTUS (Comprehensive Abstraction and Classification Tool for Uncovering Structures), an explainable machine learning framework explicitly designed to address these challenges in small, heterogeneous, and incomplete clinical datasets. CACTUS integrates feature abstraction, interpretable classification, and systematic feature stability analysis to quantify how consistently informative features are preserved as data quality degrades. Using a real-world haematuria cohort comprising 568 patients evaluated for bladder cancer, we benchmark CACTUS against widely used machine learning approaches, including random forests and gradient boosting methods, under controlled levels of randomly introduced missing data. We demonstrate that CACTUS achieves competitive or superior predictive performance while maintaining markedly higher stability of top-ranked features as missingness increases, including in sex-stratified analyses. Our results show that feature stability provides information complementary to conventional performance metrics and is essential for assessing the trustworthiness of machine learning models applied to biomedical data. By explicitly quantifying robustness to missing data and prioritising interpretable, stable features, CACTUS offers a generalizable framework for trustworthy data-driven decision support.

