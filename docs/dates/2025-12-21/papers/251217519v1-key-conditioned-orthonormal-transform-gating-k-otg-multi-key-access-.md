---
layout: default
title: Key-Conditioned Orthonormal Transform Gating (K-OTG): Multi-Key Access Control with Hidden-State Scrambling for LoRA-Tuned Models
---

# Key-Conditioned Orthonormal Transform Gating (K-OTG): Multi-Key Access Control with Hidden-State Scrambling for LoRA-Tuned Models
**arXiv**：[2512.17519v1](https://arxiv.org/abs/2512.17519) · [PDF](https://arxiv.org/pdf/2512.17519.pdf)  
**作者**：Muhammad Haris Khan  

**一句话要点**：提出K-OTG机制，通过隐藏状态正交变换实现LoRA微调模型的多密钥访问控制

**关键词**：访问控制, 正交变换, LoRA微调, 隐藏状态加扰, 密钥验证, 指令模型

## 3 点简述
- 核心问题：指令微调语言模型缺乏密钥访问控制，可能导致未授权使用
- 方法要点：基于双路径语料训练，在推理时通过正交变换和临时加扰器实现密钥验证与隐藏状态加扰
- 实验或效果：在1-3B规模模型上验证，授权使用保持接近基础性能，未授权使用性能崩溃，运行时开销为每秒令牌数减少40%

## 摘要（原文）

> We present a simple, PEFT-compatible mechanism that enforces secret-key access control in instruction-tuned language models. K-OTG trains on a dual-path corpus: authorized examples (prefixed with a role key) learn the task output, while unauthorized examples learn a visible block token. At inference, a pre-lm_head hook applies an orthonormal transform to the hidden state: with the correct key/role the inverse map restores the model's native basis; otherwise a session-ephemeral scrambler (permutation, sign flips, Householders) makes logits uninformative and the system short-circuits to BLOCK. Keys are not added as special tokens, and the method composes cleanly with LoRA on 4-bit bases. We evaluate an hour-scale protocol on 1-3B-class instruction models (Llama 3.2, Qwen2.5 1.5B) across utility (XSum ROUGE/BLEU, GSM8K accuracy, WikiText-2 perplexity), selectivity (3by3 role-key unlock matrices), nonce invariance, block suppression, and throughput. Authorized utility remains close to the base on summarization with the expected modest PPL increase from instruction tuning; unauthorized utility collapses (near-zero sequence metrics with exploding PPL), indicating practical unusability without the key. Unlock matrices are diagonally dominant (high on-target unlock, low cross-unlock), authorized block emission is 0 per N via robust bad-word lists, and greedy outputs match exactly across nonces, confirming correct inverse cancellation. The runtime overhead of the Python-level hook is 40% tokens per sec versus the base. K-OTG therefore provides a pragmatic, model-agnostic way to prevent unauthorized use while preserving authorized utility.

