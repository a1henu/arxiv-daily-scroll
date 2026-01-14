---
layout: default
title: EfficientFSL: Enhancing Few-Shot Classification via Query-Only Tuning in Vision Transformers
---

# EfficientFSL: Enhancing Few-Shot Classification via Query-Only Tuning in Vision Transformers
**arXiv**：[2601.08499v1](https://arxiv.org/abs/2601.08499) · [PDF](https://arxiv.org/pdf/2601.08499.pdf)  
**作者**：Wenwen Liao, Hang Ruan  

**一句话要点**：提出EfficientFSL框架，通过仅查询微调在Vision Transformers中实现高效小样本分类

**关键词**：小样本分类, Vision Transformers, 查询微调, 轻量训练, 跨域适应

## 3 点简述
- 核心问题：Vision Transformers在小样本分类中性能优越，但微调计算成本高，不适合低资源场景。
- 方法要点：引入轻量可训练模块，仅通过查询方式从预训练模型中提取任务特定特征，减少可调参数。
- 实验或效果：在多个数据集上达到先进性能，显著降低计算开销，适用于实际应用。

## 摘要（原文）

> Large models such as Vision Transformers (ViTs) have demonstrated remarkable superiority over smaller architectures like ResNet in few-shot classification, owing to their powerful representational capacity. However, fine-tuning such large models demands extensive GPU memory and prolonged training time, making them impractical for many real-world low-resource scenarios. To bridge this gap, we propose EfficientFSL, a query-only fine-tuning framework tailored specifically for few-shot classification with ViT, which achieves competitive performance while significantly reducing computational overhead. EfficientFSL fully leverages the knowledge embedded in the pre-trained model and its strong comprehension ability, achieving high classification accuracy with an extremely small number of tunable parameters. Specifically, we introduce a lightweight trainable Forward Block to synthesize task-specific queries that extract informative features from the intermediate representations of the pre-trained model in a query-only manner. We further propose a Combine Block to fuse multi-layer outputs, enhancing the depth and robustness of feature representations. Finally, a Support-Query Attention Block mitigates distribution shift by adjusting prototypes to align with the query set distribution. With minimal trainable parameters, EfficientFSL achieves state-of-the-art performance on four in-domain few-shot datasets and six cross-domain datasets, demonstrating its effectiveness in real-world applications.

