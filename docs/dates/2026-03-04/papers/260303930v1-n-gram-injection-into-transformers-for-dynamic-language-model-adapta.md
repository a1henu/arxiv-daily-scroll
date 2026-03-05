---
layout: default
title: N-gram Injection into Transformers for Dynamic Language Model Adaptation in Handwritten Text Recognition
---

# N-gram Injection into Transformers for Dynamic Language Model Adaptation in Handwritten Text Recognition
**arXiv**：[2603.03930v1](https://arxiv.org/abs/2603.03930) · [PDF](https://arxiv.org/pdf/2603.03930.pdf)  
**作者**：Florent Meyer, Laurent Guichard, Denis Coquenet, Guillaume Gravier, Yann Soullard, Bertrand Coüasnon  

**一句话要点**：提出外部n-gram注入方法，以动态适应手写文本识别中的语言分布偏移问题。

**关键词**：手写文本识别, Transformer, 语言模型适应, n-gram注入, 动态推理

## 3 点简述
- 核心问题：Transformer网络在语言分布偏移的目标语料上性能显著下降。
- 方法要点：在推理时早期注入n-gram语言模型，无需额外图像-文本对训练。
- 实验或效果：在三个手写数据集上验证，显著缩小源与目标语料间的性能差距。

## 摘要（原文）

> Transformer-based encoder-decoder networks have recently achieved impressive results in handwritten text recognition, partly thanks to their auto-regressive decoder which implicitly learns a language model. However, such networks suffer from a large performance drop when evaluated on a target corpus whose language distribution is shifted from the source text seen during training. To retain recognition accuracy despite this language shift, we propose an external n-gram injection (NGI) for dynamic adaptation of the network's language modeling at inference time. Our method allows switching to an n-gram language model estimated on a corpus close to the target distribution, therefore mitigating bias without any extra training on target image-text pairs. We opt for an early injection of the n-gram into the transformer decoder so that the network learns to fully leverage text-only data at the low additional cost of n-gram inference. Experiments on three handwritten datasets demonstrate that the proposed NGI significantly reduces the performance gap between source and target corpora.

