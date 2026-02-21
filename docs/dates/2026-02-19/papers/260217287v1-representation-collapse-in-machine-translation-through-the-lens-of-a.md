---
layout: default
title: Representation Collapse in Machine Translation Through the Lens of Angular Dispersion
---

# Representation Collapse in Machine Translation Through the Lens of Angular Dispersion
**arXiv**：[2602.17287v1](https://arxiv.org/abs/2602.17287) · [PDF](https://arxiv.org/pdf/2602.17287.pdf)  
**作者**：Evgeniia Tokarchuk, Maya K. Nachesa, Sergey Troshin, Vlad Niculae  

**一句话要点**：提出基于角分散的正则化方法，缓解机器翻译中Transformer的表征塌陷问题。

**关键词**：表征塌陷, 机器翻译, Transformer, 角分散正则化, 量化模型

## 3 点简述
- 分析离散和连续NMT Transformer训练中表征塌陷的动态过程。
- 引入角分散正则化，实验证明能减轻塌陷并提升翻译质量。
- 量化模型也表现出塌陷，正则化在量化后仍保持益处。

## 摘要（原文）

> Modern neural translation models based on the Transformer architecture are known for their high performance, particularly when trained on high-resource datasets. A standard next-token prediction training strategy, while widely adopted in practice, may lead to overlooked artifacts such as representation collapse. Previous works have shown that this problem is especially pronounced in the representation of the deeper Transformer layers, where it often fails to efficiently utilize the geometric space. Representation collapse is even more evident in end-to-end training of continuous-output neural machine translation, where the trivial solution would be to set all vectors to the same value. In this work, we analyze the dynamics of representation collapse at different levels of discrete and continuous NMT transformers throughout training. We incorporate an existing regularization method based on angular dispersion and demonstrate empirically that it not only mitigates collapse but also improves translation quality. Furthermore, we show that quantized models exhibit similar collapse behavior and that the benefits of regularization are preserved even after quantization.

