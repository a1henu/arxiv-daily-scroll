---
layout: default
title: Masked Face Recognition under Different Backbones
---

# Masked Face Recognition under Different Backbones
**arXiv**：[2601.16440v1](https://arxiv.org/abs/2601.16440) · [PDF](https://arxiv.org/pdf/2601.16440.pdf)  
**作者**：Bo Zhang, Ming Zhang, Kun Wu, Lei Bian, Yi Lin  

**一句话要点**：评估不同骨干网络在戴口罩人脸识别中的性能，提供部署建议

**关键词**：戴口罩人脸识别, 骨干网络评估, 后疫情时代应用, 模型性能比较, 部署建议

## 3 点简述
- 核心问题：后疫情时代戴口罩人脸识别对传统模型构成挑战
- 方法要点：通过比较实验评估r100、r50、r34_mask_v1、r100_mask_v2、r50_mask_v3、Vit-Small/Tiny等骨干网络
- 实验或效果：r100_mask_v2在戴口罩测试中领先，Vit-Small/Tiny在戴口罩场景下表现强劲

## 摘要（原文）

> Erratum to the paper (Zhang et al., 2025): corrections to Table IV and the data in Page 3, Section A. In the post-pandemic era, a high proportion of civil aviation passengers wear masks during security checks, posing significant challenges to traditional face recognition models. The backbone network serves as the core component of face recognition models. In standard tests, r100 series models excelled (98%+ accuracy at 0.01% FAR in face comparison, high top1/top5 in search). r50 ranked second, r34_mask_v1 lagged. In masked tests, r100_mask_v2 led (90.07% accuracy), r50_mask_v3 performed best among r50 but trailed r100. Vit-Small/Tiny showed strong masked performance with gains in effectiveness. Through extensive comparative experiments, this paper conducts a comprehensive evaluation of several core backbone networks, aiming to reveal the impacts of different models on face recognition with and without masks, and provide specific deployment recommendations.

