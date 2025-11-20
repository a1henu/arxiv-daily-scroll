---
layout: default
title: BrainRotViT: Transformer-ResNet Hybrid for Explainable Modeling of Brain Aging from 3D sMRI
---

# BrainRotViT: Transformer-ResNet Hybrid for Explainable Modeling of Brain Aging from 3D sMRI
**arXiv**：[2511.15188v1](https://arxiv.org/abs/2511.15188) · [PDF](https://arxiv.org/pdf/2511.15188.pdf)  
**作者**：Wasif Jalal, Md Nafiu Rahman, M. Sohel Rahman  

**一句话要点**：提出BrainRotViT混合架构，用于从3D sMRI中可解释地建模脑老化

**关键词**：脑年龄估计, Transformer-ResNet混合, 结构MRI分析, 可解释AI, 神经退行性疾病

## 3 点简述
- 传统脑年龄估计方法存在手动特征工程和过拟合问题，纯Transformer模型需大数据和高计算成本
- 结合ViT的全局上下文建模与ResNet的局部细化，通过预训练编码器和残差CNN回归器估计脑年龄
- 在多个数据集上验证，MAE达3.34年，泛化性强，注意力图可解释脑老化相关区域

## 摘要（原文）

> Accurate brain age estimation from structural MRI is a valuable biomarker for studying aging and neurodegeneration. Traditional regression and CNN-based methods face limitations such as manual feature engineering, limited receptive fields, and overfitting on heterogeneous data. Pure transformer models, while effective, require large datasets and high computational cost. We propose Brain ResNet over trained Vision Transformer (BrainRotViT), a hybrid architecture that combines the global context modeling of vision transformers (ViT) with the local refinement of residual CNNs. A ViT encoder is first trained on an auxiliary age and sex classification task to learn slice-level features. The frozen encoder is then applied to all sagittal slices to generate a 2D matrix of embedding vectors, which is fed into a residual CNN regressor that incorporates subject sex at the final fully-connected layer to estimate continuous brain age. Our method achieves an MAE of 3.34 years (Pearson $r=0.98$, Spearman $ρ=0.97$, $R^2=0.95$) on validation across 11 MRI datasets encompassing more than 130 acquisition sites, outperforming baseline and state-of-the-art models. It also generalizes well across 4 independent cohorts with MAEs between 3.77 and 5.04 years. Analyses on the brain age gap (the difference between the predicted age and actual age) show that aging patterns are associated with Alzheimer's disease, cognitive impairment, and autism spectrum disorder. Model attention maps highlight aging-associated regions of the brain, notably the cerebellar vermis, precentral and postcentral gyri, temporal lobes, and medial superior frontal gyrus. Our results demonstrate that this method provides an efficient, interpretable, and generalizable framework for brain-age prediction, bridging the gap between CNN- and transformer-based approaches while opening new avenues for aging and neurodegeneration research.

