---
layout: default
title: MEGnifying Emotion: Sentiment Analysis from Annotated Brain Data
---

# MEGnifying Emotion: Sentiment Analysis from Annotated Brain Data
**arXiv**：[2601.18792v1](https://arxiv.org/abs/2601.18792) · [PDF](https://arxiv.org/pdf/2601.18792.pdf)  
**作者**：Brian Liu, Oiwi Parker Jones  

**一句话要点**：提出基于预训练文本情感模型标注脑磁图数据的方法，以解码大脑活动中的情感信号。

**关键词**：情感解码, 脑磁图, 文本情感模型, 脑数据标注, Brain-to-Sentiment模型

## 3 点简述
- 核心问题：现有脑数据缺乏情感标注，阻碍从大脑活动解码情感的研究。
- 方法要点：利用预训练文本情感模型标注脑磁图数据，通过文本-音频对齐将情感标签与脑记录对齐。
- 实验或效果：实验显示Brain-to-Sentiment模型在平衡准确率上优于基线，验证了方法的可行性。

## 摘要（原文）

> Decoding emotion from brain activity could unlock a deeper understanding of the human experience. While a number of existing datasets align brain data with speech and with speech transcripts, no datasets have annotated brain data with sentiment. To bridge this gap, we explore the use of pre-trained Text-to-Sentiment models to annotate non invasive brain recordings, acquired using magnetoencephalography (MEG), while participants listened to audiobooks. Having annotated the text, we employ force-alignment of the text and audio to align our sentiment labels with the brain recordings. It is straightforward then to train Brainto-Sentiment models on these data. Experimental results show an improvement in balanced accuracy for Brain-to-Sentiment compared to baseline, supporting the proposed approach as a proof-of-concept for leveraging existing MEG datasets and learning to decode sentiment directly from the brain.

