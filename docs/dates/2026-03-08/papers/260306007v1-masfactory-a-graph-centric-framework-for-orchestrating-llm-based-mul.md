---
layout: default
title: MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing
---

# MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing
**arXiv**：[2603.06007v1](https://arxiv.org/abs/2603.06007) · [PDF](https://arxiv.org/pdf/2603.06007.pdf)  
**作者**：Yang Liu, Jinxuan Cai, Yishen Li, Qi Meng, Zedi Liu, Xin Li, Chen Qian, Chuan Shi, Cheng Yang  

**一句话要点**：提出MASFactory框架，基于Vibe Graphing编排LLM多智能体系统，解决工作流构建难题。

**关键词**：多智能体系统, 图工作流, 自然语言意图编译, 可重用组件, 上下文集成, 视觉化工具

## 3 点简述
- 核心问题：现有框架构建复杂图工作流需大量手动操作，复用性差，集成外部上下文困难。
- 方法要点：引入Vibe Graphing，将自然语言意图编译为可编辑工作流规范，支持可重用组件和可插拔上下文集成。
- 实验或效果：在七个公共基准上评估，验证了代表性方法的复现一致性和Vibe Graphing的有效性。

## 摘要（原文）

> Large language model-based (LLM-based) multi-agent systems (MAS) are increasingly used to extend agentic problem solving via role specialization and collaboration. MAS workflows can be naturally modeled as directed computation graphs, where nodes execute agents/sub-workflows and edges encode dependencies and message passing. However, implementing complex graph workflows in current frameworks still requires substantial manual effort, offers limited reuse, and makes it difficult to integrate heterogeneous external context sources. To overcome these limitations, we present MASFactory, a graph-centric framework for orchestrating LLM-based MAS. It introduces Vibe Graphing, a human-in-the-loop approach that compiles natural-language intent into an editable workflow specification and then into an executable graph. In addition, the framework provides reusable components and pluggable context integration, as well as a visualizer for topology preview, runtime tracing, and human-in-the-loop interaction. We evaluate MASFactory on seven public benchmarks, validating both reproduction consistency for representative MAS methods and the effectiveness of Vibe Graphing. Our code (https://github.com/BUPT-GAMMA/MASFactory) and video (https://youtu.be/ANynzVfY32k) are publicly available.

