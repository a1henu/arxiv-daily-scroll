---
layout: default
title: RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models
---

# RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models
**arXiv**：[2602.04448v1](https://arxiv.org/abs/2602.04448) · [PDF](https://arxiv.org/pdf/2602.04448.pdf)  
**作者**：Jiacheng Liang, Yuhui Wang, Tanqiu Jiang, Ting Wang  

**一句话要点**：提出RASA框架以解决MoE模型安全对齐中的路由感知专家修复问题

**关键词**：专家混合模型, 安全对齐, 路由感知, 专家修复, 越狱攻击, 微调优化

## 3 点简述
- MoE模型在标准全参数微调下，稀疏路由机制可能导致安全对齐失效，攻击成功率降低源于路由或专家主导效应而非安全关键专家修复。
- RASA通过识别被越狱攻击过度激活的专家，在固定路由下选择性微调这些专家，并强制路由与安全对齐上下文的一致性。
- 实验表明RASA在多种MoE架构和越狱攻击下实现近乎完美的鲁棒性、强跨攻击泛化能力，同时减少过度拒绝并保持通用能力。

## 摘要（原文）

> Mixture-of-Experts (MoE) language models introduce unique challenges for safety alignment due to their sparse routing mechanisms, which can enable degenerate optimization behaviors under standard full-parameter fine-tuning. In our preliminary experiments, we observe that naively applying full-parameter safety fine-tuning to MoE models can reduce attack success rates through routing or expert dominance effects, rather than by directly repairing Safety-Critical Experts. To address this challenge, we propose RASA, a routing-aware expert-level alignment framework that explicitly repairs Safety-Critical Experts while preventing routing-based bypasses. RASA identifies experts disproportionately activated by successful jailbreaks, selectively fine-tunes only these experts under fixed routing, and subsequently enforces routing consistency with safety-aligned contexts. Across two representative MoE architectures and a diverse set of jailbreak attacks, RASA achieves near-perfect robustness, strong cross-attack generalization, and substantially reduced over-refusal, while preserving general capabilities on benchmarks such as MMLU, GSM8K, and TruthfulQA. Our results suggest that robust MoE safety alignment benefits from targeted expert repair rather than global parameter updates, offering a practical and architecture-preserving alternative to prior approaches.

