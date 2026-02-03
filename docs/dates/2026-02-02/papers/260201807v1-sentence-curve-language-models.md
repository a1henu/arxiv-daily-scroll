---
layout: default
title: Sentence Curve Language Models
---

# Sentence Curve Language Models
**arXiv**：[2602.01807v1](https://arxiv.org/abs/2602.01807) · [PDF](https://arxiv.org/pdf/2602.01807.pdf)  
**作者**：DongNyeong Heo, Heelyoul Choi  

**一句话要点**：提出句子曲线语言模型以解决静态词嵌入忽略全局结构的问题

**关键词**：句子曲线表示, 扩散语言模型, 全局结构建模, 连续句子嵌入, 语言模型正则化

## 3 点简述
- 核心问题：静态词嵌入对相邻词不敏感，导致模型忽视句子全局结构
- 方法要点：引入句子曲线作为连续表示，扩展扩散模型预测曲线而非静态嵌入
- 实验或效果：在IWSLT14和WMT14上达到扩散语言模型SOTA，训练稳定且无需繁重知识蒸馏

## 摘要（原文）

> Language models (LMs) are a central component of modern AI systems, and diffusion-based language models (DLMs) have recently emerged as a competitive alternative. Both paradigms rely on word embeddings not only to represent the input sentence, but also to represent the target sentence that backbone models are trained to predict. We argue that such static embedding of the target word is insensitive to neighboring words, encouraging locally accurate word prediction while neglecting global structure across the target sentence. To address this limitation, we propose a continuous sentence representation, termed sentence curve, defined as a spline curve whose control points affect multiple words in the sentence. Based on this representation, we introduce sentence curve language model (SCLM), which extends DLMs to predict sentence curves instead of the static word embeddings. We theoretically show that sentence curve prediction induces a regularization effect that promotes global structure modeling, and characterize how different sentence curve types affect this behavior. Empirically, SCLM achieves SOTA performance among DLMs on IWSLT14 and WMT14, shows stable training without burdensome knowledge distillation, and demonstrates promising potential compared to discrete DLMs on LM1B.

