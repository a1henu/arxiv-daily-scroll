---
layout: default
title: Breast Cancer Neoadjuvant Chemotherapy Treatment Response Prediction Using Aligned Longitudinal MRI and Clinical Data
---

# Breast Cancer Neoadjuvant Chemotherapy Treatment Response Prediction Using Aligned Longitudinal MRI and Clinical Data
**arXiv**：[2512.17759v1](https://arxiv.org/abs/2512.17759) · [PDF](https://arxiv.org/pdf/2512.17759.pdf)  
**作者**：Rahul Ravi, Ruizhe Li, Tarek Abdelfatah, Stephen Chan, Xin Chen  

**一句话要点**：提出基于对齐纵向MRI和临床数据的机器学习框架，预测乳腺癌新辅助化疗治疗反应。

**关键词**：乳腺癌治疗反应预测, 纵向MRI分析, 图像配准, 放射组学特征, 机器学习模型, 临床数据整合

## 3 点简述
- 核心问题：预测乳腺癌患者新辅助化疗后的病理完全缓解和5年无复发生存状态。
- 方法要点：通过图像配准提取纵向肿瘤特征，结合放射组学和深度学习特征提取器构建预测模型。
- 实验或效果：放射组学特征在逻辑回归模型中表现最佳，PCR分类AUC达0.88，RFS分类AUC达0.78。

## 摘要（原文）

> Aim: This study investigates treatment response prediction to neoadjuvant chemotherapy (NACT) in breast cancer patients, using longitudinal contrast-enhanced magnetic resonance images (CE-MRI) and clinical data. The goal is to develop machine learning (ML) models to predict pathologic complete response (PCR binary classification) and 5-year relapse-free survival status (RFS binary classification). Method: The proposed framework includes tumour segmentation, image registration, feature extraction, and predictive modelling. Using the image registration method, MRI image features can be extracted and compared from the original tumour site at different time points, therefore monitoring the intratumor changes during NACT process. Four feature extractors, including one radiomics and three deep learning-based (MedicalNet, Segformer3D, SAM-Med3D) were implemented and compared. In combination with three feature selection methods and four ML models, predictive models are built and compared. Results: The proposed image registration-based feature extraction consistently improves the predictive models. In the PCR and RFS classification tasks logistic regression model trained on radiomic features performed the best with an AUC of 0.88 and classification accuracy of 0.85 for PCR classification, and AUC of 0.78 and classification accuracy of 0.72 for RFS classification. Conclusions: It is evidenced that the image registration method has significantly improved performance in longitudinal feature learning in predicting PCR and RFS. The radiomics feature extractor is more effective than the pre-trained deep learning feature extractors, with higher performance and better interpretability.

