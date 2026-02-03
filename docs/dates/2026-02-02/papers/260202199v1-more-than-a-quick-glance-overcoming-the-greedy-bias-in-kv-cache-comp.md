---
layout: default
title: More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression
---

# More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression
**arXiv**：[2602.02199v1](https://arxiv.org/abs/2602.02199) · [PDF](https://arxiv.org/pdf/2602.02199.pdf)  
**作者**：Aryan Sood, Tanvi Sharma, Vansh Agrawal  

**一句话要点**：提出LASER-KV框架以解决KV缓存压缩中的贪婪偏差问题

**关键词**：KV缓存压缩, 长上下文处理, 注意力机制, 内存效率, 语义召回

## 3 点简述
- 核心问题：现有KV缓存压缩方法因线性内存增长受限，牺牲语义召回换取效率
- 方法要点：采用层累积选择与精确LSH召回，实施块累积策略以隔离压缩效应
- 实验或效果：在Babilong基准上，LASER-KV保持稳定性能，优于先前方法达10%

## 摘要（原文）

> While Large Language Models (LLMs) can theoretically support extensive context windows, their actual deployment is constrained by the linear growth of Key-Value (KV) cache memory. Prevailing compression strategies mitigate this through various pruning mechanisms, yet trade-off semantic recall for memory efficiency. In this work, we present LASER-KV (Layer Accumulated Selection with Exact-LSH Recall), a framework designed to test the limits of KV compression under a strict accumulative budgeting policy. We deviate from the standard fixed summary size approach by implementing a block-wise accumulation strategy governed by a protection divisor (n). This allows us to isolate the effects of compression from sliding window artifacts. Our experiments on the Babilong benchmark reveal performance degradation in previous compression methods by 15-30% on various long context tasks. LASER-KV maintains stable performance, achieving superior accuracies by a margin of upto 10% at 128k. These findings challenge the prevailing assumption that attention scores alone are a sufficient proxy for token utility.

