---
layout: default
title: Good-Enough LLM Obfuscation (GELO)
---

# Good-Enough LLM Obfuscation (GELO)
**arXiv**：[2603.05035v1](https://arxiv.org/abs/2603.05035) · [PDF](https://arxiv.org/pdf/2603.05035.pdf)  
**作者**：Anatoly Belikov, Ilya Fedotov  

**一句话要点**：提出GELO协议以保护共享加速器上开源LLM的提示隐私

**关键词**：大语言模型隐私, 可逆混合, 共享加速器安全, 信息泄露防御, 轻量级协议

## 3 点简述
- 问题：共享加速器上LLM的KV缓存和隐藏状态易被攻击者读取，威胁提示隐私。
- 方法：使用每批次新鲜可逆混合矩阵隐藏隐藏状态，限制单批次信息泄露。
- 效果：在Llama-2 7B上保持输出精度，延迟开销约20-30%，抵御多种攻击。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly served on shared accelerators where an adversary with read access to device memory can observe KV caches and hidden states, threatening prompt privacy for open-source models. Cryptographic protections such as MPC and FHE offer strong guarantees but remain one to two orders of magnitude too slow for interactive inference, while static obfuscation schemes break under multi-run statistical attacks once the model is known. We present GELO (Good-Enough LLM Obfuscation), a lightweight protocol for privacy-preserving inference that limits information leakage from untrusted accelerator observations by hiding hidden states with fresh, per-batch invertible mixing. For each offloaded projection, the TEE samples a random matrix A, forms $U = AH$, offloads U and weights W to the accelerator, and then applies $A^-1$ on return, so that $A^-1 ((AH)W ) = HW$ and outputs are unchanged. Because mixing is never reused across batches, the attacker faces only a single-batch blind source separation problem. We analyze information leakage and introduce two practical defenses: (i) non-orthogonal mixing to mask Gram matrices, and (ii) orthogonal mixing augmented with a small fraction of high-energy "shield" vectors that pollute higher-order statistics. On Llama-2 7B, GELO preserves float32 outputs exactly, closely matches low-precision baselines, offloads the dominant matrix multiplications with about 20-30% latency overhead, and defeats a range of ICA/BSS and anchor-based attacks.

