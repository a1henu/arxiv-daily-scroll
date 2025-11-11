---
layout: default
title: Sim4Seg: Boosting Multimodal Multi-disease Medical Diagnosis Segmentation with Region-Aware Vision-Language Similarity Masks
---

# Sim4Seg: Boosting Multimodal Multi-disease Medical Diagnosis Segmentation with Region-Aware Vision-Language Similarity Masks
**arXiv**：[2511.06665v1](https://arxiv.org/abs/2511.06665) · [PDF](https://arxiv.org/pdf/2511.06665.pdf)  
**作者**：Lingran Song, Yucheng Zhou, Jianbing Shen  

**一句话要点**：提出Sim4Seg框架以提升多模态多疾病医学诊断分割性能

**关键词**：医学图像分割, 视觉语言模型, 多模态诊断, 区域感知相似性, 测试时间缩放

## 3 点简述
- 核心问题：现有医学图像分割模型未联合处理分割与诊断任务，缺乏可解释性。
- 方法要点：引入区域感知视觉语言相似性掩码模块，优化分割与诊断联合学习。
- 实验或效果：在M3DS数据集上，方法在分割和诊断方面均优于基线模型。

## 摘要（原文）

> Despite significant progress in pixel-level medical image analysis, existing
> medical image segmentation models rarely explore medical segmentation and
> diagnosis tasks jointly. However, it is crucial for patients that models can
> provide explainable diagnoses along with medical segmentation results. In this
> paper, we introduce a medical vision-language task named Medical Diagnosis
> Segmentation (MDS), which aims to understand clinical queries for medical
> images and generate the corresponding segmentation masks as well as diagnostic
> results. To facilitate this task, we first present the Multimodal Multi-disease
> Medical Diagnosis Segmentation (M3DS) dataset, containing diverse multimodal
> multi-disease medical images paired with their corresponding segmentation masks
> and diagnosis chain-of-thought, created via an automated diagnosis
> chain-of-thought generation pipeline. Moreover, we propose Sim4Seg, a novel
> framework that improves the performance of diagnosis segmentation by taking
> advantage of the Region-Aware Vision-Language Similarity to Mask (RVLS2M)
> module. To improve overall performance, we investigate a test-time scaling
> strategy for MDS tasks. Experimental results demonstrate that our method
> outperforms the baselines in both segmentation and diagnosis.

