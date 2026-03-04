---
layout: default
title: From Heuristic Selection to Automated Algorithm Design: LLMs Benefit from Strong Priors
---

# From Heuristic Selection to Automated Algorithm Design: LLMs Benefit from Strong Priors
**arXiv**：[2603.02792v1](https://arxiv.org/abs/2603.02792) · [PDF](https://arxiv.org/pdf/2603.02792.pdf)  
**作者**：Qi Huang, Furong Ye, Ananta Shahane, Thomas Bäck, Niki van Stein  

**一句话要点**：提出利用先验基准算法指导LLM驱动优化，提升黑盒优化性能

**关键词**：大语言模型, 自动化算法设计, 黑盒优化, 基准算法, 提示工程, 代码生成

## 3 点简述
- 核心问题：现有LLM驱动算法设计依赖自适应提示，缺乏高效引导机制
- 方法要点：通过分析提示对生成代码的贡献，引入高质量算法示例作为强先验
- 实验或效果：在pbo和bbob基准测试中，该方法展现出优越性能和鲁棒性

## 摘要（原文）

> Large Language Models (LLMs) have already been widely adopted for automated algorithm design, demonstrating strong abilities in generating and evolving algorithms across various fields. Existing work has largely focused on examining their effectiveness in solving specific problems, with search strategies primarily guided by adaptive prompt designs. In this paper, through investigating the token-wise attribution of the prompts to LLM-generated algorithmic codes, we show that providing high-quality algorithmic code examples can substantially improve the performance of the LLM-driven optimization. Building upon this insight, we propose leveraging prior benchmark algorithms to guide LLM-driven optimization and demonstrate superior performance on two black-box optimization benchmarks: the pseudo-Boolean optimization suite (pbo) and the black-box optimization suite (bbob). Our findings highlight the value of integrating benchmarking studies to enhance both efficiency and robustness of the LLM-driven black-box optimization methods.

