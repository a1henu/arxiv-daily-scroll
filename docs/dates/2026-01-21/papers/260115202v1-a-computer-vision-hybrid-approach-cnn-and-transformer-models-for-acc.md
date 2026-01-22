---
layout: default
title: A Computer Vision Hybrid Approach: CNN and Transformer Models for Accurate Alzheimer's Detection from Brain MRI Scans
---

# A Computer Vision Hybrid Approach: CNN and Transformer Models for Accurate Alzheimer's Detection from Brain MRI Scans
**arXiv**：[2601.15202v1](https://arxiv.org/abs/2601.15202) · [PDF](https://arxiv.org/pdf/2601.15202.pdf)  
**作者**：Md Mahmudul Hoque, Shuvo Karmaker, Md. Hadi Al-Amin, Md Modabberul Islam, Jisun Junayed, Farha Ulfat Mahi  

**一句话要点**：提出Evan_V2混合模型，通过特征融合提升脑MRI阿尔茨海默病分类准确率。

**关键词**：阿尔茨海默病分类, 脑MRI分析, CNN模型, Transformer模型, 混合模型, 特征融合

## 3 点简述
- 核心问题：早期准确分类阿尔茨海默病，涉及轻度、中度、非痴呆和极轻度痴呆四类。
- 方法要点：比较CNN和Transformer模型，提出Evan_V2混合模型，融合十种架构特征。
- 实验或效果：Evan_V2达到99.99%准确率，优于所有独立模型，减少误分类。

## 摘要（原文）

> Early and accurate classification of Alzheimers disease (AD) from brain MRI scans is essential for timely clinical intervention and improved patient outcomes. This study presents a comprehensive comparative analysis of five CNN architectures (EfficientNetB0, ResNet50, DenseNet201, MobileNetV3, VGG16), five Transformer-based models (ViT, ConvTransformer, PatchTransformer, MLP-Mixer, SimpleTransformer), and a proposed hybrid model named Evan_V2. All models were evaluated on a four-class AD classification task comprising Mild Dementia, Moderate Dementia, Non-Demented, and Very Mild Dementia categories. Experimental findings show that CNN architectures consistently achieved strong performance, with ResNet50 attaining 98.83% accuracy. Transformer models demonstrated competitive generalization capabilities, with ViT achieving the highest accuracy among them at 95.38%. However, individual Transformer variants exhibited greater class-specific instability. The proposed Evan_V2 hybrid model, which integrates outputs from ten CNN and Transformer architectures through feature-level fusion, achieved the best overall performance with 99.99% accuracy, 0.9989 F1-score, and 0.9968 ROC AUC. Confusion matrix analysis further confirmed that Evan_V2 substantially reduced misclassification across all dementia stages, outperforming every standalone model. These findings highlight the potential of hybrid ensemble strategies in producing highly reliable and clinically meaningful diagnostic tools for Alzheimers disease classification.

