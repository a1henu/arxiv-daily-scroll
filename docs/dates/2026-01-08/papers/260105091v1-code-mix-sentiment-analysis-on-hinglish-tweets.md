---
layout: default
title: Code-Mix Sentiment Analysis on Hinglish Tweets
---

# Code-Mix Sentiment Analysis on Hinglish Tweets
**arXiv**：[2601.05091v1](https://arxiv.org/abs/2601.05091) · [PDF](https://arxiv.org/pdf/2601.05091.pdf)  
**作者**：Aashi Garg, Aneshya Das, Arshi Arya, Anushka Goyal, Aditi  

**一句话要点**：提出基于mBERT微调的框架，以解决Hinglish推文情感分析中的代码混合挑战。

**关键词**：代码混合情感分析, Hinglish推文, mBERT微调, 子词分词, 多语言NLP, 品牌监控

## 3 点简述
- 核心问题：传统NLP模型难以处理印地语-英语混合语言的句法和语义复杂性，导致情感分析不准确。
- 方法要点：利用mBERT的多语言能力，结合子词分词技术，有效处理拼写变体和俚语。
- 实验或效果：为品牌情感跟踪提供生产就绪的AI解决方案，并在低资源代码混合环境中建立强基准。

## 摘要（原文）

> The effectiveness of brand monitoring in India is increasingly challenged by the rise of Hinglish--a hybrid of Hindi and English--used widely in user-generated content on platforms like Twitter. Traditional Natural Language Processing (NLP) models, built for monolingual data, often fail to interpret the syntactic and semantic complexity of this code-mixed language, resulting in inaccurate sentiment analysis and misleading market insights. To address this gap, we propose a high-performance sentiment classification framework specifically designed for Hinglish tweets. Our approach fine-tunes mBERT (Multilingual BERT), leveraging its multilingual capabilities to better understand the linguistic diversity of Indian social media. A key component of our methodology is the use of subword tokenization, which enables the model to effectively manage spelling variations, slang, and out-of-vocabulary terms common in Romanized Hinglish. This research delivers a production-ready AI solution for brand sentiment tracking and establishes a strong benchmark for multilingual NLP in low-resource, code-mixed environments.

