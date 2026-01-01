---
layout: default
title: PrivacyBench: A Conversational Benchmark for Evaluating Privacy in Personalized AI
---

# PrivacyBench: A Conversational Benchmark for Evaluating Privacy in Personalized AI
**arXiv**：[2512.24848v1](https://arxiv.org/abs/2512.24848) · [PDF](https://arxiv.org/pdf/2512.24848.pdf)  
**作者**：Srija Mukhopadhyay, Sathwik Reddy, Shruthi Muthukumar, Jisun An, Ponnurangam Kumaraguru  

**一句话要点**：提出PrivacyBench基准以评估个性化AI中的隐私风险，通过多轮对话测试秘密泄露情况。

**关键词**：隐私评估基准, 个性化AI, 秘密泄露, 多轮对话测试, 检索增强生成

## 3 点简述
- 核心问题：个性化AI访问用户敏感数据时，缺乏社会上下文意识可能导致秘密泄露，威胁数字福祉。
- 方法要点：构建基于社会情境的数据集，嵌入秘密，并设计多轮对话评估来测量秘密保留能力。
- 实验或效果：测试RAG助手发现秘密泄露率高达26.56%，隐私提示降低至5.12%，但检索机制仍无差别访问敏感数据。

## 摘要（原文）

> Personalized AI agents rely on access to a user's digital footprint, which often includes sensitive data from private emails, chats and purchase histories. Yet this access creates a fundamental societal and privacy risk: systems lacking social-context awareness can unintentionally expose user secrets, threatening digital well-being. We introduce PrivacyBench, a benchmark with socially grounded datasets containing embedded secrets and a multi-turn conversational evaluation to measure secret preservation. Testing Retrieval-Augmented Generation (RAG) assistants reveals that they leak secrets in up to 26.56% of interactions. A privacy-aware prompt lowers leakage to 5.12%, yet this measure offers only partial mitigation. The retrieval mechanism continues to access sensitive data indiscriminately, which shifts the entire burden of privacy preservation onto the generator. This creates a single point of failure, rendering current architectures unsafe for wide-scale deployment. Our findings underscore the urgent need for structural, privacy-by-design safeguards to ensure an ethical and inclusive web for everyone.

