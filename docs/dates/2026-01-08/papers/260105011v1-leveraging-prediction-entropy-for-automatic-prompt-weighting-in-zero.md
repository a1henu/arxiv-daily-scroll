---
layout: default
title: Leveraging Prediction Entropy for Automatic Prompt Weighting in Zero-Shot Audio-Language Classification
---

# Leveraging Prediction Entropy for Automatic Prompt Weighting in Zero-Shot Audio-Language Classification
**arXiv**：[2601.05011v1](https://arxiv.org/abs/2601.05011) · [PDF](https://arxiv.org/pdf/2601.05011.pdf)  
**作者**：Karim El Khoury, Maxime Zanella, Tiffanie Godelaine, Christophe De Vleeschouwer, Benoit Macq  

**一句话要点**：提出基于预测熵的自动提示加权方法，以提升零样本音频-语言分类的鲁棒性。

**关键词**：零样本学习, 音频分类, 提示工程, 预测熵, 自动加权

## 3 点简述
- 核心问题：音频-语言模型在零样本分类中对文本提示的措辞高度敏感，性能波动大。
- 方法要点：设计目标函数最小化预测熵，利用低熵作为高置信度代理，自动加权提示贡献。
- 实验或效果：在五个音频数据集上相比传统提示集成方法，准确率提升显著，无需额外标注。

## 摘要（原文）

> Audio-language models have recently demonstrated strong zero-shot capabilities by leveraging natural-language supervision to classify audio events without labeled training data. Yet, their performance is highly sensitive to the wording of text prompts, with small variations leading to large fluctuations in accuracy. Prior work has mitigated this issue through prompt learning or prompt ensembling. However, these strategies either require annotated data or fail to account for the fact that some prompts may negatively impact performance. In this work, we present an entropy-guided prompt weighting approach that aims to find a robust combination of prompt contributions to maximize prediction confidence. To this end, we formulate a tailored objective function that minimizes prediction entropy to yield new prompt weights, utilizing low-entropy as a proxy for high confidence. Our approach can be applied to individual samples or a batch of audio samples, requiring no additional labels and incurring negligible computational overhead. Experiments on five audio classification datasets covering environmental, urban, and vocal sounds, demonstrate consistent gains compared to classical prompt ensembling methods in a zero-shot setting, with accuracy improvements 5-times larger across the whole benchmark.

