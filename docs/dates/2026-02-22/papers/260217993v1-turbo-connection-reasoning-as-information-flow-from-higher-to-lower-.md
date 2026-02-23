---
layout: default
title: Turbo Connection: Reasoning as Information Flow from Higher to Lower Layers
---

# Turbo Connection: Reasoning as Information Flow from Higher to Lower Layers
**arXiv**：[2602.17993v1](https://arxiv.org/abs/2602.17993) · [PDF](https://arxiv.org/pdf/2602.17993.pdf)  
**作者**：Mohan Tang, Sidi Lu  

**一句话要点**：提出TurboConn架构，通过高层到低层的信息流增强Transformer推理能力

**关键词**：Transformer架构, 推理增强, 残差连接, 微调优化, 计算路径深度

## 3 点简述
- 核心问题：Transformer推理能力受限于固定计算路径深度
- 方法要点：引入密集反向连接，从高层隐藏状态路由到后续token的低层
- 实验或效果：在GSM8K等基准上提升0.9%至10%以上，Parity任务达100%准确率

## 摘要（原文）

> Complex problems, whether in math, logic, or planning, are solved by humans through a sequence of steps where the result of one step informs the next. In this work, we adopt the perspective that the reasoning power of Transformers is fundamentally limited by a fixed maximum number of steps along any latent path of computation. To address this, we introduce Turbo Connection (TurboConn), a novel architecture that overcomes the fixed-depth constraint by routing multiple residual connections from the higher-layer hidden states of each token $t$ to the lower layers of token $t+1$. Fine-tuning pre-trained LLMs with our method not only yields accuracy gains of 0.9% to over 10% on benchmarks like GSM8K, Parity, and multi-step arithmetic, but also demonstrates that the density of these backward connections is critical; our dense interaction significantly outperforms "sparse" alternatives that only pass a single hidden state or vector. Notably, TurboConn can be integrated into pre-trained LLMs to overcome task-specific plateaus: while a fine-tuned Qwen-3-1.7B achieves only 53.78% on Parity, adding our architectural modification enables the model to reach 100% accuracy, all without the necessity to retrain the full model from scratch or sophisticated curriculum learning. Our results provide strong empirical evidence that the depth of the computational path is a key factor in reasoning ability, also offering a new mechanism to enhance LLMs without significantly affecting generation latency.

