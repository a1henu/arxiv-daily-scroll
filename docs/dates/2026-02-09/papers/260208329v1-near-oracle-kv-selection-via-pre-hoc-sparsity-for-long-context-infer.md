---
layout: default
title: Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference
---

# Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference
**arXiv**：[2602.08329v1](https://arxiv.org/abs/2602.08329) · [PDF](https://arxiv.org/pdf/2602.08329.pdf)  
**作者**：Yifei Gao, Lei Wang, Rong-Cheng Tu, Qixin Zhang, Jun Cheng, Dacheng Tao  

**一句话要点**：提出预稀疏方法以解决长上下文推理中KV缓存选择的后验偏差问题

**关键词**：KV缓存选择, 长上下文推理, 稀疏注意力, 互信息分析, 计算优化

## 3 点简述
- 核心问题：现有KV选择方法依赖后验启发式，导致偏差并损害长程推理
- 方法要点：通过边际-互信息分析推导损失上界，实现丢弃质量可控的预稀疏选择
- 实验效果：在多个基准上显著降低计算开销，保持或提升准确率

## 摘要（原文）

> A core bottleneck in large language model (LLM) inference is the cost of attending over the ever-growing key-value (KV) cache. Although near-oracle top-k KV selection can preserve the quality of dense attention while sharply reducing computation and bandwidth, existing sparse methods generally rely on posterior heuristics, i.e., selectors conditioned on observed attention or proxy scores. Such conditioning introduces posterior bias: it tends to distort true token importance and miss salient tokens, thereby impairing long-range reasoning. To tackle this problem, we propose Pre-hoc Sparsity (PrHS), which selects KV entries before attention scoring and provides explicit accuracy control. Let the attention mass of discarded entries be delta (the dropped mass). Through a marginal-to-mutual-information analysis, we derive an upper bound on the mutual-information loss that depends only on the dropped mass. This relation explains failure modes of posterior heuristics and enables verifiable guarantees by controlling the dropped mass in advance. Within PrHS, we instantiate three orthogonal pre-hoc selectors along the axes of time, depth, and layer. Extensive experiments on LLaMA and Mistral families validate PrHS. Across GSM8K and CoQA, PrHS reduces retrieval overhead by over 90%, achieving 3x higher retrieval sparsity than HShare at matched or better accuracy. It incurs under 1% average degradation on LongBench, lowers attention FLOPs by about 15% versus prior sparse baselines, and yields a 9.9x speedup in attention-operator latency and 2.8x higher throughput on NVIDIA A100-80GB GPUs than the dense baseline.

