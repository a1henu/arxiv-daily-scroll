---
layout: default
title: V-Retrver: Evidence-Driven Agentic Reasoning for Universal Multimodal Retrieval
---

# V-Retrver: Evidence-Driven Agentic Reasoning for Universal Multimodal Retrieval
**arXiv**：[2602.06034v1](https://arxiv.org/abs/2602.06034) · [PDF](https://arxiv.org/pdf/2602.06034.pdf)  
**作者**：Dongyang Chen, Chaoyang Wang, Dezhao SU, Xi Xiao, Zeyu Zhang, Jing Xiong, Qing Li, Yuzhang Shang, Shichao Ka  

**一句话要点**：提出V-Retrver框架，通过证据驱动的代理推理解决多模态检索中的视觉模糊问题。

**关键词**：多模态检索, 代理推理, 视觉证据验证, 课程学习, 强化学习

## 3 点简述
- 现有方法依赖静态视觉编码，缺乏主动验证细粒度视觉证据的能力，导致推理易受视觉模糊影响。
- V-Retrver将多模态检索重构为基于视觉检查的代理推理过程，允许MLLM通过外部工具选择性获取证据，实现假设生成与视觉验证交替的推理。
- 采用课程学习策略训练，结合监督激活、拒绝细化和强化学习，在多个基准上平均提升检索准确率23.0%，增强推理可靠性和泛化能力。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have recently been applied to universal multimodal retrieval, where Chain-of-Thought (CoT) reasoning improves candidate reranking. However, existing approaches remain largely language-driven, relying on static visual encodings and lacking the ability to actively verify fine-grained visual evidence, which often leads to speculative reasoning in visually ambiguous cases. We propose V-Retrver, an evidence-driven retrieval framework that reformulates multimodal retrieval as an agentic reasoning process grounded in visual inspection. V-Retrver enables an MLLM to selectively acquire visual evidence during reasoning via external visual tools, performing a multimodal interleaved reasoning process that alternates between hypothesis generation and targeted visual verification.To train such an evidence-gathering retrieval agent, we adopt a curriculum-based learning strategy combining supervised reasoning activation, rejection-based refinement, and reinforcement learning with an evidence-aligned objective. Experiments across multiple multimodal retrieval benchmarks demonstrate consistent improvements in retrieval accuracy (with 23.0% improvements on average), perception-driven reasoning reliability, and generalization.

