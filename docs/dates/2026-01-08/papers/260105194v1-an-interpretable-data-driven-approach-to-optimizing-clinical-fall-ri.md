---
layout: default
title: An interpretable data-driven approach to optimizing clinical fall risk assessment
---

# An interpretable data-driven approach to optimizing clinical fall risk assessment
**arXiv**：[2601.05194v1](https://arxiv.org/abs/2601.05194) · [PDF](https://arxiv.org/pdf/2601.05194.pdf)  
**作者**：Fardin Ganjkhanloo, Emmett Springer, Erik H. Hoyer, Daniel L. Young, Holley Farley, Kimia Ghobadi  

**一句话要点**：提出约束评分优化方法以提升住院患者跌倒风险评估工具的预测性能与可解释性

**关键词**：跌倒风险评估, 约束评分优化, 临床可解释性, 数据驱动建模, 住院患者安全, 预测性能提升

## 3 点简述
- 核心问题：约翰霍普金斯跌倒风险评估工具（JHFRAT）的预测性能有待改进，需与临床风险标签更好对齐。
- 方法要点：采用约束评分优化模型重新加权JHFRAT评分权重，保持其可加结构和临床阈值，确保可解释性。
- 实验或效果：模型AUC-ROC从0.86提升至0.91，每周可额外保护35名高风险患者，性能稳健且优于基准黑盒模型。

## 摘要（原文）

> In this study, we aim to better align fall risk prediction from the Johns Hopkins Fall Risk Assessment Tool (JHFRAT) with additional clinically meaningful measures via a data-driven modelling approach. We conducted a retrospective cohort analysis of 54,209 inpatient admissions from three Johns Hopkins Health System hospitals between March 2022 and October 2023. A total of 20,208 admissions were included as high fall risk encounters, and 13,941 were included as low fall risk encounters. To incorporate clinical knowledge and maintain interpretability, we employed constrained score optimization (CSO) models to reweight the JHFRAT scoring weights, while preserving its additive structure and clinical thresholds. Recalibration refers to adjusting item weights so that the resulting score can order encounters more consistently by the study's risk labels, and without changing the tool's form factor or deployment workflow. The model demonstrated significant improvements in predictive performance over the current JHFRAT (CSO AUC-ROC=0.91, JHFRAT AUC-ROC=0.86). This performance improvement translates to protecting an additional 35 high-risk patients per week across the Johns Hopkins Health System. The constrained score optimization models performed similarly with and without the EHR variables. Although the benchmark black-box model (XGBoost), improves upon the performance metrics of the knowledge-based constrained logistic regression (AUC-ROC=0.94), the CSO demonstrates more robustness to variations in risk labeling. This evidence-based approach provides a robust foundation for health systems to systematically enhance inpatient fall prevention protocols and patient safety using data-driven optimization techniques, contributing to improved risk assessment and resource allocation in healthcare settings.

