---
layout: default
title: Gained in Translation: Privileged Pairwise Judges Enhance Multilingual Reasoning
---

# Gained in Translation: Privileged Pairwise Judges Enhance Multilingual Reasoning
**arXiv**：[2601.18722v1](https://arxiv.org/abs/2601.18722) · [PDF](https://arxiv.org/pdf/2601.18722.pdf)  
**作者**：Lintang Sutawika, Gokul Swamy, Zhiwei Steven Wu, Graham Neubig  

**一句话要点**：提出SP3F框架，通过特权成对反馈增强多语言推理，无需目标语言数据。

**关键词**：多语言推理, 强化学习, 自对弈训练, 特权信息, 模型微调, 跨语言泛化

## 3 点简述
- 核心问题：当前推理大模型在训练数据较少的语言上性能显著低于英语。
- 方法要点：采用两阶段框架，包括监督微调和带特权成对反馈的自对弈强化学习。
- 实验或效果：SP3F大幅提升基础模型性能，在多项任务上优于全量后训练模型，数据需求更少。

## 摘要（原文）

> When asked a question in a language less seen in its training data, current reasoning large language models (RLMs) often exhibit dramatically lower performance than when asked the same question in English. In response, we introduce \texttt{SP3F} (Self-Play with Privileged Pairwise Feedback), a two-stage framework for enhancing multilingual reasoning without \textit{any} data in the target language(s). First, we supervise fine-tune (SFT) on translated versions of English question-answer pairs to raise base model correctness. Second, we perform RL with feedback from a pairwise judge in a self-play fashion, with the judge receiving the English reference response as \textit{privileged information}. Thus, even when none of the model's responses are completely correct, the privileged pairwise judge can still tell which response is better. End-to-end, \texttt{SP3F} greatly improves base model performance, even outperforming fully post-trained models on multiple math and non-math tasks with less than
>   of the training data across the single-language, multilingual, and generalization to unseen language settings.

