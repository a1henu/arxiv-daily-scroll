---
layout: default
title: A unified FLAIR hyperintensity segmentation model for various CNS tumor types and acquisition time points
---

# A unified FLAIR hyperintensity segmentation model for various CNS tumor types and acquisition time points
**arXiv**：[2512.17566v1](https://arxiv.org/abs/2512.17566) · [PDF](https://arxiv.org/pdf/2512.17566.pdf)  
**作者**：Mathilde Gajda Faanes, David Bouget, Asgeir S. Jakola, Timothy R. Smith, Vasileios K. Kavouridis, Francesco Latini, Margret Jensdottir, Peter Milos, Henrietta Nittby Redebrandt, Rickard L. Sjöberg, Rupavathana Mahesparan, Lars Kjelsberg Pedersen, Ole Solheim, Ingerid Reinertsen  

**一句话要点**：提出统一FLAIR高信号分割模型，适用于多种中枢神经系统肿瘤类型和采集时间点

**关键词**：FLAIR高信号分割, 中枢神经系统肿瘤, Attention U-Net, 多中心数据, 临床部署, 开源软件集成

## 3 点简述
- 核心问题：FLAIR MRI高信号体积是评估脑肿瘤体积或周围水肿的关键指标，需自动分割以辅助临床诊断与监测。
- 方法要点：使用约5000张不同肿瘤类型和采集时间点的FLAIR图像，基于Attention U-Net架构训练统一分割模型。
- 实验或效果：模型在多种肿瘤类型和采集时间点上表现良好，平均Dice分数达61.27%至90.92%，并集成到开源软件Raidionics中。

## 摘要（原文）

> T2-weighted fluid-attenuated inversion recovery (FLAIR) magnetic resonance imaging (MRI) scans are important for diagnosis, treatment planning and monitoring of brain tumors. Depending on the brain tumor type, the FLAIR hyperintensity volume is an important measure to asses the tumor volume or surrounding edema, and an automatic segmentation of this would be useful in the clinic. In this study, around 5000 FLAIR images of various tumors types and acquisition time points from different centers were used to train a unified FLAIR hyperintensity segmentation model using an Attention U-Net architecture. The performance was compared against dataset specific models, and was validated on different tumor types, acquisition time points and against BraTS. The unified model achieved an average Dice score of 88.65\% for pre-operative meningiomas, 80.08% for pre-operative metastasis, 90.92% for pre-operative and 84.60% for post-operative gliomas from BraTS, and 84.47% for pre-operative and 61.27\% for post-operative lower grade gliomas. In addition, the results showed that the unified model achieved comparable segmentation performance to the dataset specific models on their respective datasets, and enables generalization across tumor types and acquisition time points, which facilitates the deployment in a clinical setting. The model is integrated into Raidionics, an open-source software for CNS tumor analysis.

