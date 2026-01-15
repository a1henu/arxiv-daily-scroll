---
layout: default
title: Adaptive Multi-Stage Patent Claim Generation with Unified Quality Assessment
---

# Adaptive Multi-Stage Patent Claim Generation with Unified Quality Assessment
**arXiv**：[2601.09120v1](https://arxiv.org/abs/2601.09120) · [PDF](https://arxiv.org/pdf/2601.09120.pdf)  
**作者**：Chen-Wei Liang, Bin Guo, Zhen-Yuan Wei, Mu-Jiang-Shan Wang  

**一句话要点**：提出自适应多阶段专利权利要求生成框架，通过关系建模、领域适应和统一评估解决跨司法管辖区泛化、语义关系建模和质量评估问题。

**关键词**：专利权利要求生成, 跨司法管辖区泛化, 语义关系建模, 统一质量评估, 多头注意力, 动态LoRA适配器

## 3 点简述
- 核心问题：现有系统存在跨司法管辖区泛化差、权利要求与现有技术语义关系建模不足、质量评估不可靠。
- 方法要点：采用三阶段框架，包括关系感知相似性分析、领域自适应权利要求生成和统一质量评估，使用多头注意力和动态LoRA适配器。
- 实验或效果：在USPTO HUPD等数据集上，相比基线模型，ROUGE-L提升7.6点，跨司法管辖区性能保持率达89.4%。

## 摘要（原文）

> Current patent claim generation systems face three fundamental limitations: poor cross-jurisdictional generalization, inadequate semantic relationship modeling between claims and prior art, and unreliable quality assessment. We introduce a novel three-stage framework that addresses these challenges through relationship-aware similarity analysis, domain-adaptive claim generation, and unified quality assessment. Our approach employs multi-head attention with eight specialized heads for explicit relationship modeling, integrates curriculum learning with dynamic LoRA adapter selection across five patent domains, and implements cross-attention mechanisms between evaluation aspects for comprehensive quality assessment. Extensive experiments on USPTO HUPD dataset, EPO patent collections, and Patent-CE benchmark demonstrate substantial improvements: 7.6-point ROUGE-L gain over GPT-4o, 8.3\% BERTScore enhancement over Llama-3.1-8B, and 0.847 correlation with human experts compared to 0.623 for separate evaluation models. Our method maintains 89.4\% cross-jurisdictional performance retention versus 76.2\% for baselines, establishing a comprehensive solution for automated patent prosecution workflows.

