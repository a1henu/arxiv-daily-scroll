---
layout: default
title: Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets
---

# Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets
**arXiv**：[2512.14237v1](https://arxiv.org/abs/2512.14237) · [PDF](https://arxiv.org/pdf/2512.14237.pdf)  
**作者**：Estelle Zheng, Nathan Cerisara, Sébastien Warichet, Emmanuel Helbert, Christophe Cerisara  

**一句话要点**：提出Ladder Side Tuning以解决大语言模型微调中的内存瓶颈问题

**关键词**：参数高效微调, 内存优化, 侧网络, 大语言模型, 微调效率

## 3 点简述
- 核心问题：大语言模型微调受限于消费级GPU内存，现有参数高效微调方法如QLoRA仍因反向传播导致高内存占用。
- 方法要点：采用轻量级侧网络Ladder Side Tuning，匹配QLoRA的计算扩展斜率，同时降低峰值内存50%。
- 实验或效果：在自然语言理解、数学和LLM批评任务中，LST性能与QLoRA相当，支持7B参数模型在12GB GPU上微调2k令牌上下文。

## 摘要（原文）

> Fine-tuning large language models (LLMs) is often limited by the memory available on commodity GPUs. Parameter-efficient fine-tuning (PEFT) methods such as QLoRA reduce the number of trainable parameters, yet still incur high memory usage induced by the backward pass in the full model. We revisit Ladder Side Tuning (LST), a rarely explored PEFT technique that adds a lightweight side network, and show that it matches QLoRA's compute scaling slope while cutting peak memory by 50\%. Across different downstream benchmarks spanning natural language understanding, mathematical and LLM-critic tasks, LST has competitive performance with QLoRA's accuracy on average while being much more memory-efficient. This efficiency enables fine-tuning of 7B-parameter models on a single 12 GB consumer GPU with 2k-token contexts, requiring no gradient checkpointing\textemdash conditions under which QLoRA exhausts memory. Beyond memory efficiency, we also establish scaling laws showing that LST scales similarly to QLoRA. We exploit Ladder's architectural flexibility by introducing xLadder, a depth-extended variant that increases effective depth via cross-connections and shortens chain-of-thought (CoT) at fixed parameter count. Ladder is strong when memory is the bottleneck; xLadder builds on this by enabling deeper reasoning without additional memory overhead.

