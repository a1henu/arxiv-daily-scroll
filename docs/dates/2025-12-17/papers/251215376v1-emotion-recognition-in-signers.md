---
layout: default
title: Emotion Recognition in Signers
---

# Emotion Recognition in Signers
**arXiv**：[2512.15376v1](https://arxiv.org/abs/2512.15376) · [PDF](https://arxiv.org/pdf/2512.15376.pdf)  
**作者**：Kotaro Funakoshi, Yaoxiong Zhu  

**一句话要点**：提出跨语言方法解决手语者情感识别中表情重叠与数据稀缺问题

**关键词**：手语情感识别, 跨语言迁移, 面部表情分析, 手部运动特征, 数据集构建

## 3 点简述
- 核心问题：手语中语法与情感面部表情重叠，且训练数据稀缺。
- 方法要点：利用eJSL和BOBSL数据集，结合文本情感识别与手部运动特征。
- 实验或效果：跨语言迁移缓解数据不足，时间片段选择与手部运动提升识别效果。

## 摘要（原文）

> Recognition of signers' emotions suffers from one theoretical challenge and one practical challenge, namely, the overlap between grammatical and affective facial expressions and the scarcity of data for model training. This paper addresses these two challenges in a cross-lingual setting using our eJSL dataset, a new benchmark dataset for emotion recognition in Japanese Sign Language signers, and BOBSL, a large British Sign Language dataset with subtitles. In eJSL, two signers expressed 78 distinct utterances with each of seven different emotional states, resulting in 1,092 video clips. We empirically demonstrate that 1) textual emotion recognition in spoken language mitigates data scarcity in sign language, 2) temporal segment selection has a significant impact, and 3) incorporating hand motion enhances emotion recognition in signers. Finally we establish a stronger baseline than spoken language LLMs.

