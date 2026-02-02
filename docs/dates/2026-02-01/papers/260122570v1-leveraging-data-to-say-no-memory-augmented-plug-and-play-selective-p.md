---
layout: default
title: Leveraging Data to Say No: Memory Augmented Plug-and-Play Selective Prediction
---

# Leveraging Data to Say No: Memory Augmented Plug-and-Play Selective Prediction
**arXiv**：[2601.22570v1](https://arxiv.org/abs/2601.22570) · [PDF](https://arxiv.org/pdf/2601.22570.pdf)  
**作者**：Aditya Sarkar, Yi Li, Jiacheng Cheng, Shlok Mishra, Nuno Vasconcelos  

**一句话要点**：提出记忆增强即插即用选择性预测方法，以解决视觉语言基础模型在开放集任务中的预测不确定性。

**关键词**：选择性预测, 视觉语言模型, 记忆增强, 开放集任务, 嵌入校准, 即插即用方法

## 3 点简述
- 核心问题：现有选择性预测方法主要针对闭集任务，难以处理视觉语言基础模型在开放集和无限词汇任务中的不稳定嵌入和分数校准问题。
- 方法要点：通过检索数据集增强即插即用选择性预测，利用最近邻平均减少嵌入方差，并结合对比归一化改进分数校准。
- 实验或效果：在多个数据集上验证，MA-PaPSP在选择性描述、图像-文本匹配和细粒度分类中优于基线方法，代码已公开。

## 摘要（原文）

> Selective prediction aims to endow predictors with a reject option, to avoid low confidence predictions. However, existing literature has primarily focused on closed-set tasks, such as visual question answering with predefined options or fixed-category classification. This paper considers selective prediction for visual language foundation models, addressing a taxonomy of tasks ranging from closed to open set and from finite to unbounded vocabularies, as in image captioning. We seek training-free approaches of low-complexity, applicable to any foundation model and consider methods based on external vision-language model embeddings, like CLIP. This is denoted as Plug-and-Play Selective Prediction (PaPSP). We identify two key challenges: (1) instability of the visual-language representations, leading to high variance in image-text embeddings, and (2) poor calibration of similarity scores. To address these issues, we propose a memory augmented PaPSP (MA-PaPSP) model, which augments PaPSP with a retrieval dataset of image-text pairs. This is leveraged to reduce embedding variance by averaging retrieved nearest-neighbor pairs and is complemented by the use of contrastive normalization to improve score calibration. Through extensive experiments on multiple datasets, we show that MA-PaPSP outperforms PaPSP and other selective prediction baselines for selective captioning, image-text matching, and fine-grained classification. Code is publicly available at https://github.com/kingston-aditya/MA-PaPSP.

