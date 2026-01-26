---
layout: default
title: CASP: Few-Shot Class-Incremental Learning with CLS Token Attention Steering Prompts
---

# CASP: Few-Shot Class-Incremental Learning with CLS Token Attention Steering Prompts
**arXiv**：[2601.16773v1](https://arxiv.org/abs/2601.16773) · [PDF](https://arxiv.org/pdf/2601.16773.pdf)  
**作者**：Shuai Huang, Xuhan Lin, Yuwu Lu  

**一句话要点**：提出CASP方法，通过CLS令牌注意力引导提示解决少样本类增量学习中的灾难性遗忘问题。

**关键词**：少样本类增量学习, 注意力机制, 提示学习, 灾难性遗忘, 泛化增强

## 3 点简述
- 核心问题：少样本类增量学习需模型用极少样本快速适应新类，同时避免灾难性遗忘。
- 方法要点：引入类共享可训练偏置参数调制CLS令牌自注意力，结合注意力扰动和流形令牌混合增强泛化。
- 实验效果：在CUB200等数据集上优于现有方法，无需增量阶段微调且参数开销显著降低。

## 摘要（原文）

> Few-shot class-incremental learning (FSCIL) presents a core challenge in continual learning, requiring models to rapidly adapt to new classes with very limited samples while mitigating catastrophic forgetting. Recent prompt-based methods, which integrate pretrained backbones with task-specific prompts, have made notable progress. However, under extreme few-shot incremental settings, the model's ability to transfer and generalize becomes critical, and it is thus essential to leverage pretrained knowledge to learn feature representations that can be shared across future categories during the base session. Inspired by the mechanism of the CLS token, which is similar to human attention and progressively filters out task-irrelevant information, we propose the CLS Token Attention Steering Prompts (CASP). This approach introduces class-shared trainable bias parameters into the query, key, and value projections of the CLS token to explicitly modulate the self-attention weights. To further enhance generalization, we also design an attention perturbation strategy and perform Manifold Token Mixup in the shallow feature space, synthesizing potential new class features to improve generalization and reserve the representation capacity for upcoming tasks. Experiments on the CUB200, CIFAR100, and ImageNet-R datasets demonstrate that CASP outperforms state-of-the-art methods in both standard and fine-grained FSCIL settings without requiring fine-tuning during incremental phases and while significantly reducing the parameter overhead.

