---
layout: default
title: Distillation-based Layer Dropping (DLD) Effective End-to-end Framework for Dynamic Speech Networks
---

# Distillation-based Layer Dropping (DLD) Effective End-to-end Framework for Dynamic Speech Networks
**arXiv**：[2601.16117v1](https://arxiv.org/abs/2601.16117) · [PDF](https://arxiv.org/pdf/2601.16117.pdf)  
**作者**：Abdul Hannan, Daniele Falavigna, Shah Nawaz, Mubashir Noman, Markus Schedl, Alessio Brutti  

**一句话要点**：提出蒸馏层丢弃框架以优化动态语音网络的性能-计算权衡

**关键词**：动态语音网络, 层丢弃, 知识蒸馏, 端到端训练, 词错误率优化

## 3 点简述
- 核心问题：现有层丢弃方法在高低丢弃率下性能下降，影响动态模型性能。
- 方法要点：结合知识蒸馏与层丢弃，端到端训练提升动态语音网络性能。
- 实验或效果：在三个基准测试中，高丢弃率下词错误率降低9.32%，训练时间减少33.3%。

## 摘要（原文）

> Edge devices operate in constrained and varying resource settings, requiring dynamic architectures that can adapt to limitations of the available resources. To meet such demands, layer dropping ($\mathcal{LD}$) approach is typically used to transform static models into dynamic ones by skipping parts of the network along with reducing overall computational complexity. However, existing $\mathcal{LD}$ methods greatly impact the dynamic model's performance for low and high dropping cases, deteriorating the performance-computation trade-off. To this end, we propose a distillation-based layer dropping (DLD) framework that effectively combines the capabilities of knowledge distillation and $\mathcal{LD}$ in an end-to-end fashion, thereby achieving state-of-the-art performance for dynamic speech networks. Comprehensive experimentation utilizing well-known speech recognition methods, including conformer and WavLM, on three public benchmarks demonstrates the effectiveness of our framework, reducing the word error rate by $9.32\%$ and $2.25\%$ for high and no dropping cases with $33.3\%$ reduction in training time.

