---
layout: default
title: Deep learning for pedestrians: backpropagation in Transformers
---

# Deep learning for pedestrians: backpropagation in Transformers
**arXiv**：[2512.23329v1](https://arxiv.org/abs/2512.23329) · [PDF](https://arxiv.org/pdf/2512.23329.pdf)  
**作者**：Laurent Boué  

**一句话要点**：提出轻量级索引无关方法，推导Transformer中反向传播的梯度表达式

**关键词**：Transformer反向传播, 梯度推导, 向量化方法, LoRA微调, PyTorch实现

## 3 点简述
- 核心问题：手动推导Transformer架构的反向传播，以增强对梯度流动的理解
- 方法要点：应用向量化方法处理嵌入、多头自注意力和层归一化等新层类型
- 实验或效果：提供完整PyTorch实现和梯度更新分析表达式，支持LoRA层参数高效微调

## 摘要（原文）

> This document is a follow-up to our previous paper dedicated to a vectorized derivation of backpropagation in CNNs. Following the same principles and notations already put in place there, we now focus on transformer-based next-token-prediction architectures. To this end, we apply our lightweight index-free methodology to new types of layers such as embedding, multi-headed self-attention and layer normalization. In addition, we also provide gradient expressions for LoRA layers to illustrate parameter-efficient fine-tuning. Why bother doing manual backpropagation when there are so many tools that do this automatically? Any gap in understanding of how values propagate forward will become evident when attempting to differentiate the loss function. By working through the backward pass manually, we gain a deeper intuition for how each operation influences the final output. A complete PyTorch implementation of a minimalistic GPT-like network is also provided along with analytical expressions for of all of its gradient updates.

