---
layout: default
title: C-SWAP: Explainability-Aware Structured Pruning for Efficient Neural Networks Compression
---

# C-SWAP: Explainability-Aware Structured Pruning for Efficient Neural Networks Compression
**arXiv**：[2510.18636v1](https://arxiv.org/abs/2510.18636) · [PDF](https://arxiv.org/pdf/2510.18636.pdf)  
**作者**：Baptiste Bauvin, Loïc Baret, Ola Ahmad  

**一句话要点**：提出C-SWAP框架，利用可解释性实现高效神经网络压缩，解决一次性剪枝性能下降问题。

**关键词**：神经网络压缩, 结构化剪枝, 可解释深度学习, 一次性剪枝, 因果感知剪枝

## 3 点简述
- 核心问题：一次性结构化剪枝常导致模型性能显著下降，且传统方法需迭代重训练，计算成本高。
- 方法要点：基于因果关系的渐进剪枝，利用可解释深度学习识别并移除不影响预测的结构。
- 实验或效果：在CNN和ViT基准上验证，模型大小大幅减小，性能影响最小，无需微调。

## 摘要（原文）

> Neural network compression has gained increasing attention in recent years,
> particularly in computer vision applications, where the need for model
> reduction is crucial for overcoming deployment constraints. Pruning is a widely
> used technique that prompts sparsity in model structures, e.g. weights,
> neurons, and layers, reducing size and inference costs. Structured pruning is
> especially important as it allows for the removal of entire structures, which
> further accelerates inference time and reduces memory overhead. However, it can
> be computationally expensive, requiring iterative retraining and optimization.
> To overcome this problem, recent methods considered one-shot setting, which
> applies pruning directly at post-training. Unfortunately, they often lead to a
> considerable drop in performance. In this paper, we focus on this issue by
> proposing a novel one-shot pruning framework that relies on explainable deep
> learning. First, we introduce a causal-aware pruning approach that leverages
> cause-effect relations between model predictions and structures in a
> progressive pruning process. It allows us to efficiently reduce the size of the
> network, ensuring that the removed structures do not deter the performance of
> the model. Then, through experiments conducted on convolution neural network
> and vision transformer baselines, pre-trained on classification tasks, we
> demonstrate that our method consistently achieves substantial reductions in
> model size, with minimal impact on performance, and without the need for
> fine-tuning. Overall, our approach outperforms its counterparts, offering the
> best trade-off. Our code is available on GitHub.

