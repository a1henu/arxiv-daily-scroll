---
layout: default
title: Cross-Lingual Activation Steering for Multilingual Language Models
---

# Cross-Lingual Activation Steering for Multilingual Language Models
**arXiv**：[2601.16390v1](https://arxiv.org/abs/2601.16390) · [PDF](https://arxiv.org/pdf/2601.16390.pdf)  
**作者**：Rhitabrat Pokharel, Ameeta Agrawal, Tanay Nagar  

**一句话要点**：提出跨语言激活引导（CLAS），通过选择性调制神经元激活来提升多语言模型在非主导语言上的性能。

**关键词**：多语言模型, 激活引导, 推理时干预, 神经元调制, 跨语言性能提升

## 3 点简述
- 核心问题：多语言模型中主导与非主导语言间存在性能差距，归因于共享与语言特定神经元的不平衡。
- 方法要点：CLAS是一种无需训练的推理时干预，通过选择性调制神经元激活来引导模型行为。
- 实验或效果：在分类和生成基准测试中，平均提升2.3%（准确率）和3.4%（F1），同时保持高资源语言性能。

## 摘要（原文）

> Large language models exhibit strong multilingual capabilities, yet significant performance gaps persist between dominant and non-dominant languages. Prior work attributes this gap to imbalances between shared and language-specific neurons in multilingual representations. We propose Cross-Lingual Activation Steering (CLAS), a training-free inference-time intervention that selectively modulates neuron activations. We evaluate CLAS on classification and generation benchmarks, achieving average improvements of 2.3% (Acc.) and 3.4% (F1) respectively, while maintaining high-resource language performance. We discover that effective transfer operates through functional divergence rather than strict alignment; performance gains correlate with increased language cluster separation. Our results demonstrate that targeted activation steering can unlock latent multilingual capacity in existing models without modification to model weights.

