---
layout: default
title: Performance of a Deep Learning-Based Segmentation Model for Pancreatic Tumors on Public Endoscopic Ultrasound Datasets
---

# Performance of a Deep Learning-Based Segmentation Model for Pancreatic Tumors on Public Endoscopic Ultrasound Datasets
**arXiv**：[2601.05937v1](https://arxiv.org/abs/2601.05937) · [PDF](https://arxiv.org/pdf/2601.05937.pdf)  
**作者**：Pankaj Gupta, Priya Mudgil, Niharika Dutta, Kartik Bose, Nitish Kumar, Anupam Kumar, Jimil Shah, Vaneet Jearth, Jayanta Samanta, Vishal Sharma, Harshal Mandavdhare, Surinder Rana, Saroj K Sinha, Usha Dutta  

**一句话要点**：提出基于Vision Transformer的深度学习分割模型，用于内镜超声图像中的胰腺肿瘤分割。

**关键词**：胰腺肿瘤分割, 内镜超声, Vision Transformer, 深度学习, 医学图像分析

## 3 点简述
- 核心问题：胰腺癌诊断依赖内镜超声，但存在操作者主观性，影响准确性。
- 方法要点：采用Vision Transformer骨干网络，在USFM框架下训练分割模型，处理17,367张图像。
- 实验或效果：模型在外部验证集上DSC达0.657，敏感性71.8%，但9.7%病例出现错误多重预测。

## 摘要（原文）

> Background: Pancreatic cancer is one of the most aggressive cancers, with poor survival rates. Endoscopic ultrasound (EUS) is a key diagnostic modality, but its effectiveness is constrained by operator subjectivity. This study evaluates a Vision Transformer-based deep learning segmentation model for pancreatic tumors. Methods: A segmentation model using the USFM framework with a Vision Transformer backbone was trained and validated with 17,367 EUS images (from two public datasets) in 5-fold cross-validation. The model was tested on an independent dataset of 350 EUS images from another public dataset, manually segmented by radiologists. Preprocessing included grayscale conversion, cropping, and resizing to 512x512 pixels. Metrics included Dice similarity coefficient (DSC), intersection over union (IoU), sensitivity, specificity, and accuracy. Results: In 5-fold cross-validation, the model achieved a mean DSC of 0.651 +/- 0.738, IoU of 0.579 +/- 0.658, sensitivity of 69.8%, specificity of 98.8%, and accuracy of 97.5%. For the external validation set, the model achieved a DSC of 0.657 (95% CI: 0.634-0.769), IoU of 0.614 (95% CI: 0.590-0.689), sensitivity of 71.8%, and specificity of 97.7%. Results were consistent, but 9.7% of cases exhibited erroneous multiple predictions. Conclusions: The Vision Transformer-based model demonstrated strong performance for pancreatic tumor segmentation in EUS images. However, dataset heterogeneity and limited external validation highlight the need for further refinement, standardization, and prospective studies.

