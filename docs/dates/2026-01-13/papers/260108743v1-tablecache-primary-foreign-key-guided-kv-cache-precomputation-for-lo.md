---
layout: default
title: TableCache: Primary Foreign Key Guided KV Cache Precomputation for Low Latency Text-to-SQL
---

# TableCache: Primary Foreign Key Guided KV Cache Precomputation for Low Latency Text-to-SQL
**arXiv**：[2601.08743v1](https://arxiv.org/abs/2601.08743) · [PDF](https://arxiv.org/pdf/2601.08743.pdf)  
**作者**：Jinbo Su, Yuxuan Hu, Cuiping Li, Hong Chen, Jia Li, Lintao Ma, Jing Zhang  

**一句话要点**：提出TableCache以解决Text-to-SQL中KV缓存冗余导致的延迟问题

**关键词**：Text-to-SQL, KV缓存预计算, 主外键关系, Table Trie结构, 缓存管理, 低延迟推理

## 3 点简述
- 核心问题：现有LLM方法因包含完整数据库模式导致上下文长和预填充延迟高，且查询间KV缓存共享不足。
- 方法要点：离线预计算表表示作为KV缓存，基于主外键关系保持表间关联，并构建Table Trie结构支持高效在线查询。
- 实验或效果：实验显示TableCache在首次令牌时间上实现最高3.62倍加速，性能下降可忽略。

## 摘要（原文）

> In Text-to-SQL tasks, existing LLM-based methods often include extensive database schemas in prompts, leading to long context lengths and increased prefilling latency. While user queries typically focus on recurrent table sets-offering an opportunity for KV cache sharing across queries-current inference engines, such as SGLang and vLLM, generate redundant prefix cache copies when processing user queries with varying table orders. To address this inefficiency, we propose precomputing table representations as KV caches offline and querying the required ones online. A key aspect of our approach is the computation of table caches while preserving primary foreign key relationships between tables. Additionally, we construct a Table Trie structure to facilitate efficient KV cache lookups during inference. To enhance cache performance, we introduce a cache management system with a query reranking strategy to improve cache hit rates and a computation loading pipeline for parallelizing model inference and cache loading. Experimental results show that our proposed TableCache achieves up to a 3.62x speedup in Time to First Token (TTFT) with negligible performance degradation.

