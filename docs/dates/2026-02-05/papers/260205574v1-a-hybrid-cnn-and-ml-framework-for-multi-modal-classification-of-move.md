---
layout: default
title: A Hybrid CNN and ML Framework for Multi-modal Classification of Movement Disorders Using MRI and Brain Structural Features
---

# A Hybrid CNN and ML Framework for Multi-modal Classification of Movement Disorders Using MRI and Brain Structural Features
**arXiv**：[2602.05574v1](https://arxiv.org/abs/2602.05574) · [PDF](https://arxiv.org/pdf/2602.05574.pdf)  
**作者**：Mengyu Li, Ingibjörg Kristjánsdóttir, Thilo van Eimeren, Kathrin Giehl, Lotta M. Ellingsen, the ASAP Neuroimaging Initiative  

**一句话要点**：提出结合CNN与机器学习的混合框架，利用多模态MRI数据分类非典型帕金森病亚型与帕金森病。

**关键词**：非典型帕金森病分类, 多模态MRI分析, 卷积神经网络, 机器学习, 脑结构分割, 早期诊断

## 3 点简述
- 核心问题：非典型帕金森病早期与帕金森病临床特征重叠，导致误诊，需可靠影像生物标志物进行早期鉴别诊断。
- 方法要点：融合T1加权MRI、12个深部脑结构分割掩模及其体积测量，结合CNN提取图像特征与机器学习处理定量特征。
- 实验或效果：在PSP vs. PD、MSA vs. PD和PSP vs. MSA分类中，AUC分别达0.95、0.86和0.92，显示多模态信息整合提升分类性能。

## 摘要（原文）

> Atypical Parkinsonian Disorders (APD), also known as Parkinson-plus syndrome, are a group of neurodegenerative diseases that include progressive supranuclear palsy (PSP) and multiple system atrophy (MSA). In the early stages, overlapping clinical features often lead to misdiagnosis as Parkinson's disease (PD). Identifying reliable imaging biomarkers for early differential diagnosis remains a critical challenge. In this study, we propose a hybrid framework combining convolutional neural networks (CNNs) with machine learning (ML) techniques to classify APD subtypes versus PD and distinguish between the subtypes themselves: PSP vs. PD, MSA vs. PD, and PSP vs. MSA. The model leverages multi-modal input data, including T1-weighted magnetic resonance imaging (MRI), segmentation masks of 12 deep brain structures associated with APD, and their corresponding volumetric measurements. By integrating these complementary modalities, including image data, structural segmentation masks, and quantitative volume features, the hybrid approach achieved promising classification performance with area under the curve (AUC) scores of 0.95 for PSP vs. PD, 0.86 for MSA vs. PD, and 0.92 for PSP vs. MSA. These results highlight the potential of combining spatial and structural information for robust subtype differentiation. In conclusion, this study demonstrates that fusing CNN-based image features with volume-based ML inputs improves classification accuracy for APD subtypes. The proposed approach may contribute to more reliable early-stage diagnosis, facilitating timely and targeted interventions in clinical practice.

