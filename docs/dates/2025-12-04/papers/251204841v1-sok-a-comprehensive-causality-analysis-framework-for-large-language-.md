---
layout: default
title: SoK: a Comprehensive Causality Analysis Framework for Large Language Model Security
---

# SoK: a Comprehensive Causality Analysis Framework for Large Language Model Security
**arXiv**：[2512.04841v1](https://arxiv.org/abs/2512.04841) · [PDF](https://arxiv.org/pdf/2512.04841.pdf)  
**作者**：Wei Zhao, Zhe Li, Jun Sun  

**一句话要点**：提出统一因果分析框架以系统研究大语言模型安全漏洞

**关键词**：大语言模型安全, 因果分析框架, 越狱攻击, 模型可解释性, 安全检测

## 3 点简述
- 核心问题：大语言模型易受越狱等对抗攻击，需理解其因果因素以构建可靠防御。
- 方法要点：框架支持从令牌到表示层的多级因果干预，实现一致实验与比较。
- 实验或效果：在多个模型和基准上评估，揭示安全机制高度局部化，检测准确率超95%。

## 摘要（原文）

> Large Language Models (LLMs) exhibit remarkable capabilities but remain vulnerable to adversarial manipulations such as jailbreaking, where crafted prompts bypass safety mechanisms. Understanding the causal factors behind such vulnerabilities is essential for building reliable defenses.
>   In this work, we introduce a unified causality analysis framework that systematically supports all levels of causal investigation in LLMs, ranging from token-level, neuron-level, and layer-level interventions to representation-level analysis. The framework enables consistent experimentation and comparison across diverse causality-based attack and defense methods. Accompanying this implementation, we provide the first comprehensive survey of causality-driven jailbreak studies and empirically evaluate the framework on multiple open-weight models and safety-critical benchmarks including jailbreaks, hallucination detection, backdoor identification, and fairness evaluation. Our results reveal that: (1) targeted interventions on causally critical components can reliably modify safety behavior; (2) safety-related mechanisms are highly localized (i.e., concentrated in early-to-middle layers with only 1--2\% of neurons exhibiting causal influence); and (3) causal features extracted from our framework achieve over 95\% detection accuracy across multiple threat types.
>   By bridging theoretical causality analysis and practical model safety, our framework establishes a reproducible foundation for research on causality-based attacks, interpretability, and robust attack detection and mitigation in LLMs. Code is available at https://github.com/Amadeuszhao/SOK_Casuality.

