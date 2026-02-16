---
layout: default
title: Asynchronous Verified Semantic Caching for Tiered LLM Architectures
---

# Asynchronous Verified Semantic Caching for Tiered LLM Architectures
**arXiv**：[2602.13165v1](https://arxiv.org/abs/2602.13165) · [PDF](https://arxiv.org/pdf/2602.13165.pdf)  
**作者**：Asmit Kumar Singh, Haozhe Wang, Laxmi Naga Santosh Attaluri, Tak Chiam, Weihua Zhu  

**一句话要点**：提出异步验证语义缓存Krites，以扩展分层LLM架构中静态缓存的覆盖范围。

**关键词**：语义缓存, 分层LLM架构, 异步验证, LLM法官, 缓存策略, 推理优化

## 3 点简述
- 核心问题：分层LLM架构中，单一嵌入相似度阈值导致静态缓存覆盖与语义准确性之间的硬权衡。
- 方法要点：在关键路径保持标准静态阈值策略，异步调用LLM法官验证低于阈值的静态响应，批准后提升至动态缓存。
- 实验或效果：在对话和搜索工作负载的模拟中，Krites将使用静态答案的请求比例提升至基线3.9倍，关键路径延迟不变。

## 摘要（原文）

> Large language models (LLMs) now sit in the critical path of search, assistance, and agentic workflows, making semantic caching essential for reducing inference cost and latency. Production deployments typically use a tiered static-dynamic design: a static cache of curated, offline vetted responses mined from logs, backed by a dynamic cache populated online. In practice, both tiers are commonly governed by a single embedding similarity threshold, which induces a hard tradeoff: conservative thresholds miss safe reuse opportunities, while aggressive thresholds risk serving semantically incorrect responses. We introduce \textbf{Krites}, an asynchronous, LLM-judged caching policy that expands static coverage without changing serving decisions. On the critical path, Krites behaves exactly like a standard static threshold policy. When the nearest static neighbor of the prompt falls just below the static threshold, Krites asynchronously invokes an LLM judge to verify whether the static response is acceptable for the new prompt. Approved matches are promoted into the dynamic cache, allowing future repeats and paraphrases to reuse curated static answers and expanding static reach over time. In trace-driven simulations on conversational and search workloads, Krites increases the fraction of requests served with curated static answers (direct static hits plus verified promotions) by up to $\textbf{3.9}$ times for conversational traffic and search-style queries relative to tuned baselines, with unchanged critical path latency.

