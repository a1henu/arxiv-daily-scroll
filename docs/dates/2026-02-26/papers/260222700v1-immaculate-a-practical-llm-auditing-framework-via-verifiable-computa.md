---
layout: default
title: IMMACULATE: A Practical LLM Auditing Framework via Verifiable Computation
---

# IMMACULATE: A Practical LLM Auditing Framework via Verifiable Computation
**arXiv**：[2602.22700v1](https://arxiv.org/abs/2602.22700) · [PDF](https://arxiv.org/pdf/2602.22700.pdf)  
**作者**：Yanpei Guo, Wenjie Qu, Linyu Wu, Shengfang Zhai, Lionel Z. Wang, Ming Xu, Yue Liu, Binhang Yuan, Dawn Song, Jiaheng Zhang  

**一句话要点**：提出IMMACULATE框架，通过可验证计算审计商业大语言模型API的经济动机偏差。

**关键词**：大语言模型审计, 可验证计算, API安全, 经济动机偏差, 模型部署

## 3 点简述
- 核心问题：商业大语言模型作为黑盒API部署，用户需信任提供商正确执行推理和报告令牌使用，存在模型替换、量化滥用和令牌超计费等经济动机偏差风险。
- 方法要点：IMMACULATE框架基于可验证计算，选择性审计少量请求，无需可信硬件或模型内部访问，实现强检测保证并摊销密码学开销。
- 实验或效果：在密集和MoE模型上实验表明，IMMACULATE可靠区分良性和恶意执行，吞吐量开销低于1%。

## 摘要（原文）

> Commercial large language models are typically deployed as black-box API services, requiring users to trust providers to execute inference correctly and report token usage honestly. We present IMMACULATE, a practical auditing framework that detects economically motivated deviations-such as model substitution, quantization abuse, and token overbilling-without trusted hardware or access to model internals. IMMACULATE selectively audits a small fraction of requests using verifiable computation, achieving strong detection guarantees while amortizing cryptographic overhead. Experiments on dense and MoE models show that IMMACULATE reliably distinguishes benign and malicious executions with under 1% throughput overhead. Our code is published at https://github.com/guo-yanpei/Immaculate.

