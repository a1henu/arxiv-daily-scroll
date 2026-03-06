---
layout: default
title: Good-Enough LLM Obfuscation (GELO)
---

# Good-Enough LLM Obfuscation (GELO)
**arXiv**：[2603.05035v1](https://arxiv.org/abs/2603.05035) · [PDF](https://arxiv.org/pdf/2603.05035.pdf)  
**作者**：Anatoly Belikov, Ilya Fedotov  

**一句话要点**：提出GELO协议以保护共享加速器上开源LLM的提示隐私，通过每批次可逆混合隐藏状态。

**关键词**：大语言模型隐私, 可逆混合, 可信执行环境, 共享加速器安全, 盲源分离防御

## 3 点简述
- 核心问题：共享加速器中对手可观察KV缓存和隐藏状态，威胁开源LLM的提示隐私。
- 方法要点：使用TEE生成随机矩阵混合隐藏状态，每批次更新，防止多轮统计攻击。
- 实验或效果：在Llama-2 7B上保持输出精度，延迟开销约20-30%，抵御多种攻击。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly served on shared accelerators where an adversary with read access to device memory can observe KV caches and hidden states, threatening prompt privacy for open-source models. Cryptographic protections such as MPC and FHE offer strong guarantees but remain one to two orders of magnitude too slow for interactive inference, while static obfuscation schemes break under multi-run statistical attacks once the model is known. We present GELO (Good-Enough LLM Obfuscation), a lightweight protocol for privacy-preserving inference that limits information leakage from untrusted accelerator observations by hiding hidden states with fresh, per-batch invertible mixing. For each offloaded projection, the TEE samples a random matrix A, forms $U = AH$, offloads U and weights W to the accelerator, and then applies $A^-1$ on return, so that $A^-1 ((AH)W ) = HW$ and outputs are unchanged. Because mixing is never reused across batches, the attacker faces only a single-batch blind source separation problem. We analyze information leakage and introduce two practical defenses: (i) non-orthogonal mixing to mask Gram matrices, and (ii) orthogonal mixing augmented with a small fraction of high-energy "shield" vectors that pollute higher-order statistics. On Llama-2 7B, GELO preserves float32 outputs exactly, closely matches low-precision baselines, offloads the dominant matrix multiplications with about 20-30% latency overhead, and defeats a range of ICA/BSS and anchor-based attacks.

