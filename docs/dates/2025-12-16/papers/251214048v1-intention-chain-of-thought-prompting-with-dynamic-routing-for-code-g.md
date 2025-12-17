---
layout: default
title: Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation
---

# Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation
**arXiv**：[2512.14048v1](https://arxiv.org/abs/2512.14048) · [PDF](https://arxiv.org/pdf/2512.14048.pdf)  
**作者**：Shen Li, Li Huang, Shaoxiong Zhan, Weifeng Sun, Tao Yin, Zhongxin Liu, Meng Yan  

**一句话要点**：提出RoutingGen框架，通过动态路由和意图链式思考提示解决代码生成中过度思考和意图抽象不足的问题。

**关键词**：代码生成, 链式思考提示, 动态路由, 意图抽象, 大语言模型, 算法设计

## 3 点简述
- 现有链式思考提示在代码生成中统一应用，导致简单任务过度思考和缺乏意图抽象。
- 引入RoutingGen框架，根据任务难度动态选择提示策略，简单任务用少样本提示，复杂任务用意图链式思考。
- 实验在三个模型和六个基准上显示，RoutingGen在多数设置中达到最优性能，平均减少46.37%的令牌使用。

## 摘要（原文）

> Large language models (LLMs) exhibit strong generative capabilities and have shown great potential in code generation. Existing chain-of-thought (CoT) prompting methods enhance model reasoning by eliciting intermediate steps, but suffer from two major limitations: First, their uniform application tends to induce overthinking on simple tasks. Second, they lack intention abstraction in code generation, such as explicitly modeling core algorithmic design and efficiency, leading models to focus on surface-level structures while neglecting the global problem objective. Inspired by the cognitive economy principle of engaging structured reasoning only when necessary to conserve cognitive resources, we propose RoutingGen, a novel difficulty-aware routing framework that dynamically adapts prompting strategies for code generation. For simple tasks, it adopts few-shot prompting; for more complex ones, it invokes a structured reasoning strategy, termed Intention Chain-of-Thought (ICoT), which we introduce to guide the model in capturing task intention, such as the core algorithmic logic and its time complexity. Experiments across three models and six standard code generation benchmarks show that RoutingGen achieves state-of-the-art performance in most settings, while reducing total token usage by 46.37% on average across settings. Furthermore, ICoT outperforms six existing prompting baselines on challenging benchmarks.

