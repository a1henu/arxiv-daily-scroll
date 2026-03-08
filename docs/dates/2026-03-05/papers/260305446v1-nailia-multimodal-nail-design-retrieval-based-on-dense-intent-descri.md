---
layout: default
title: NaiLIA: Multimodal Nail Design Retrieval Based on Dense Intent Descriptions and Palette Queries
---

# NaiLIA: Multimodal Nail Design Retrieval Based on Dense Intent Descriptions and Palette Queries
**arXiv**：[2603.05446v1](https://arxiv.org/abs/2603.05446) · [PDF](https://arxiv.org/pdf/2603.05446.pdf)  
**作者**：Kanon Amemiya, Daichi Yashima, Kei Katsumata, Takumi Komatsu, Ryosuke Korekata, Seitaro Otsuki, Komei Sugiura  

**一句话要点**：提出NaiLIA方法，基于密集意图描述和调色板查询实现美甲设计图像检索。

**关键词**：美甲设计检索, 密集意图描述, 调色板查询, 多模态对齐, 松弛损失, 基准数据集

## 3 点简述
- 核心问题：现有视觉语言基础模型难以处理美甲设计中的密集意图描述和颜色调色板查询。
- 方法要点：引入基于置信度分数的松弛损失，对齐未标记图像与描述，支持多模态检索。
- 实验或效果：在包含10,625张图像的基准上，NaiLIA优于标准方法，验证了其有效性。

## 摘要（原文）

> We focus on the task of retrieving nail design images based on dense intent descriptions, which represent multi-layered user intent for nail designs. This is challenging because such descriptions specify unconstrained painted elements and pre-manufactured embellishments as well as visual characteristics, themes, and overall impressions. In addition to these descriptions, we assume that users provide palette queries by specifying zero or more colors via a color picker, enabling the expression of subtle and continuous color nuances. Existing vision-language foundation models often struggle to incorporate such descriptions and palettes. To address this, we propose NaiLIA, a multimodal retrieval method for nail design images, which comprehensively aligns with dense intent descriptions and palette queries during retrieval. Our approach introduces a relaxed loss based on confidence scores for unlabeled images that can align with the descriptions. To evaluate NaiLIA, we constructed a benchmark consisting of 10,625 images collected from people with diverse cultural backgrounds. The images were annotated with long and dense intent descriptions given by over 200 annotators. Experimental results demonstrate that NaiLIA outperforms standard methods.

