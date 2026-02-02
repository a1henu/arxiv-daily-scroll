---
layout: default
title: Vision-Language Models Unlock Task-Centric Latent Actions
---

# Vision-Language Models Unlock Task-Centric Latent Actions
**arXiv**：[2601.22714v1](https://arxiv.org/abs/2601.22714) · [PDF](https://arxiv.org/pdf/2601.22714.pdf)  
**作者**：Alexander Nikulin, Ilya Zisman, Albina Klepach, Denis Tarasov, Alexander Derevyagin, Andrei Polubarov, Lyubaykin Nikita, Vladislav Kurenkov  

**一句话要点**：提出利用视觉语言模型提供可提示表示，以提升潜在动作模型在含干扰观测中的性能。

**关键词**：视觉语言模型, 潜在动作模型, 无监督学习, 任务中心表示, 干扰鲁棒性, 下游任务评估

## 3 点简述
- 潜在动作模型在含动作相关干扰的观测中易编码噪声而非有意义的潜在动作。
- 利用视觉语言模型的常识推理能力，以无监督方式分离可控变化与噪声。
- 实验显示，简单提示视觉语言模型忽略干扰可显著提升潜在动作质量，下游成功率最高提升六倍。

## 摘要（原文）

> Latent Action Models (LAMs) have rapidly gained traction as an important component in the pre-training pipelines of leading Vision-Language-Action models. However, they fail when observations contain action-correlated distractors, often encoding noise instead of meaningful latent actions. Humans, on the other hand, can effortlessly distinguish task-relevant motions from irrelevant details in any video given only a brief task description. In this work, we propose to utilize the common-sense reasoning abilities of Vision-Language Models (VLMs) to provide promptable representations, effectively separating controllable changes from the noise in unsupervised way. We use these representations as targets during LAM training and benchmark a wide variety of popular VLMs, revealing substantial variation in the quality of promptable representations as well as their robustness to different prompts and hyperparameters. Interestingly, we find that more recent VLMs may perform worse than older ones. Finally, we show that simply asking VLMs to ignore distractors can substantially improve latent action quality, yielding up to a six-fold increase in downstream success rates on Distracting MetaWorld.

