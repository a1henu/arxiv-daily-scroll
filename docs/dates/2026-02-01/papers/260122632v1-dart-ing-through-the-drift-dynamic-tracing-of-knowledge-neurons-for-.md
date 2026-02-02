---
layout: default
title: DART-ing Through the Drift: Dynamic Tracing of Knowledge Neurons for Adaptive Inference-Time Pruning
---

# DART-ing Through the Drift: Dynamic Tracing of Knowledge Neurons for Adaptive Inference-Time Pruning
**arXiv**：[2601.22632v1](https://arxiv.org/abs/2601.22632) · [PDF](https://arxiv.org/pdf/2601.22632.pdf)  
**作者**：Abhishek Tyagi, Yunuo Cen, Shrey Dhorajiya, Bharadwaj Veeravalli, Xuanyao Fong  

**一句话要点**：提出DART方法，通过动态追踪注意力变化实现自适应推理时剪枝，以解决LLM参数冗余问题。

**关键词**：大语言模型剪枝, 动态推理优化, 注意力机制, 参数冗余, 自适应剪枝, 轻量级方法

## 3 点简述
- 核心问题：现有剪枝方法依赖数据集校准且为静态，无法适应自回归生成中知识神经元的动态变化。
- 方法要点：DART监控注意力分数分布变化，动态更新神经元级掩码，实现无训练、轻量级的上下文剪枝。
- 实验或效果：在十个基准测试中，DART在70%稀疏度下准确率提升达14.5%，内存占用小于10MB，FLOPs开销仅0.1%。

## 摘要（原文）

> Large Language Models (LLMs) exhibit substantial parameter redundancy, particularly in Feed-Forward Networks (FFNs). Existing pruning methods suffer from two primary limitations. First, reliance on dataset-specific calibration introduces significant data dependency and computational overhead. Second, being predominantly static, they fail to account for the evolving subset of knowledge neurons in LLMs during autoregressive generation as the context evolves. To address this, we introduce DART, i.e., Dynamic Attention-Guided Runtime Tracing), a lightweight, training-free method that performs on-the-fly context-based pruning. DART monitors shifts in attention score distributions to infer context changes, dynamically updating neuron-level masks to retain salient parameters. Across ten benchmarks, DART outperforms prior dynamic baseline, achieving accuracy gains of up to 14.5% on LLAMA-3.1-8B at 70% FFN sparsity. Furthermore, DART achieves up to 3x better ROUGE-L scores with respect to static-masked pruning on summarization tasks, with its performance comparable to the original dense models. We conclusively demonstrate that the proposed framework effectively adapts to diverse semantic contexts, preserves model capabilities across both general and domain-specific tasks while running at less than 10MBs of memory for LLAMA-3.1-8B(16GBs) with 0.1% FLOPs overhead. The code is available at https://github.com/seeder-research/DART.

