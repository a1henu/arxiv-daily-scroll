---
layout: default
title: CodeCompass: Navigating the Navigation Paradox in Agentic Code Intelligence
---

# CodeCompass: Navigating the Navigation Paradox in Agentic Code Intelligence
**arXiv**：[2602.20048v1](https://arxiv.org/abs/2602.20048) · [PDF](https://arxiv.org/pdf/2602.20048.pdf)  
**作者**：Tarakanath Paipuru  

**一句话要点**：提出CodeCompass以解决代码智能代理在导航与检索分离问题中的性能瓶颈

**关键词**：代码智能代理, 导航悖论, 图结构导航, 依赖图, 任务完成率, 行为对齐

## 3 点简述
- 核心问题：代码智能代理面临导航悖论，即导航与检索是根本不同问题，导致在百万令牌级上下文中无法发现关键文件。
- 方法要点：通过基于图的结构导航，利用CodeCompass暴露依赖图，改进代理在隐藏依赖任务中的表现。
- 实验或效果：在FastAPI仓库的30个基准任务中，图导航实现99.4%任务完成率，比基线代理提升23.2个百分点。

## 摘要（原文）

> Modern code intelligence agents operate in contexts exceeding 1 million tokens--far beyond the scale where humans manually locate relevant files. Yet agents consistently fail to discover architecturally critical files when solving real-world coding tasks. We identify the Navigation Paradox: agents perform poorly not due to context limits, but because navigation and retrieval are fundamentally distinct problems. Through 258 automated trials across 30 benchmark tasks on a production FastAPI repository, we demonstrate that graph-based structural navigation via CodeCompass--a Model Context Protocol server exposing dependency graphs--achieves 99.4% task completion on hidden-dependency tasks, a 23.2 percentage-point improvement over vanilla agents (76.2%) and 21.2 points over BM25 retrieval (78.2%).However, we uncover a critical adoption gap: 58% of trials with graph access made zero tool calls, and agents required explicit prompt engineering to adopt the tool consistently. Our findings reveal that the bottleneck is not tool availability but behavioral alignment--agents must be explicitly guided to leverage structural context over lexical heuristics. We contribute: (1) a task taxonomy distinguishing semantic-search, structural, and hidden-dependency scenarios; (2) empirical evidence that graph navigation outperforms retrieval when dependencies lack lexical overlap; and (3) open-source infrastructure for reproducible evaluation of navigation tools.

