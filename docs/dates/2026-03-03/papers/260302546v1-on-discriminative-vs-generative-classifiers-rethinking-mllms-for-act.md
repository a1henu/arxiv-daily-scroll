---
layout: default
title: On Discriminative vs. Generative classifiers: Rethinking MLLMs for Action Understanding
---

# On Discriminative vs. Generative classifiers: Rethinking MLLMs for Action Understanding
**arXiv**：[2603.02546v1](https://arxiv.org/abs/2603.02546) · [PDF](https://arxiv.org/pdf/2603.02546.pdf)  
**作者**：Zhanzhong Pang, Dibyadip Chatterjee, Fadime Sener, Angela Yao  

**一句话要点**：提出生成辅助判别分类器以提升闭集动作理解性能与效率

**关键词**：闭集动作理解, 多模态大语言模型, 生成辅助判别分类器, 动作识别, 高效推理, 语义歧义

## 3 点简述
- 核心问题：MLLMs作为生成分类器在闭集动作理解中效率低且标签语义重叠导致歧义
- 方法要点：设计策略提升生成分类器性能，并融合生成与判别优势提出GAD分类器
- 实验或效果：在多个数据集上实现SOTA，平均准确率提升2.5%，推理速度加快3倍

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have advanced open-world action understanding and can be adapted as generative classifiers for closed-set settings by autoregressively generating action labels as text. However, this approach is inefficient, and shared subwords across action labels introduce semantic overlap, leading to ambiguity in generation. In contrast, discriminative classifiers learn task-specific representations with clear decision boundaries, enabling efficient one-step classification without autoregressive decoding. We first compare generative and discriminative classifiers with MLLMs for closed-set action understanding, revealing the superior accuracy and efficiency of the latter. To bridge the performance gap, we design strategies that elevate generative classifiers toward performance comparable with discriminative ones. Furthermore, we show that generative modeling can complement discriminative classifiers, leading to better performance while preserving efficiency. To this end, we propose Generation-Assisted Discriminative~(GAD) classifier for closed-set action understanding. GAD operates only during fine-tuning, preserving full compatibility with MLLM pretraining. Extensive experiments on temporal action understanding benchmarks demonstrate that GAD improves both accuracy and efficiency over generative methods, achieving state-of-the-art results on four tasks across five datasets, including an average 2.5% accuracy gain and 3x faster inference on our largest COIN benchmark.

