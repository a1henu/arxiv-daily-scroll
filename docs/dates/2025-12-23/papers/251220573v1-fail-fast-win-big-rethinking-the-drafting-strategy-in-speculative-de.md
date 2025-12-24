---
layout: default
title: Fail Fast, Win Big: Rethinking the Drafting Strategy in Speculative Decoding via Diffusion LLMs
---

# Fail Fast, Win Big: Rethinking the Drafting Strategy in Speculative Decoding via Diffusion LLMs
**arXiv**：[2512.20573v1](https://arxiv.org/abs/2512.20573) · [PDF](https://arxiv.org/pdf/2512.20573.pdf)  
**作者**：Rui Pan, Zhuofu Chen, Ravi Netravali  

**一句话要点**：提出FailFast框架，利用扩散大语言模型优化推测解码策略以加速自回归模型

**关键词**：推测解码, 扩散大语言模型, 自回归模型, 动态草稿长度, 无损加速

## 3 点简述
- 扩散大语言模型在推测解码中面临效率与质量权衡问题
- FailFast通过动态调整推测长度，在易推测区域延长草稿以降低验证延迟
- 实验显示，FailFast实现无损加速，最高达4.9倍速度提升

## 摘要（原文）

> Diffusion Large Language Models (dLLMs) offer fast, parallel token generation, but their standalone use is plagued by an inherent efficiency-quality tradeoff. We show that, if carefully applied, the attributes of dLLMs can actually be a strength for drafters in speculative decoding with autoregressive (AR) verifiers. Our core insight is that dLLM's speed from parallel decoding drastically lowers the risk of costly rejections, providing a practical mechanism to effectively realize the (elusive) lengthy drafts that lead to large speedups with speculative decoding. We present FailFast, a dLLM-based speculative decoding framework that realizes this approach by dynamically adapting its speculation length. It "fails fast" by spending minimal compute in hard-to-speculate regions to shrink speculation latency and "wins big" by aggressively extending draft lengths in easier regions to reduce verification latency (in many cases, speculating and accepting 70 tokens at a time!). Without any fine-tuning, FailFast delivers lossless acceleration of AR LLMs and achieves up to 4.9$\times$ speedup over vanilla decoding, 1.7$\times$ over the best naive dLLM drafter, and 1.4$\times$ over EAGLE-3 across diverse models and workloads. We open-source FailFast at https://github.com/ruipeterpan/failfast.

