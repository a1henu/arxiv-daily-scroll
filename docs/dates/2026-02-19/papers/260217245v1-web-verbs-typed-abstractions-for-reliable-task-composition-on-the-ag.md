---
layout: default
title: Web Verbs: Typed Abstractions for Reliable Task Composition on the Agentic Web
---

# Web Verbs: Typed Abstractions for Reliable Task Composition on the Agentic Web
**arXiv**：[2602.17245v1](https://arxiv.org/abs/2602.17245) · [PDF](https://arxiv.org/pdf/2602.17245.pdf)  
**作者**：Linxi Jiang, Rui Xi, Zhijie Liu, Shuo Chen, Zhiqiang Lin, Suman Nath  

**一句话要点**：提出Web Verbs作为语义层，以提升网络代理任务组合的可靠性与效率。

**关键词**：网络代理, 语义层, 任务组合, 类型化接口, 可靠性验证

## 3 点简述
- 核心问题：当前网络代理依赖低级操作如点击，导致脆弱、低效且难以验证。
- 方法要点：引入类型化、语义文档化的Web Verbs，统一API与浏览器接口，支持可组合任务。
- 实验或效果：通过概念验证和案例研究，展示其能实现简洁、稳健的执行，优于现有代理。

## 摘要（原文）

> The Web is evolving from a medium that humans browse to an environment where software agents act on behalf of users. Advances in large language models (LLMs) make natural language a practical interface for goal-directed tasks, yet most current web agents operate on low-level primitives such as clicks and keystrokes. These operations are brittle, inefficient, and difficult to verify. Complementing content-oriented efforts such as NLWeb's semantic layer for retrieval, we argue that the agentic web also requires a semantic layer for web actions. We propose \textbf{Web Verbs}, a web-scale set of typed, semantically documented functions that expose site capabilities through a uniform interface, whether implemented through APIs or robust client-side workflows. These verbs serve as stable and composable units that agents can discover, select, and synthesize into concise programs. This abstraction unifies API-based and browser-based paradigms, enabling LLMs to synthesize reliable and auditable workflows with explicit control and data flow. Verbs can carry preconditions, postconditions, policy tags, and logging support, which improves \textbf{reliability} by providing stable interfaces, \textbf{efficiency} by reducing dozens of steps into a few function calls, and \textbf{verifiability} through typed contracts and checkable traces. We present our vision, a proof-of-concept implementation, and representative case studies that demonstrate concise and robust execution compared to existing agents. Finally, we outline a roadmap for standardization to make verbs deployable and trustworthy at web scale.

