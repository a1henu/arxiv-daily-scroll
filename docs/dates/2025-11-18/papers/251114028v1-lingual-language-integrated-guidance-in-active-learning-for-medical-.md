---
layout: default
title: LINGUAL: Language-INtegrated GUidance in Active Learning for Medical Image Segmentation
---

# LINGUAL: Language-INtegrated GUidance in Active Learning for Medical Image Segmentation
**arXiv**：[2511.14028v1](https://arxiv.org/abs/2511.14028) · [PDF](https://arxiv.org/pdf/2511.14028.pdf)  
**作者**：Md Shazid Islam, Shreyangshu Bera, Sudipta Paul, Amit K. Roy-Chowdhury  

**一句话要点**：提出LINGUAL框架，通过语言指导减少医学图像分割中的标注负担。

**关键词**：医学图像分割, 主动学习, 语言指导, 域适应, 标注效率

## 3 点简述
- 医学图像分割中，主动学习标注模糊边界时劳动密集且认知负担高。
- LINGUAL将自然语言指令转化为程序，自动执行子任务，无需人工干预。
- 在主动域适应中，性能可比或优于基线，估计标注时间减少约80%。

## 摘要（原文）

> Although active learning (AL) in segmentation tasks enables experts to annotate selected regions of interest (ROIs) instead of entire images, it remains highly challenging, labor-intensive, and cognitively demanding due to the blurry and ambiguous boundaries commonly observed in medical images. Also, in conventional AL, annotation effort is a function of the ROI- larger regions make the task cognitively easier but incur higher annotation costs, whereas smaller regions demand finer precision and more attention from the expert. In this context, language guidance provides an effective alternative, requiring minimal expert effort while bypassing the cognitively demanding task of precise boundary delineation in segmentation. Towards this goal, we introduce LINGUAL: a framework that receives natural language instructions from an expert, translates them into executable programs through in-context learning, and automatically performs the corresponding sequence of sub-tasks without any human intervention. We demonstrate the effectiveness of LINGUAL in active domain adaptation (ADA) achieving comparable or superior performance to AL baselines while reducing estimated annotation time by approximately 80%.

