---
layout: default
title: Black-Box Behavioral Distillation Breaks Safety Alignment in Medical LLMs
---

# Black-Box Behavioral Distillation Breaks Safety Alignment in Medical LLMs
**arXiv**：[2512.09403v1](https://arxiv.org/abs/2512.09403) · [PDF](https://arxiv.org/pdf/2512.09403.pdf)  
**作者**：Sohely Jahan, Ruimin Sun  

**一句话要点**：提出黑盒行为蒸馏攻击，揭示医疗大语言模型安全对齐的脆弱性。

**关键词**：医疗大语言模型, 安全对齐, 黑盒蒸馏, 对抗攻击, 模型提取, 零对齐监督

## 3 点简述
- 核心问题：医疗大语言模型安全对齐在仅输出访问下易被攻击，导致功能保留但安全机制失效。
- 方法要点：通过指令查询和零对齐监督，低成本蒸馏LLaMA3 8B代理模型，无需模型权重或安全过滤器。
- 实验或效果：代理模型在86%对抗提示下产生不安全输出，远超原模型和基础模型，暴露功能-伦理差距。

## 摘要（原文）

> As medical large language models (LLMs) become increasingly integrated into clinical workflows, concerns around alignment robustness, and safety are escalating. Prior work on model extraction has focused on classification models or memorization leakage, leaving the vulnerability of safety-aligned generative medical LLMs underexplored.
>   We present a black-box distillation attack that replicates the domain-specific reasoning of safety-aligned medical LLMs using only output-level access. By issuing 48,000 instruction queries to Meditron-7B and collecting 25,000 benign instruction response pairs, we fine-tune a LLaMA3 8B surrogate via parameter efficient LoRA under a zero-alignment supervision setting, requiring no access to model weights, safety filters, or training data. With a cost of $12, the surrogate achieves strong fidelity on benign inputs while producing unsafe completions for 86% of adversarial prompts, far exceeding both Meditron-7B (66%) and the untuned base model (46%). This reveals a pronounced functional-ethical gap, task utility transfers, while alignment collapses. To analyze this collapse, we develop a dynamic adversarial evaluation framework combining Generative Query (GQ)-based harmful prompt generation, verifier filtering, category-wise failure analysis, and adaptive Random Search (RS) jailbreak attacks. We also propose a layered defense system, as a prototype detector for real-time alignment drift in black-box deployments.
>   Our findings show that benign-only black-box distillation exposes a practical and under-recognized threat: adversaries can cheaply replicate medical LLM capabilities while stripping safety mechanisms, underscoring the need for extraction-aware safety monitoring.

