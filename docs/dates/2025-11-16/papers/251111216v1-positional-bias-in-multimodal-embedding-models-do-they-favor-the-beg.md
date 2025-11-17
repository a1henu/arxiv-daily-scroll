---
layout: default
title: Positional Bias in Multimodal Embedding Models: Do They Favor the Beginning, the Middle, or the End?
---

# Positional Bias in Multimodal Embedding Models: Do They Favor the Beginning, the Middle, or the End?
**arXiv**：[2511.11216v1](https://arxiv.org/abs/2511.11216) · [PDF](https://arxiv.org/pdf/2511.11216.pdf)  
**作者**：Kebin Wu, Fatima Albreiki  

**一句话要点**：研究多模态嵌入模型中的位置偏差及其在图像-文本检索中的影响

**关键词**：位置偏差, 多模态嵌入模型, 图像-文本检索, 文本编码器, 图像编码器, 训练损失

## 3 点简述
- 核心问题：多模态表示模型中存在位置偏差，即模型过度强调输入位置而非内容。
- 方法要点：区分上下文重要性与位置偏差，评估不同模型和数据集中的偏差程度。
- 实验或效果：文本编码器偏向输入开头，图像编码器偏向开头和结尾，偏差源于多种因素。

## 摘要（原文）

> Positional bias - where models overemphasize certain positions regardless of content - has been shown to negatively impact model performance across various tasks. While recent research has extensively examined positional bias in text generation models, its presence and effects in representation models remain underexplored. Even less is known about such biases in multimodal models. In this work, we investigate positional bias in multimodal representation models, specifically in the context of image-text retrieval. We begin by distinguishing between context importance and positional bias, and then assess the presence and extent of positional bias across different models and datasets. Our experiments demonstrate that positional bias is prevalent in multimodal models, but manifests differently across modalities: text encoders tend to exhibit bias toward the beginning of the input, whereas image encoders show bias at both the beginning and end. Furthermore, we find that this bias arises from, or is amplified by, a combination of factors, including the positional encoding scheme, training loss, context importance, and the nature of using image-text pairs in multimodal training.

