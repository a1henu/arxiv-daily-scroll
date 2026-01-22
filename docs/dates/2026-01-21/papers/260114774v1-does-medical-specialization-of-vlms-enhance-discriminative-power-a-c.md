---
layout: default
title: Does medical specialization of VLMs enhance discriminative power?: A comprehensive investigation through feature distribution analysis
---

# Does medical specialization of VLMs enhance discriminative power?: A comprehensive investigation through feature distribution analysis
**arXiv**：[2601.14774v1](https://arxiv.org/abs/2601.14774) · [PDF](https://arxiv.org/pdf/2601.14774.pdf)  
**作者**：Keita Takeda, Tomoya Sakai  

**一句话要点**：通过特征分布分析探究医学视觉语言模型的医学专业化是否增强判别力

**关键词**：医学视觉语言模型, 特征分布分析, 病灶分类, 文本编码器增强, 背景偏差

## 3 点简述
- 核心问题：医学视觉语言模型是否学习到真正判别性的病灶特征，其表示尚不明确
- 方法要点：分析医学与非医学VLMs的特征分布，评估医学专业化对特征提取的影响
- 实验或效果：医学VLMs能提取有效特征，但非医学模型在文本编码器增强后表现更优

## 摘要（原文）

> This study investigates the feature representations produced by publicly available open source medical vision-language models (VLMs). While medical VLMs are expected to capture diagnostically relevant features, their learned representations remain underexplored, and standard evaluations like classification accuracy do not fully reveal if they acquire truly discriminative, lesion-specific features. Understanding these representations is crucial for revealing medical image structures and improving downstream tasks in medical image analysis. This study aims to investigate the feature distributions learned by medical VLMs and evaluate the impact of medical specialization. We analyze the feature distribution of multiple image modalities extracted by some representative medical VLMs across lesion classification datasets on multiple modalities. These distributions were compared them with non-medical VLMs to assess the domain-specific medical training. Our experiments showed that medical VLMs can extract discriminative features that are effective for medical classification tasks. Moreover, it was found that non-medical VLMs with recent improvement with contextual enrichment such as LLM2CLIP produce more refined feature representations. Our results imply that enhancing text encoder is more crucial than training intensively on medical images when developing medical VLMs. Notably, non-medical models are particularly vulnerable to biases introduced by overlaied text strings on images. These findings underscore the need for careful consideration on model selection according to downstream tasks besides potential risks in inference due to background biases such as textual information in images.

