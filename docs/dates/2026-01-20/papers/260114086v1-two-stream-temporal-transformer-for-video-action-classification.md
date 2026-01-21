---
layout: default
title: Two-Stream temporal transformer for video action classification
---

# Two-Stream temporal transformer for video action classification
**arXiv**：[2601.14086v1](https://arxiv.org/abs/2601.14086) · [PDF](https://arxiv.org/pdf/2601.14086.pdf)  
**作者**：Nattapong Kurpukdee, Adrian G. Bors  

**一句话要点**：提出双流时序Transformer模型，用于视频动作分类，结合内容与光流信息提取时空特征。

**关键词**：视频动作分类, 双流Transformer, 时空特征提取, 自注意力机制, 光流表示

## 3 点简述
- 核心问题：视频理解中运动表示对动作识别等应用至关重要，需有效提取时空信息。
- 方法要点：采用双流Transformer，分别处理内容帧和光流，通过自注意力机制融合时空特征。
- 实验或效果：在三个人类活动视频数据集上验证，分类结果优异，证明模型有效性。

## 摘要（原文）

> Motion representation plays an important role in video understanding and has many applications including action recognition, robot and autonomous guidance or others. Lately, transformer networks, through their self-attention mechanism capabilities, have proved their efficiency in many applications. In this study, we introduce a new two-stream transformer video classifier, which extracts spatio-temporal information from content and optical flow representing movement information. The proposed model identifies self-attention features across the joint optical flow and temporal frame domain and represents their relationships within the transformer encoder mechanism. The experimental results show that our proposed methodology provides excellent classification results on three well-known video datasets of human activities.

