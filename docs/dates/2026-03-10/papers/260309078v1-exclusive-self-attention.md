---
layout: default
title: Exclusive Self Attention
---

# Exclusive Self Attention
**arXiv**：[2603.09078v1](https://arxiv.org/abs/2603.09078) · [PDF](https://arxiv.org/pdf/2603.09078.pdf)  
**作者**：Shuangfei Zhai  

**一句话要点**：提出独占自注意力以改进Transformer序列建模性能

**关键词**：自注意力机制, Transformer模型, 序列建模, 语言建模, 正交约束

## 3 点简述
- 核心问题：标准自注意力可能过度关注自身位置信息，影响上下文建模。
- 方法要点：通过约束注意力仅捕获与自身值向量正交的信息，排除自身位置影响。
- 实验或效果：在语言建模任务中，XSA在高达2.7B参数模型上优于SA，且序列越长增益越大。

## 摘要（原文）

> We introduce exclusive self attention (XSA), a simple modification of self attention (SA) that improves Transformer's sequence modeling performance. The key idea is to constrain attention to capture only information orthogonal to the token's own value vector (thus excluding information of self position), encouraging better context modeling. Evaluated on the standard language modeling task, XSA consistently outperforms SA across model sizes up to 2.7B parameters and shows increasingly larger gains as sequence length grows.

