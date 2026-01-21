---
layout: default
title: Soft Tail-dropping for Adaptive Visual Tokenization
---

# Soft Tail-dropping for Adaptive Visual Tokenization
**arXiv**：[2601.14246v1](https://arxiv.org/abs/2601.14246) · [PDF](https://arxiv.org/pdf/2601.14246.pdf)  
**作者**：Zeyuan Chen, Kai Zhang, Zhuowen Tu, Yuanjun Xiong  

**一句话要点**：提出Soft Tail-dropping自适应视觉分词器，为因果自回归视觉生成模型提供长度自适应的一维离散视觉标记。

**关键词**：视觉分词器, 自适应标记, 因果自回归模型, 视觉生成, 离散编码, 图像复杂度

## 3 点简述
- 核心问题：传统视觉分词器输出固定长度标记，难以适应图像结构复杂性和细节水平，限制了因果自回归视觉生成模型的性能。
- 方法要点：STAT通过自适应选择每图像输出标记数量，编码为离散代码序列及每个标记的保留概率，并正则化这些概率单调递减以对齐图像级复杂度。
- 实验或效果：在ImageNet-1k上，结合STAT的因果自回归模型在视觉生成质量上具有竞争力，并展现出良好的缩放行为。

## 摘要（原文）

> We present Soft Tail-dropping Adaptive Tokenizer (STAT), a 1D discrete visual tokenizer that adaptively chooses the number of output tokens per image according to its structural complexity and level of detail. STAT encodes an image into a sequence of discrete codes together with per-token keep probabilities. Beyond standard autoencoder objectives, we regularize these keep probabilities to be monotonically decreasing along the sequence and explicitly align their distribution with an image-level complexity measure. As a result, STAT produces length-adaptive 1D visual tokens that are naturally compatible with causal 1D autoregressive (AR) visual generative models. On ImageNet-1k, equipping vanilla causal AR models with STAT yields competitive or superior visual generation quality compared to other probabilistic model families, while also exhibiting favorable scaling behavior that has been elusive in prior vanilla AR visual generation attempts.

