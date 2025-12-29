---
layout: default
title: Training-free Conditional Image Embedding Framework Leveraging Large Vision Language Models
---

# Training-free Conditional Image Embedding Framework Leveraging Large Vision Language Models
**arXiv**：[2512.21860v1](https://arxiv.org/abs/2512.21860) · [PDF](https://arxiv.org/pdf/2512.21860.pdf)  
**作者**：Masayuki Kawarada, Kosuke Yamada, Antonio Tejero-de-Pablos, Naoto Inoue  

**一句话要点**：提出DIOR框架，利用大型视觉语言模型生成条件图像嵌入，无需训练即可处理任意图像和条件。

**关键词**：条件图像嵌入, 大型视觉语言模型, 训练免费方法, 图像相似性任务, CLIP模型

## 3 点简述
- 核心问题：条件图像嵌入需根据文本条件聚焦图像特定方面，现有模型如CLIP未专门设计此功能。
- 方法要点：通过提示大型视觉语言模型用单字描述图像，提取最后令牌的隐藏状态向量作为嵌入，无需额外训练。
- 实验或效果：在条件图像相似性任务中，DIOR优于包括CLIP在内的无训练基线，并在多设置中超越需训练的方法。

## 摘要（原文）

> Conditional image embeddings are feature representations that focus on specific aspects of an image indicated by a given textual condition (e.g., color, genre), which has been a challenging problem. Although recent vision foundation models, such as CLIP, offer rich representations of images, they are not designed to focus on a specified condition. In this paper, we propose DIOR, a method that leverages a large vision-language model (LVLM) to generate conditional image embeddings. DIOR is a training-free approach that prompts the LVLM to describe an image with a single word related to a given condition. The hidden state vector of the LVLM's last token is then extracted as the conditional image embedding. DIOR provides a versatile solution that can be applied to any image and condition without additional training or task-specific priors. Comprehensive experimental results on conditional image similarity tasks demonstrate that DIOR outperforms existing training-free baselines, including CLIP. Furthermore, DIOR achieves superior performance compared to methods that require additional training across multiple settings.

