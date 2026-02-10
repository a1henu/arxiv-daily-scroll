---
layout: default
title: LLMs + Security = Trouble
---

# LLMs + Security = Trouble
**arXiv**：[2602.08422v1](https://arxiv.org/abs/2602.08422) · [PDF](https://arxiv.org/pdf/2602.08422.pdf)  
**作者**：Benjamin Livshits  

**一句话要点**：提出在代码生成中强制安全约束以增强AI辅助开发的安全性

**关键词**：AI辅助开发, 安全约束, 代码生成, 长尾漏洞, 扩散模型

## 3 点简述
- 核心问题：现有AI安全方法无法处理长尾安全漏洞，导致系统易受零日攻击
- 方法要点：主张在代码生成阶段通过约束解码等方式强制安全约束，而非依赖事后检测修复
- 实验或效果：未知，但指出扩散式代码模型为模块化安全执行提供优雅机会

## 摘要（原文）

> We argue that when it comes to producing secure code with AI, the prevailing "fighting fire with fire" approach -- using probabilistic AI-based checkers or attackers to secure probabilistically generated code -- fails to address the long tail of security bugs. As a result, systems may remain exposed to zero-day vulnerabilities that can be discovered by better-resourced or more persistent adversaries.
>   While neurosymbolic approaches that combine LLMs with formal methods are attractive in principle, we argue that they are difficult to reconcile with the "vibe coding" workflow common in LLM-assisted development: unless the end-to-end verification pipeline is fully automated, developers are repeatedly asked to validate specifications, resolve ambiguities, and adjudicate failures, making the human-in-the-loop a likely point of weakness, compromising secure-by-construction guarantees.
>   In this paper we argue that stronger security guarantees can be obtained by enforcing security constraints during code generation (e.g., via constrained decoding), rather than relying solely on post-hoc detection and repair. This direction is particularly promising for diffusion-style code models, whose approach provides a natural elegant opportunity for modular, hierarchical security enforcement, allowing us to combine lower-latency generation techniques with generating secure-by-construction code.

