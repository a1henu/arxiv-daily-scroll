---
layout: default
title: Layer by layer, module by module: Choose both for optimal OOD probing of ViT
---

# Layer by layer, module by module: Choose both for optimal OOD probing of ViT
**arXiv**：[2603.05280v1](https://arxiv.org/abs/2603.05280) · [PDF](https://arxiv.org/pdf/2603.05280.pdf)  
**作者**：Ambroise Odonnat, Vasilii Feofanov, Laetitia Chapel, Romain Tavenard, Ievgen Redko  

**一句话要点**：分析ViT中间层与模块以优化分布偏移下的OOD探测性能

**关键词**：视觉Transformer, 分布偏移, 线性探测, 中间层分析, 模块级别分析, OOD探测

## 3 点简述
- 核心问题：预训练与下游数据分布偏移导致ViT深层性能下降
- 方法要点：在模块级别精细分析，比较前馈网络与自注意力模块的激活
- 实验或效果：前馈网络激活在强偏移下最优，自注意力归一化输出在弱偏移下最优

## 摘要（原文）

> Recent studies have observed that intermediate layers of foundation models often yield more discriminative representations than the final layer. While initially attributed to autoregressive pretraining, this phenomenon has also been identified in models trained via supervised and discriminative self-supervised objectives. In this paper, we conduct a comprehensive study to analyze the behavior of intermediate layers in pretrained vision transformers. Through extensive linear probing experiments across a diverse set of image classification benchmarks, we find that distribution shift between pretraining and downstream data is the primary cause of performance degradation in deeper layers. Furthermore, we perform a fine-grained analysis at the module level. Our findings reveal that standard probing of transformer block outputs is suboptimal; instead, probing the activation within the feedforward network yields the best performance under significant distribution shift, whereas the normalized output of the multi-head self-attention module is optimal when the shift is weak.

