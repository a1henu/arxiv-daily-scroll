---
layout: default
title: Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure
---

# Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure
**arXiv**：[2601.10566v1](https://arxiv.org/abs/2601.10566) · [PDF](https://arxiv.org/pdf/2601.10566.pdf)  
**作者**：Syed Naveed Mahmood, Md. Rezaur Rahman Bhuiyan, Tasfia Zaman, Jareen Tasneem Khondaker, Md. Sameer Sakib, Nazia Tasnim, Farig Sadeque  

**一句话要点**：提出基于激活签名的表示感知遗忘框架，以区分真实擦除与表面抑制，实现大语言模型的知识选择性擦除。

**关键词**：知识选择性擦除, 表示感知遗忘, 激活签名, 大语言模型, GDPR合规, 模型安全

## 3 点简述
- 核心问题：现有遗忘方法混淆行为抑制与真实知识移除，导致潜在能力残留，影响GDPR合规与模型安全。
- 方法要点：引入知识免疫框架，通过动态抑制主题特定表示和参数高效适配，针对内部激活签名而非表面输出实现表示感知遗忘。
- 实验或效果：在3B至14B参数模型上实现接近理想的擦除效果，保持实用性，突破稳定性与擦除的权衡，并揭示不同模型架构的遗忘行为差异。

## 摘要（原文）

> Selective knowledge erasure from LLMs is critical for GDPR compliance and model safety, yet current unlearning methods conflate behavioral suppression with true knowledge removal, allowing latent capabilities to persist beneath surface-level refusals. In this work, we address this challenge by introducing Knowledge Immunization Framework (KIF), a representation-aware architecture that distinguishes genuine erasure from obfuscation by targeting internal activation signatures rather than surface outputs. Our approach combines dynamic suppression of subject-specific representations with parameter-efficient adaptation, enabling durable unlearning without full model retraining. KIF achieves near-oracle erasure (FQ approx 0.99 vs. 1.00) while preserving utility at oracle levels (MU = 0.62), effectively breaking the stability-erasure tradeoff that has constrained all prior work. We evaluate both standard foundation models (Llama and Mistral) and reasoning-prior models (Qwen and DeepSeek) across 3B to 14B parameters. Our observation shows that standard models exhibit scale-independent true erasure (<3% utility drift), while reasoning-prior models reveal fundamental architectural divergence. Our comprehensive dual-metric evaluation protocol, combining surface-level leakage with latent trace persistence, operationalizes the obfuscation - erasure distinction and enables the first systematic diagnosis of mechanism-level forgetting behavior across model families and scales.

