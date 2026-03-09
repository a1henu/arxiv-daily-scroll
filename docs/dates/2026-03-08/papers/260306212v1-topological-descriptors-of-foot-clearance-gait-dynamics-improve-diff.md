---
layout: default
title: Topological descriptors of foot clearance gait dynamics improve differential diagnosis of Parkinsonism
---

# Topological descriptors of foot clearance gait dynamics improve differential diagnosis of Parkinsonism
**arXiv**：[2603.06212v1](https://arxiv.org/abs/2603.06212) · [PDF](https://arxiv.org/pdf/2603.06212.pdf)  
**作者**：Jhonathan Barrios, Wolfram Erlhagen, Miguel F. Gago, Estela Bicho, Flora Ferreira  

**一句话要点**：提出基于拓扑数据分析的步态特征，以改进帕金森综合征的鉴别诊断。

**关键词**：拓扑数据分析, 步态分析, 帕金森综合征, 机器学习分类, 持久同调, 足部间隙

## 3 点简述
- 核心问题：帕金森综合征鉴别诊断困难，传统步态分析忽略非线性结构特征。
- 方法要点：使用拓扑数据分析提取足部间隙时间序列的持久同调特征，结合随机森林分类。
- 实验或效果：在15名对照、15名特发性帕金森病和14名血管性帕金森病患者中，Betti曲线特征在药物状态下达到83%准确率。

## 摘要（原文）

> Differential diagnosis among parkinsonian syndromes remains a clinical challenge due to overlapping motor symptoms and subtle gait abnormalities. Accurate differentiation is crucial for treatment planning and prognosis. While gait analysis is a well established approach for assessing motor impairments, conventional methods often overlook hidden nonlinear and structural features embedded in foot clearance patterns. We evaluated Topological Data Analysis (TDA) as a complementary tool for Parkinsonism classification using foot clearance time series. Persistent homology produced Betti curves, persistence landscapes, and silhouettes, which were used as features for a Random Forest classifier. The dataset comprised 15 controls (CO), 15 idiopathic Parkinson's disease (IPD), and 14 vascular Parkinsonism (VaP). Models were assessed with leave-one-out cross-validation (LOOCV). Betti-curve descriptors consistently yielded the strongest results. For IPD vs VaP, foot clearance variables minimum toe clearance, maximum toe late swing, and maximum heel clearance achieved 83% accuracy and AUC=0.89 under LOOCV in the medicated (On) state. Performance improved in the On state and further when both Off and On states were considered, indicating sensitivity of the topological features to levodopa related gait changes. These findings support integrating TDA with machine learning to improve clinical gait analysis and aid differential diagnosis across parkinsonian disorders.

