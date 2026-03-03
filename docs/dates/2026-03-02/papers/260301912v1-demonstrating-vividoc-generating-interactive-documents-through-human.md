---
layout: default
title: Demonstrating ViviDoc: Generating Interactive Documents through Human-Agent Collaboration
---

# Demonstrating ViviDoc: Generating Interactive Documents through Human-Agent Collaboration
**arXiv**：[2603.01912v1](https://arxiv.org/abs/2603.01912) · [PDF](https://arxiv.org/pdf/2603.01912.pdf)  
**作者**：Yinghao Tang, Yupeng Xie, Yingchaojie Feng, Tingfeng Lan, Wei Chen  

**一句话要点**：提出ViviDoc系统，通过人机协作从单一主题生成交互式教育文档。

**关键词**：交互式文档生成, 人机协作, 多代理系统, 文档规范, 教育技术, LLM应用

## 3 点简述
- 核心问题：创建交互式文章成本高，需领域知识和开发技能，现有LLM代理生成不可控且不可验证。
- 方法要点：引入多代理管道和文档规范，将交互可视化分解为状态、渲染、转换和约束组件，支持人工审核。
- 实验或效果：专家评估和用户研究表明，ViviDoc显著优于简单代理生成，提供直观编辑体验。

## 摘要（原文）

> Interactive articles help readers engage with complex ideas through exploration, yet creating them remains costly, requiring both domain expertise and web development skills. Recent LLM-based agents can automate content creation, but naively applying them yields uncontrollable and unverifiable outputs. We present ViviDoc, a human-agent collaborative system that generates interactive educational documents from a single topic input. ViviDoc introduces a multi-agent pipeline (Planner, Executor, Evaluator) and the Document Specification (DocSpec), a human-readable intermediate representation that decomposes each interactive visualization into State, Render, Transition, and Constraint components. The DocSpec enables educators to review and refine generation plans before code is produced, bridging the gap between pedagogical intent and executable output. Expert evaluation and a user study show that ViviDoc substantially outperforms naive agentic generation and provides an intuitive editing experience. Our project homepage is available at https://vividoc-homepage.vercel.app/.

