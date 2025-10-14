---
layout: default
title: Saudi Sign Language Translation Using T5
---

# Saudi Sign Language Translation Using T5
**arXiv**：[2510.11183v1](https://arxiv.org/abs/2510.11183) · [PDF](https://arxiv.org/pdf/2510.11183.pdf)  
**作者**：Ali Alhejab, Tomas Zelezny, Lamya Alkanhal, Ivan Gruber, Yazeed Alharbi, Jakub Straka, Vaclav Javorek, Marek Hruz, Badriah Alkalifah, Ahmed Ali  

**一句话要点**：应用T5模型翻译沙特手语，利用ASL预训练提升性能

**关键词**：沙特手语翻译, T5模型, 跨语言迁移, 预训练优化, 手语数据集

## 3 点简述
- 核心问题：沙特手语翻译面临独特挑战，如面部覆盖影响识别。
- 方法要点：比较T5模型在ASL预训练与直接SSL训练的效果。
- 实验或效果：ASL预训练显著提升BLEU-4分数约3倍。

## 摘要（原文）

> This paper explores the application of T5 models for Saudi Sign Language
> (SSL) translation using a novel dataset. The SSL dataset includes three
> challenging testing protocols, enabling comprehensive evaluation across
> different scenarios. Additionally, it captures unique SSL characteristics, such
> as face coverings, which pose challenges for sign recognition and translation.
> In our experiments, we investigate the impact of pre-training on American Sign
> Language (ASL) data by comparing T5 models pre-trained on the YouTubeASL
> dataset with models trained directly on the SSL dataset. Experimental results
> demonstrate that pre-training on YouTubeASL significantly improves models'
> performance (roughly $3\times$ in BLEU-4), indicating cross-linguistic
> transferability in sign language models. Our findings highlight the benefits of
> leveraging large-scale ASL data to improve SSL translation and provide insights
> into the development of more effective sign language translation systems. Our
> code is publicly available at our GitHub repository.

