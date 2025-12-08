---
layout: default
title: EmoStyle: Emotion-Driven Image Stylization
---

# EmoStyle: Emotion-Driven Image Stylization
**arXiv**：[2512.05478v1](https://arxiv.org/abs/2512.05478) · [PDF](https://arxiv.org/pdf/2512.05478.pdf)  
**作者**：Jingyuan Yang, Zihuan Bai, Hui Huang  

**一句话要点**：提出EmoStyle框架以解决情感驱动图像风格化中数据缺失和情感-风格映射问题。

**关键词**：情感驱动图像风格化, 情感-内容推理器, 风格量化器, EmoStyleSet数据集, 情感感知风格字典

## 3 点简述
- 核心问题：现有图像风格化方法忽略情感表达，缺乏训练数据和情感-风格映射机制。
- 方法要点：构建EmoStyleSet数据集，设计Emotion-Content Reasoner和Style Quantizer来学习情感感知风格查询。
- 实验或效果：通过用户研究和量化评估，EmoStyle在保持内容一致性的同时增强情感表达力。

## 摘要（原文）

> Art has long been a profound medium for expressing emotions. While existing image stylization methods effectively transform visual appearance, they often overlook the emotional impact carried by styles. To bridge this gap, we introduce Affective Image Stylization (AIS), a task that applies artistic styles to evoke specific emotions while preserving content. We present EmoStyle, a framework designed to address key challenges in AIS, including the lack of training data and the emotion-style mapping. First, we construct EmoStyleSet, a content-emotion-stylized image triplet dataset derived from ArtEmis to support AIS. We then propose an Emotion-Content Reasoner that adaptively integrates emotional cues with content to learn coherent style queries. Given the discrete nature of artistic styles, we further develop a Style Quantizer that converts continuous style features into emotion-related codebook entries. Extensive qualitative and quantitative evaluations, including user studies, demonstrate that EmoStyle enhances emotional expressiveness while maintaining content consistency. Moreover, the learned emotion-aware style dictionary is adaptable to other generative tasks, highlighting its potential for broader applications. Our work establishes a foundation for emotion-driven image stylization, expanding the creative potential of AI-generated art.

