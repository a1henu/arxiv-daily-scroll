---
layout: default
title: Unsupervised Detection of Post-Stroke Brain Abnormalities
---

# Unsupervised Detection of Post-Stroke Brain Abnormalities
**arXiv**：[2510.24398v1](https://arxiv.org/abs/2510.24398) · [PDF](https://arxiv.org/pdf/2510.24398.pdf)  
**作者**：Youwan Mahé, Elise Bannier, Stéphanie Leplaideur, Elisa Fromont, Francesca Galassi  

**一句话要点**：提出基于流生成模型的非监督方法，检测中风后脑部异常

**关键词**：非监督异常检测, 流生成模型, 中风后脑成像, 结构异常, FROC分析

## 3 点简述
- 核心问题：监督分割方法难以捕捉中风后非病灶性结构异常，如萎缩和脑室扩大
- 方法要点：使用REFLECT流生成模型，在无病灶切片上训练，生成异常图进行检测
- 实验或效果：在ATLAS数据上，健康数据训练模型提升病灶分割和非病灶异常敏感性

## 摘要（原文）

> Post-stroke MRI not only delineates focal lesions but also reveals secondary
> structural changes, such as atrophy and ventricular enlargement. These
> abnormalities, increasingly recognised as imaging biomarkers of recovery and
> outcome, remain poorly captured by supervised segmentation methods. We evaluate
> REFLECT, a flow-based generative model, for unsupervised detection of both
> focal and non-lesional abnormalities in post-stroke patients. Using dual-expert
> central-slice annotations on ATLAS data, performance was assessed at the object
> level with Free-Response ROC analysis for anomaly maps. Two models were trained
> on lesion-free slices from stroke patients (ATLAS) and on healthy controls
> (IXI) to test the effect of training data. On ATLAS test subjects, the
> IXI-trained model achieved higher lesion segmentation (Dice = 0.37 vs 0.27) and
> improved sensitivity to non-lesional abnormalities (FROC = 0.62 vs 0.43).
> Training on fully healthy anatomy improves the modelling of normal variability,
> enabling broader and more reliable detection of structural abnormalities.

