---
layout: default
title: CoMeT: Collaborative Memory Transformer for Efficient Long Context Modeling
---

# CoMeT: Collaborative Memory Transformer for Efficient Long Context Modeling
**arXiv**：[2602.01766v1](https://arxiv.org/abs/2602.01766) · [PDF](https://arxiv.org/pdf/2602.01766.pdf)  
**作者**：Runsong Zhao, Shilei Liu, Jiwei Tang, Langming Liu, Haibin Chen, Weidong Zhang, Yujin Yuan, Tong Xiao, Jingbo Zhu, Wenbo Su, Bo Zheng  

**一句话要点**：提出CoMeT以解决Transformer长上下文处理中的二次复杂度和KV缓存无限增长问题

**关键词**：长上下文建模, Transformer优化, 内存管理, 高效推理, 序列处理

## 3 点简述
- 标准Transformer的二次复杂度和无限增长的KV缓存阻碍长上下文处理
- CoMeT采用双内存系统和分块处理，实现恒定内存和线性时间
- 在1M token序列中准确检索，SCROLLS基准上性能媲美全注意力基线

## 摘要（原文）

> The quadratic complexity and indefinitely growing key-value (KV) cache of standard Transformers pose a major barrier to long-context processing. To overcome this, we introduce the Collaborative Memory Transformer (CoMeT), a novel architecture that enables LLMs to handle arbitrarily long sequences with constant memory usage and linear time complexity. Designed as an efficient, plug-in module, CoMeT can be integrated into pre-trained models with only minimal fine-tuning. It operates on sequential data chunks, using a dual-memory system to manage context: a temporary memory on a FIFO queue for recent events, and a global memory with a gated update rule for long-range dependencies. These memories then act as a dynamic soft prompt for the next chunk. To enable efficient fine-tuning on extremely long contexts, we introduce a novel layer-level pipeline parallelism strategy. The effectiveness of our approach is remarkable: a model equipped with CoMeT and fine-tuned on 32k contexts can accurately retrieve a passkey from any position within a 1M token sequence. On the SCROLLS benchmark, CoMeT surpasses other efficient methods and achieves performance comparable to a full-attention baseline on summarization tasks. Its practical effectiveness is further validated on real-world agent and user behavior QA tasks. The code is available at: https://anonymous.4open.science/r/comet-B00B/

