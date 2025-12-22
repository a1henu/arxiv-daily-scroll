---
layout: default
title: Learning What to Write: Write-Gated KV for Efficient Long-Context Inference
---

# Learning What to Write: Write-Gated KV for Efficient Long-Context Inference
**arXiv**：[2512.17452v1](https://arxiv.org/abs/2512.17452) · [PDF](https://arxiv.org/pdf/2512.17452.pdf)  
**作者**：Yen-Chieh Huang, Rui Fang, Ming-Syan Chen, Pi-Cheng Hsiu  

**一句话要点**：提出Write-Gated KV机制，通过预测令牌效用优化KV缓存管理，以提升长上下文LLM推理效率。

**关键词**：KV缓存管理, 长上下文推理, 注意力优化, 轻量机制, 效率提升

## 3 点简述
- 核心问题：长上下文LLM推理因注意力复杂度二次方和KV缓存线性增长而效率低下，现有方法忽视写入低效性。
- 方法要点：将KV缓存管理形式化为因果系统，引入Write-Gated KV轻量机制，早期过滤低效用令牌，结合全局和局部缓存。
- 实验或效果：在Llama模型上，内存使用减少46-57%，预填充和解码速度分别提升3.03-3.45倍和1.89-2.56倍，精度损失可忽略。

## 摘要（原文）

> Long-context LLM inference is bottlenecked by the quadratic attention complexity and linear KV cache growth. Prior approaches mitigate this via post-hoc selection or eviction but overlook the root inefficiency: indiscriminate writing to persistent memory. In this paper, we formalize KV cache management as a causal system of three primitives: KV Admission, Selection, and Eviction. We instantiate KV Admission via Write-Gated KV, a lightweight mechanism that learns to predict token utility before it enters the cache. By filtering out low-utility states early to maintain a compact global cache alongside a sliding local cache, Write-Gated KV reduces memory usage by 46-57% and delivers 3.03-3.45$\times$ prefill and 1.89-2.56$\times$ decode speedups on Llama model with negligible accuracy loss, all while remaining compatible with FlashAttention and paged-KV systems. These results demonstrate that learning what to write, is a principled and practical recipe for efficient long-context inference. Code is available at https://github.com/EMCLab-Sinica/WG-KV .

