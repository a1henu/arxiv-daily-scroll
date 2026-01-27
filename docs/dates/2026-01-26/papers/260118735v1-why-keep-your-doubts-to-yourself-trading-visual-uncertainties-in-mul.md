---
layout: default
title: Why Keep Your Doubts to Yourself? Trading Visual Uncertainties in Multi-Agent Bandit Systems
---

# Why Keep Your Doubts to Yourself? Trading Visual Uncertainties in Multi-Agent Bandit Systems
**arXiv**：[2601.18735v1](https://arxiv.org/abs/2601.18735) · [PDF](https://arxiv.org/pdf/2601.18735.pdf)  
**作者**：Jusheng Zhang, Yijia Fan, Kaitong Cai, Jing Yang, Jiawei Yao, Jian Wang, Guanlong Qu, Ziliang Chen, Keze Wang  

**一句话要点**：提出Agora框架，将多智能体协调重构为不确定性市场，以解决视觉语言模型扩展中的成本问题。

**关键词**：多智能体系统, 视觉语言模型, 不确定性交易, 市场协调, 成本效率, 多模态基准

## 3 点简述
- 核心问题：多智能体系统中信息不对称导致协调成本高昂，现有方法忽略成本且破坏不确定性结构。
- 方法要点：将认知不确定性形式化为可交易资产，基于经济规则驱动智能体间盈利性交易，引入市场感知代理引导系统。
- 实验或效果：在五个多模态基准测试中优于基线，如在MMMU上准确率提升8.5%且成本降低超3倍。

## 摘要（原文）

> Vision-Language Models (VLMs) enable powerful multi-agent systems, but scaling them is economically unsustainable: coordinating heterogeneous agents under information asymmetry often spirals costs. Existing paradigms, such as Mixture-of-Agents and knowledge-based routers, rely on heuristic proxies that ignore costs and collapse uncertainty structure, leading to provably suboptimal coordination. We introduce Agora, a framework that reframes coordination as a decentralized market for uncertainty. Agora formalizes epistemic uncertainty into a structured, tradable asset (perceptual, semantic, inferential), and enforces profitability-driven trading among agents based on rational economic rules. A market-aware broker, extending Thompson Sampling, initiates collaboration and guides the system toward cost-efficient equilibria. Experiments on five multimodal benchmarks (MMMU, MMBench, MathVision, InfoVQA, CC-OCR) show that Agora outperforms strong VLMs and heuristic multi-agent strategies, e.g., achieving +8.5% accuracy over the best baseline on MMMU while reducing cost by over 3x. These results establish market-based coordination as a principled and scalable paradigm for building economically viable multi-agent visual intelligence systems.

