---
layout: default
title: Towards Explainable Skin Cancer Classification: A Dual-Network Attention Model with Lesion Segmentation and Clinical Metadata Fusion
---

# Towards Explainable Skin Cancer Classification: A Dual-Network Attention Model with Lesion Segmentation and Clinical Metadata Fusion
**arXiv**：[2510.17773v1](https://arxiv.org/abs/2510.17773) · [PDF](https://arxiv.org/pdf/2510.17773.pdf)  
**作者**：Md. Enamul Atiq, Shaikh Anowarul Fattah  

**一句话要点**：提出双网络注意力模型，融合病灶分割与临床元数据以提升皮肤癌分类准确性与可解释性。

**关键词**：皮肤癌分类, 病灶分割, 注意力机制, 临床元数据融合, 可解释性AI, 深度学习

## 3 点简述
- 皮肤癌诊断面临类内高变异性与类间细微差异，且深度学习模型常为黑箱，影响临床信任。
- 方法采用Deep-UNet分割病灶，双DenseNet201编码器融合特征，并集成临床元数据以增强分类。
- 在HAM10000等数据集上验证，模型在分割与分类性能上优于基线，并通过Grad-CAM热图提升可解释性。

## 摘要（原文）

> Skin cancer is a life-threatening disease where early detection significantly
> improves patient outcomes. Automated diagnosis from dermoscopic images is
> challenging due to high intra-class variability and subtle inter-class
> differences. Many deep learning models operate as "black boxes," limiting
> clinical trust. In this work, we propose a dual-encoder attention-based
> framework that leverages both segmented lesions and clinical metadata to
> enhance skin lesion classification in terms of both accuracy and
> interpretability. A novel Deep-UNet architecture with Dual Attention Gates
> (DAG) and Atrous Spatial Pyramid Pooling (ASPP) is first employed to segment
> lesions. The classification stage uses two DenseNet201 encoders-one on the
> original image and another on the segmented lesion whose features are fused via
> multi-head cross-attention. This dual-input design guides the model to focus on
> salient pathological regions. In addition, a transformer-based module
> incorporates patient metadata (age, sex, lesion site) into the prediction. We
> evaluate our approach on the HAM10000 dataset and the ISIC 2018 and 2019
> challenges. The proposed method achieves state-of-the-art segmentation
> performance and significantly improves classification accuracy and average AUC
> compared to baseline models. To validate our model's reliability, we use
> Gradient-weighted Class Activation Mapping (Grad-CAM) to generate heatmaps.
> These visualizations confirm that our model's predictions are based on the
> lesion area, unlike models that rely on spurious background features. These
> results demonstrate that integrating precise lesion segmentation and clinical
> data with attention-based fusion leads to a more accurate and interpretable
> skin cancer classification model.

