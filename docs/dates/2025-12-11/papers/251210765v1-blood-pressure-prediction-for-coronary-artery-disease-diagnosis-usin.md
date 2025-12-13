---
layout: default
title: Blood Pressure Prediction for Coronary Artery Disease Diagnosis using Coronary Computed Tomography Angiography
---

# Blood Pressure Prediction for Coronary Artery Disease Diagnosis using Coronary Computed Tomography Angiography
**arXiv**：[2512.10765v1](https://arxiv.org/abs/2512.10765) · [PDF](https://arxiv.org/pdf/2512.10765.pdf)  
**作者**：Rene Lisasi, Michele Esposito, Chen Zhao  

**一句话要点**：提出基于扩散回归的冠状动脉血压预测框架，以支持非侵入性CAD诊断。

**关键词**：冠状动脉疾病诊断, 血压预测, 扩散回归模型, 计算流体动力学, 冠状动脉CT血管造影

## 3 点简述
- 核心问题：传统CFD模拟计算成本高，限制AI模型训练和临床大规模应用。
- 方法要点：开发自动化管道提取CCTA几何特征，并设计扩散回归模型直接预测血压。
- 实验或效果：在模拟数据集上，模型R2达64.42%，优于基线方法，实现高效预测。

## 摘要（原文）

> Computational fluid dynamics (CFD) based simulation of coronary blood flow provides valuable hemodynamic markers, such as pressure gradients, for diagnosing coronary artery disease (CAD). However, CFD is computationally expensive, time-consuming, and difficult to integrate into large-scale clinical workflows. These limitations restrict the availability of labeled hemodynamic data for training AI models and hinder broad adoption of non-invasive, physiology based CAD assessment. To address these challenges, we develop an end to end pipeline that automates coronary geometry extraction from coronary computed tomography angiography (CCTA), streamlines simulation data generation, and enables efficient learning of coronary blood pressure distributions. The pipeline reduces the manual burden associated with traditional CFD workflows while producing consistent training data. We further introduce a diffusion-based regression model designed to predict coronary blood pressure directly from CCTA derived features, bypassing the need for slow CFD computation during inference. Evaluated on a dataset of simulated coronary hemodynamics, the proposed model achieves state of the art performance, with an R2 of 64.42%, a root mean squared error of 0.0974, and a normalized RMSE of 0.154, outperforming several baseline approaches. This work provides a scalable and accessible framework for rapid, non-invasive blood pressure prediction to support CAD diagnosis.

