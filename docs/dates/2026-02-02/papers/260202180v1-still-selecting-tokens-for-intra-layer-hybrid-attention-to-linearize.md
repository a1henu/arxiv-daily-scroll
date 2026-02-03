---
layout: default
title: STILL: Selecting Tokens for Intra-Layer Hybrid Attention to Linearize LLMs
---

# STILL: Selecting Tokens for Intra-Layer Hybrid Attention to Linearize LLMs
**arXiv**：[2602.02180v1](https://arxiv.org/abs/2602.02180) · [PDF](https://arxiv.org/pdf/2602.02180.pdf)  
**作者**：Weikang Meng, Liangyu Huo, Yadan Luo, Jiawen Guan, Jingyi Zhang, Yingjian Li, Zheng Zhang  

**一句话要点**：提出STILL框架以线性化大语言模型，通过自显著分和规范保持特征图提升效率与性能。

**关键词**：大语言模型线性化, 混合注意力机制, 令牌选择策略, 特征图设计, 长上下文处理

## 3 点简述
- 核心问题：现有线性化方法基于滑动窗口选择令牌，忽略全局重要性，且特征图导致分布偏移。
- 方法要点：引入自显著分实现局部-全局一致性令牌选择，设计规范保持特征图保留预训练表示。
- 实验或效果：在常识和推理任务上匹配或超越原模型，长上下文基准上相对改进达86.2%。

## 摘要（原文）

> Linearizing pretrained large language models (LLMs) primarily relies on intra-layer hybrid attention mechanisms to alleviate the quadratic complexity of standard softmax attention. Existing methods perform token routing based on sliding-window partitions, resulting in position-based selection and fails to capture token-specific global importance. Meanwhile, linear attention further suffers from distribution shift caused by learnable feature maps that distort pretrained feature magnitudes. Motivated by these limitations, we propose STILL, an intra-layer hybrid linearization framework for efficiently linearizing LLMs. STILL introduces a Self-Saliency Score with strong local-global consistency, enabling accurate token selection using sliding-window computation, and retains salient tokens for sparse softmax attention while summarizing the remaining context via linear attention. To preserve pretrained representations, we design a Norm-Preserved Feature Map (NP-Map) that decouples feature direction from magnitude and reinjects pretrained norms. We further adopt a unified training-inference architecture with chunk-wise parallelization and delayed selection to improve hardware efficiency. Experiments show that STILL matches or surpasses the original pretrained model on commonsense and general reasoning tasks, and achieves up to a 86.2% relative improvement over prior linearized attention methods on long-context benchmarks.

