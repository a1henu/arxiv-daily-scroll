---
layout: default
title: Reading $\neq$ Seeing: Diagnosing and Closing the Typography Gap in Vision-Language Models
---

# Reading $\neq$ Seeing: Diagnosing and Closing the Typography Gap in Vision-Language Models
**arXiv**：[2603.08497v1](https://arxiv.org/abs/2603.08497) · [PDF](https://arxiv.org/pdf/2603.08497.pdf)  
**作者**：Heng Zhou, Ao Yu, Li Kang, Yuchen Fan, Yutao Fan, Xiufeng Song, Hejia Geng, Yiran Qin  

**一句话要点**：揭示视觉语言模型在字体识别上的感知差距，并通过微调提升性能

**关键词**：视觉语言模型, 字体识别, 感知差距, 微调优化, 合成数据, 视觉推理

## 3 点简述
- 核心问题：视觉语言模型能准确读取图像文本，但对字体样式等视觉属性识别能力差
- 方法要点：系统评估15个先进模型在字体族、大小、样式和颜色上的表现，并基于合成数据微调
- 实验或效果：微调显著缩小与闭源系统的差距，但字体样式识别仍具挑战性

## 摘要（原文）

> Vision-Language Models achieve near-perfect accuracy at reading text in images, yet prove largely typography-blind: capable of recognizing what text says, but not how it looks. We systematically investigate this gap by evaluating font family, size, style, and color recognition across 26 fonts, four scripts, and three difficulty levels. Our evaluation of 15 state-of-the-art VLMs reveals a striking perception hierarchy: color recognition is near-perfect, yet font style detection remains universally poor. We further find that model scale fails to predict performance and that accuracy is uniform across difficulty levels, together pointing to a training-data omission rather than a capacity ceiling. LoRA fine-tuning on a small set of synthetic samples substantially improves an open-source model, narrowing the gap to the best closed-source system and surpassing it on font size recognition. Font style alone remains resistant to fine-tuning, suggesting that relational visual reasoning may require architectural innovation beyond current patch-based encoders. We release our evaluation framework, data, and fine-tuning recipe to support progress in closing the typographic gap in vision-language understanding.

