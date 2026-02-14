---
layout: default
title: AdaptEvolve: Improving Efficiency of Evolutionary AI Agents through Adaptive Model Selection
---

# AdaptEvolve: Improving Efficiency of Evolutionary AI Agents through Adaptive Model Selection
**arXiv**：[2602.11931v1](https://arxiv.org/abs/2602.11931) · [PDF](https://arxiv.org/pdf/2602.11931.pdf)  
**作者**：Pretam Ray, Pratik Prabhanjan Brahma, Zicheng Liu, Emad Barsoum  

**一句话要点**：提出AdaptEvolve方法，通过自适应模型选择提升进化AI代理的效率

**关键词**：进化代理系统, 自适应模型选择, 大语言模型, 计算效率优化, 置信度驱动路由

## 3 点简述
- 核心问题：进化代理系统在推理中反复调用大语言模型，需平衡计算效率与推理能力
- 方法要点：基于生成置信度动态选择LLM，估计实时可解性以优化模型选择
- 实验或效果：平均减少37.9%推理成本，保持97.5%静态大模型基准的准确率

## 摘要（原文）

> Evolutionary agentic systems intensify the trade-off between computational efficiency and reasoning capability by repeatedly invoking large language models (LLMs) during inference. This setting raises a central question: how can an agent dynamically select an LLM that is sufficiently capable for the current generation step while remaining computationally efficient? While model cascades offer a practical mechanism for balancing this trade-off, existing routing strategies typically rely on static heuristics or external controllers and do not explicitly account for model uncertainty. We introduce AdaptEvolve: Adaptive LLM Selection for Multi-LLM Evolutionary Refinement within an evolutionary sequential refinement framework that leverages intrinsic generation confidence to estimate real-time solvability. Empirical results show that confidence-driven selection yields a favourable Pareto frontier, reducing total inference cost by an average of 37.9% across benchmarks while retaining 97.5% of the upper-bound accuracy of static large-model baselines. Our code is available at https://github.com/raypretam/adaptive_llm_selection.

