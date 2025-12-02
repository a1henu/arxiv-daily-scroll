---
layout: default
title: KV Pareto: Systems-Level Optimization of KV Cache and Model Compression for Long Context Inference
---

# KV Pareto: Systems-Level Optimization of KV Cache and Model Compression for Long Context Inference
**arXiv**：[2512.01953v1](https://arxiv.org/abs/2512.01953) · [PDF](https://arxiv.org/pdf/2512.01953.pdf)  
**作者**：Sai Gokhale, Devleena Das, Rajeev Patwari, Ashish Sirasao, Elliott Delaye  

**一句话要点**：提出KV Pareto框架，通过联合优化KV缓存和模型压缩以解决长上下文LLM推理中的内存瓶颈问题。

**关键词**：长上下文推理, KV缓存优化, 模型压缩, 帕累托前沿, 边缘部署, 内存效率

## 3 点简述
- 核心问题：长上下文LLM推理中KV缓存线性增长导致内存瓶颈，现有技术联合优化不足。
- 方法要点：系统评估KV量化、分块预填充和权重量化，构建内存与精度的帕累托前沿。
- 实验或效果：在多个模型上实现68-78%内存减少，精度损失仅1-3%，验证于长上下文任务和基准测试。

## 摘要（原文）

> Long-context Large Language Models (LLMs) face significant memory bottlenecks during inference due to the linear growth of key-value (KV) cache with sequence length. While individual optimization techniques like KV cache quantization, chunked prefill, and model weight quantization have shown promise, their joint effects and optimal configurations for edge deployment remain underexplored. We introduce KV Pareto, a systems-level framework that systematically maps the trade-off frontier between total memory consumption and task accuracy across these three complementary optimization techniques. Our framework evaluates multiple LLM architectures (Qwen, Llama, Mistral) with varying KV quantization schemes (int2/4/8, mixed-precision), granularities (per-token, per-tensor, per-block), and 4-bit weight quantization via AWQ. Our framework identifies model-specific Pareto-optimal configurations that achieve 68-78% total memory reduction with minimal (1-3%) accuracy degradation on long-context tasks. We additionally verify the selected frontiers on additional benchmarks of Needle-in-a-Haystack, GSM8k and MMLU as well as extended context lengths of up to 128k to demonstrate the practical need of joint optimization for efficient LLM inference.

