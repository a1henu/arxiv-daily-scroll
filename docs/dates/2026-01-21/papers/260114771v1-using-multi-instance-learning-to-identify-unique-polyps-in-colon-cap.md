---
layout: default
title: Using Multi-Instance Learning to Identify Unique Polyps in Colon Capsule Endoscopy Images
---

# Using Multi-Instance Learning to Identify Unique Polyps in Colon Capsule Endoscopy Images
**arXiv**：[2601.14771v1](https://arxiv.org/abs/2601.14771) · [PDF](https://arxiv.org/pdf/2601.14771.pdf)  
**作者**：Puneet Sharma, Kristian Dalsbø Hindberg, Eibe Frank, Benedicte Schelde-Olesen, Ulrik Deding  

**一句话要点**：提出基于多示例学习与注意力机制的框架，用于结肠胶囊内镜图像中独特息肉的识别。

**关键词**：多示例学习, 注意力机制, 自监督学习, 结肠胶囊内镜, 医学图像分析, 息肉识别

## 3 点简述
- 核心问题：结肠胶囊内镜图像量大，人工识别独特息肉困难且标注模糊。
- 方法要点：采用多示例验证框架，结合VEMA和DBA注意力机制，并探索SimCLR自监督学习。
- 实验或效果：在1912个息肉数据集上，DBA L1结合ConvNeXt和SimCLR预训练达到86.26%准确率和0.928 AUC。

## 摘要（原文）

> Identifying unique polyps in colon capsule endoscopy (CCE) images is a critical yet challenging task for medical personnel due to the large volume of images, the cognitive load it creates for clinicians, and the ambiguity in labeling specific frames. This paper formulates this problem as a multi-instance learning (MIL) task, where a query polyp image is compared with a target bag of images to determine uniqueness. We employ a multi-instance verification (MIV) framework that incorporates attention mechanisms, such as variance-excited multi-head attention (VEMA) and distance-based attention (DBA), to enhance the model's ability to extract meaningful representations. Additionally, we investigate the impact of self-supervised learning using SimCLR to generate robust embeddings. Experimental results on a dataset of 1912 polyps from 754 patients demonstrate that attention mechanisms significantly improve performance, with DBA L1 achieving the highest test accuracy of 86.26\% and a test AUC of 0.928 using a ConvNeXt backbone with SimCLR pretraining. This study underscores the potential of MIL and self-supervised learning in advancing automated analysis of Colon Capsule Endoscopy images, with implications for broader medical imaging applications.

