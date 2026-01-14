---
layout: default
title: MPCI-Bench: A Benchmark for Multimodal Pairwise Contextual Integrity Evaluation of Language Model Agents
---

# MPCI-Bench: A Benchmark for Multimodal Pairwise Contextual Integrity Evaluation of Language Model Agents
**arXiv**：[2601.08235v1](https://arxiv.org/abs/2601.08235) · [PDF](https://arxiv.org/pdf/2601.08235.pdf)  
**作者**：Shouju Wang, Haopeng Zhang  

**一句话要点**：提出MPCI-Bench基准以评估多模态语言模型代理在隐私与效用权衡中的表现

**关键词**：多模态基准, 上下文完整性, 隐私评估, 语言模型代理, 模态泄露

## 3 点简述
- 核心问题：现有基准文本中心化，忽视多模态隐私风险和隐私与效用平衡
- 方法要点：构建首个多模态成对上下文完整性基准，包含种子判断、故事推理和代理行动三个层级
- 实验或效果：评估显示模型在隐私与效用平衡上系统性失败，视觉信息泄露更频繁

## 摘要（原文）

> As language-model agents evolve from passive chatbots into proactive assistants that handle personal data, evaluating their adherence to social norms becomes increasingly critical, often through the lens of Contextual Integrity (CI). However, existing CI benchmarks are largely text-centric and primarily emphasize negative refusal scenarios, overlooking multimodal privacy risks and the fundamental trade-off between privacy and utility. In this paper, we introduce MPCI-Bench, the first Multimodal Pairwise Contextual Integrity benchmark for evaluating privacy behavior in agentic settings. MPCI-Bench consists of paired positive and negative instances derived from the same visual source and instantiated across three tiers: normative Seed judgments, context-rich Story reasoning, and executable agent action Traces. Data quality is ensured through a Tri-Principle Iterative Refinement pipeline. Evaluations of state-of-the-art multimodal models reveal systematic failures to balance privacy and utility and a pronounced modality leakage gap, where sensitive visual information is leaked more frequently than textual information. We will open-source MPCI-Bench to facilitate future research on agentic CI.

