---
layout: default
title: Large-Scale Aspect-Based Sentiment Analysis with Reasoning-Infused LLMs
---

# Large-Scale Aspect-Based Sentiment Analysis with Reasoning-Infused LLMs
**arXiv**：[2601.03940v1](https://arxiv.org/abs/2601.03940) · [PDF](https://arxiv.org/pdf/2601.03940.pdf)  
**作者**：Paweł Liskowski, Krzysztof Jankowski  

**一句话要点**：提出Arctic-ABSA模型，通过推理注入和大规模数据增强，提升商业场景下的细粒度情感分析性能。

**关键词**：细粒度情感分析, 推理注入, 数据增强, 多语言模型, 商业应用

## 3 点简述
- 核心问题：传统细粒度情感分析模型在商业应用中面临数据规模不足和情感类别有限的问题。
- 方法要点：扩展情感类别至五类，结合推理注入技术，并利用大规模合成数据增强训练。
- 实验或效果：在SemEval14基准上超越GPT-4o和Claude 3.5 Sonnet，多语言模型保持高准确率。

## 摘要（原文）

> We introduce Arctic-ABSA, a collection of powerful models for real-life aspect-based sentiment analysis (ABSA). Our models are tailored to commercial needs, trained on a large corpus of public data alongside carefully generated synthetic data, resulting in a dataset 20 times larger than SemEval14. We extend typical ABSA models by expanding the number of sentiment classes from the standard three (positive, negative, neutral) to five, adding mixed and unknown classes, while also jointly predicting overall text sentiment and supporting multiple languages. We experiment with reasoning injection by fine-tuning on Chain-of-Thought (CoT) examples and introduce a novel reasoning pretraining technique for encoder-only models that significantly improves downstream fine-tuning and generalization. Our 395M-parameter encoder and 8B-parameter decoder achieve up to 10 percentage points higher accuracy than GPT-4o and Claude 3.5 Sonnet, while setting new state-of-the-art results on the SemEval14 benchmark. A single multilingual model maintains 87-91% accuracy across six languages without degrading English performance. We release ABSA-mix, a large-scale benchmark aggregating 17 public ABSA datasets across 92 domains.

