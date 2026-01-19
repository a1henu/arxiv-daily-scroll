---
layout: default
title: Visual question answering-based image-finding generation for pulmonary nodules on chest CT from structured annotations
---

# Visual question answering-based image-finding generation for pulmonary nodules on chest CT from structured annotations
**arXiv**：[2601.11075v1](https://arxiv.org/abs/2601.11075) · [PDF](https://arxiv.org/pdf/2601.11075.pdf)  
**作者**：Maiko Nagao, Kaito Urata, Atsushi Teramoto, Kazuyoshi Imaizumi, Masashi Kondo, Hiroshi Fujita  

**一句话要点**：提出基于视觉问答的胸部CT肺结节图像发现生成方法，用于交互式诊断支持

**关键词**：视觉问答, 胸部CT, 肺结节, 图像发现生成, 交互式诊断支持

## 3 点简述
- 核心问题：如何根据医生兴趣生成肺结节形态特征的图像发现，而非固定描述。
- 方法要点：利用LIDC-IDRI数据集构建VQA数据集，微调模型生成图像发现。
- 实验或效果：生成结果在CIDEr得分达3.896，与参考发现高度一致。

## 摘要（原文）

> Interpretation of imaging findings based on morphological characteristics is important for diagnosing pulmonary nodules on chest computed tomography (CT) images. In this study, we constructed a visual question answering (VQA) dataset from structured data in an open dataset and investigated an image-finding generation method for chest CT images, with the aim of enabling interactive diagnostic support that presents findings based on questions that reflect physicians' interests rather than fixed descriptions. In this study, chest CT images included in the Lung Image Database Consortium and Image Database Resource Initiative (LIDC-IDRI) datasets were used. Regions of interest surrounding the pulmonary nodules were extracted from these images, and image findings and questions were defined based on morphological characteristics recorded in the database. A dataset comprising pairs of cropped images, corresponding questions, and image findings was constructed, and the VQA model was fine-tuned on it. Language evaluation metrics such as BLEU were used to evaluate the generated image findings. The VQA dataset constructed using the proposed method contained image findings with natural expressions as radiological descriptions. In addition, the generated image findings showed a high CIDEr score of 3.896, and a high agreement with the reference findings was obtained through evaluation based on morphological characteristics. We constructed a VQA dataset for chest CT images using structured information on the morphological characteristics from the LIDC-IDRI dataset. Methods for generating image findings in response to these questions have also been investigated. Based on the generated results and evaluation metric scores, the proposed method was effective as an interactive diagnostic support system that can present image findings according to physicians' interests.

