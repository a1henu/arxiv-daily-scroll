---
layout: default
title: Long Context, Less Focus: A Scaling Gap in LLMs Revealed through Privacy and Personalization
---

# Long Context, Less Focus: A Scaling Gap in LLMs Revealed through Privacy and Personalization
**arXiv**：[2602.15028v1](https://arxiv.org/abs/2602.15028) · [PDF](https://arxiv.org/pdf/2602.15028.pdf)  
**作者**：Shangding Gu  

**一句话要点**：提出PAPerBench基准以揭示LLMs在隐私与个性化场景中的长上下文缩放差距

**关键词**：长上下文模型, 隐私保护, 个性化性能, 注意力机制, 基准评估

## 3 点简述
- 核心问题：长上下文如何影响LLMs的隐私泄露与个性化效果，当前研究不足
- 方法要点：构建大规模基准PAPerBench，包含29K实例和377K问题，覆盖1K至256K令牌
- 实验或效果：评估显示随上下文增长，性能下降，理论分析归因于注意力稀释

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed in privacy-critical and personalization-oriented scenarios, yet the role of context length in shaping privacy leakage and personalization effectiveness remains largely unexplored. We introduce a large-scale benchmark, PAPerBench, to systematically study how increasing context length influences both personalization quality and privacy protection in LLMs. The benchmark comprises approximately 29,000 instances with context lengths ranging from 1K to 256K tokens, yielding a total of 377K evaluation questions. It jointly evaluates personalization performance and privacy risks across diverse scenarios, enabling controlled analysis of long-context model behavior. Extensive evaluations across state-of-the-art LLMs reveal consistent performance degradation in both personalization and privacy as context length increases. We further provide a theoretical analysis of attention dilution under context scaling, explaining this behavior as an inherent limitation of soft attention in fixed-capacity Transformers. The empirical and theoretical findings together suggest a general scaling gap in current models -- long context, less focus. We release the benchmark to support reproducible evaluation and future research on scalable privacy and personalization. Code and data are available at https://github.com/SafeRL-Lab/PAPerBench

