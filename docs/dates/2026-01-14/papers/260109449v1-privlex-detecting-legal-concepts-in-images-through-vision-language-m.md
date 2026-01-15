---
layout: default
title: PrivLEX: Detecting legal concepts in images through Vision-Language Models
---

# PrivLEX: Detecting legal concepts in images through Vision-Language Models
**arXiv**：[2601.09449v1](https://arxiv.org/abs/2601.09449) · [PDF](https://arxiv.org/pdf/2601.09449.pdf)  
**作者**：Darya Baranouskaya, Andrea Cavallaro  

**一句话要点**：提出PrivLEX，基于视觉语言模型检测图像中的法律概念以实现可解释隐私分类

**关键词**：图像隐私分类, 视觉语言模型, 零样本检测, 可解释性, 法律概念对齐, 概念瓶颈模型

## 3 点简述
- 核心问题：图像隐私分类需与法律定义的个人数据概念对齐，现有方法缺乏可解释性
- 方法要点：利用零样本视觉语言模型检测概念，通过无标签概念瓶颈模型实现可解释分类，无需训练时概念标签
- 实验或效果：验证PrivLEX能识别图像中的个人数据概念，并分析人类标注者对概念敏感度的感知

## 摘要（原文）

> We present PrivLEX, a novel image privacy classifier that grounds its decisions in legally defined personal data concepts. PrivLEX is the first interpretable privacy classifier aligned with legal concepts that leverages the recognition capabilities of Vision-Language Models (VLMs). PrivLEX relies on zero-shot VLM concept detection to provide interpretable classification through a label-free Concept Bottleneck Model, without requiring explicit concept labels during training. We demonstrate PrivLEX's ability to identify personal data concepts that are present in images. We further analyse the sensitivity of such concepts as perceived by human annotators of image privacy datasets.

