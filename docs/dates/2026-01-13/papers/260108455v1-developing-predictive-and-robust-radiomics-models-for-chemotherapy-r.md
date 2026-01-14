---
layout: default
title: Developing Predictive and Robust Radiomics Models for Chemotherapy Response in High-Grade Serous Ovarian Carcinoma
---

# Developing Predictive and Robust Radiomics Models for Chemotherapy Response in High-Grade Serous Ovarian Carcinoma
**arXiv**：[2601.08455v1](https://arxiv.org/abs/2601.08455) · [PDF](https://arxiv.org/pdf/2601.08455.pdf)  
**作者**：Sepideh Hatamikia, Geevarghese George, Florian Schwarzhans, Amirreza Mahbod, Marika AV Reinius, Ali Abbasian Ardakani, Mercedes Jimenez-Linan, Satish Viswanath, Mireia Crispin-Ortuzar, Lorena Escudero Sanchez, Evis Sala, James D Brenton, Ramona Woitek  

**一句话要点**：提出结合稳健特征选择的放射组学框架，以预测高级别浆液性卵巢癌的化疗反应。

**关键词**：放射组学, 化疗反应预测, 特征选择, 机器学习, 卵巢癌, CT影像分析

## 3 点简述
- 核心问题：高级别浆液性卵巢癌患者中约40%对新辅助化疗反应有限，需非侵入性预测方法。
- 方法要点：集成自动化随机化算法模拟观察者间变异，平衡特征稳健性与预测准确性。
- 实验或效果：最佳模型在体积减少预测中AUC达0.83，不同解剖部位病变对特定指标预测效果各异。

## 摘要（原文）

> Objectives: High-grade serous ovarian carcinoma (HGSOC) is typically diagnosed at an advanced stage with extensive peritoneal metastases, making treatment challenging. Neoadjuvant chemotherapy (NACT) is often used to reduce tumor burden before surgery, but about 40% of patients show limited response. Radiomics, combined with machine learning (ML), offers a promising non-invasive method for predicting NACT response by analyzing computed tomography (CT) imaging data. This study aimed to improve response prediction in HGSOC patients undergoing NACT by integration different feature selection methods. Materials and methods: A framework for selecting robust radiomics features was introduced by employing an automated randomisation algorithm to mimic inter-observer variability, ensuring a balance between feature robustness and prediction accuracy. Four response metrics were used: chemotherapy response score (CRS), RECIST, volume reduction (VolR), and diameter reduction (DiaR). Lesions in different anatomical sites were studied. Pre- and post-NACT CT scans were used for feature extraction and model training on one cohort, and an independent cohort was used for external testing. Results: The best prediction performance was achieved using all lesions combined for VolR prediction, with an AUC of 0.83. Omental lesions provided the best results for CRS prediction (AUC 0.77), while pelvic lesions performed best for DiaR (AUC 0.76). Conclusion: The integration of robustness into the feature selection processes ensures the development of reliable models and thus facilitates the implementation of the radiomics models in clinical applications for HGSOC patients. Future work should explore further applications of radiomics in ovarian cancer, particularly in real-time clinical settings.

