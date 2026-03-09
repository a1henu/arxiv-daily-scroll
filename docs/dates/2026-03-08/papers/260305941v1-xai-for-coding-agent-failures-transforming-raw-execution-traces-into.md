---
layout: default
title: XAI for Coding Agent Failures: Transforming Raw Execution Traces into Actionable Insights
---

# XAI for Coding Agent Failures: Transforming Raw Execution Traces into Actionable Insights
**arXiv**：[2603.05941v1](https://arxiv.org/abs/2603.05941) · [PDF](https://arxiv.org/pdf/2603.05941.pdf)  
**作者**：Arun Joshi  

**一句话要点**：提出系统化可解释AI方法，将原始执行轨迹转化为结构化解释以解决LLM编码代理失败调试难题

**关键词**：可解释AI, 编码代理, 执行轨迹分析, 失败分类法, 混合解释生成

## 3 点简述
- 核心问题：LLM编码代理失败难以理解，原始执行轨迹对开发者调试构成挑战
- 方法要点：基于领域特定失败分类法、自动标注系统和混合解释生成器构建结构化解释框架
- 实验或效果：用户研究显示，该方法使失败根因识别速度提升2.8倍，修复准确率提高73%

## 摘要（原文）

> Large Language Model (LLM)-based coding agents show promise in automating software development tasks, yet they frequently fail in ways that are difficult for developers to understand and debug. While general-purpose LLMs like GPT can provide ad-hoc explanations of failures, raw execution traces remain challenging to interpret even for experienced developers. We present a systematic explainable AI (XAI) approach that transforms raw agent execution traces into structured, human-interpretable explanations. Our method consists of three key components: (1) a domain-specific failure taxonomy derived from analyzing real agent failures, (2) an automatic annotation system that classifies failures using defined annotation schema, (3) a hybrid explanation generator that produces visual execution flows, natural language explanations, and actionable recommendations. Through a user study with 20 participants (10 technical, 10 non-technical), we demonstrate that our approach enables users to identify failure root causes 2.8 times faster and propose correct fixes with 73% higher accuracy compared to raw execution traces. Importantly, our structured approach outperforms ad-hoc state of the art models explanations by providing consistent, domain-specific insights with integrated visualizations. Our work establishes a framework for systematic agent failure analysis, addressing the critical need for interpretable AI systems in software development workflows

