---
layout: default
title: Forgetting-Resistant and Lesion-Aware Source-Free Domain Adaptive Fundus Image Analysis with Vision-Language Model
---

# Forgetting-Resistant and Lesion-Aware Source-Free Domain Adaptive Fundus Image Analysis with Vision-Language Model
**arXiv**：[2602.19471v1](https://arxiv.org/abs/2602.19471) · [PDF](https://arxiv.org/pdf/2602.19471.pdf)  
**作者**：Zheang Huai, Hui Tang, Hualiang Wang, Xiaomeng Li  

**一句话要点**：提出遗忘抵抗与病灶感知方法，用于基于视觉语言模型的免源域自适应眼底图像分析

**关键词**：免源域自适应, 视觉语言模型, 眼底图像分析, 遗忘抵抗, 病灶感知, 细粒度知识

## 3 点简述
- 核心问题：现有视觉语言模型辅助的免源域自适应方法存在预测遗忘和忽略细粒度知识的问题
- 方法要点：通过遗忘抵抗模块保留目标模型置信预测，病灶感知模块利用视觉语言模型的细粒度知识
- 实验或效果：在实验中显著优于视觉语言模型，并超越现有最先进方法

## 摘要（原文）

> Source-free domain adaptation (SFDA) aims to adapt a model trained in the source domain to perform well in the target domain, with only unlabeled target domain data and the source model. Taking into account that conventional SFDA methods are inevitably error-prone under domain shift, recently greater attention has been directed to SFDA assisted with off-the-shelf foundation models, e.g., vision-language (ViL) models. However, existing works of leveraging ViL models for SFDA confront two issues: (i) Although mutual information is exploited to consider the joint distribution between the predictions of ViL model and the target model, we argue that the forgetting of some superior predictions of the target model still occurs, as indicated by the decline of the accuracies of certain classes during adaptation; (ii) Prior research disregards the rich, fine-grained knowledge embedded in the ViL model, which offers detailed grounding for fundus image diagnosis. In this paper, we introduce a novel forgetting-resistant and lesion-aware (FRLA) method for SFDA of fundus image diagnosis with ViL model. Specifically, a forgetting-resistant adaptation module explicitly preserves the confident predictions of the target model, and a lesion-aware adaptation module yields patch-wise predictions from ViL model and employs them to help the target model be aware of the lesion areas and leverage the ViL model's fine-grained knowledge. Extensive experiments show that our method not only significantly outperforms the vision-language model, but also achieves consistent improvements over the state-of-the-art methods. Our code will be released.

