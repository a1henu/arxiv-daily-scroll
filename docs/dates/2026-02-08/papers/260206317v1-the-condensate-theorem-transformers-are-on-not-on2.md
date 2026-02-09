---
layout: default
title: The Condensate Theorem: Transformers are O(n), Not $O(n^2)$
---

# The Condensate Theorem: Transformers are O(n), Not $O(n^2)$
**arXiv**：[2602.06317v1](https://arxiv.org/abs/2602.06317) · [PDF](https://arxiv.org/pdf/2602.06317.pdf)  
**作者**：Jorge L. Ruiz Williams  

**一句话要点**：提出Condensate定理，证明Transformer注意力可无损压缩至线性复杂度，实现高速推理。

**关键词**：注意力稀疏性, Condensate定理, 线性复杂度, 无损压缩, 推理加速, 拓扑注意力

## 3 点简述
- 核心问题：传统Transformer注意力计算为O(n²)，导致推理效率瓶颈。
- 方法要点：通过Condensate流形（锚点+窗口+动态Top-k）动态投影注意力，实现无损输出等价。
- 实验或效果：在多个模型上验证比特精确匹配，硬件映射实现159倍加速，推理成本降低>99.9%。

## 摘要（原文）

> We present the Condensate Theorem: attention sparsity is a learned topological property, not an architectural constraint. Through empirical analysis of trained language models, we find that attention mass concentrates on a distinct topological manifold -- and this manifold can be identified dynamically without checking every position. We prove a general result: for any query, projecting attention onto the Condensate Manifold (Anchor + Window + Dynamic Top-k) achieves 100% output equivalence with full $O(n^2)$ attention. This is not an approximation -- it is lossless parity. We validate this across GPT-2, Pythia, Qwen2, TinyLlama, and Mistral, demonstrating bit-exact token matching on 1,500+ generated tokens. By mapping this topology to hardware, our Topological Attention kernel achieves a 159x measured speedup at 131K tokens (3.94ms vs 628ms) and a projected >1,200x speedup at 1M tokens, reducing inference costs by >99.9% compared to Flash Attention. We conclude that the quadratic bottleneck is an artifact of naive implementation, not intelligence.

