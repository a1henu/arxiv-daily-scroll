---
layout: default
title: Vibe Coding an LLM-powered Theorem Prover
---

# Vibe Coding an LLM-powered Theorem Prover
**arXiv**：[2601.04653v1](https://arxiv.org/abs/2601.04653) · [PDF](https://arxiv.org/pdf/2601.04653.pdf)  
**作者**：Zhe Hou  

**一句话要点**：提出Isabellm，一个基于LLM的Isabelle/HOL定理证明器，用于自动合成证明。

**关键词**：定理证明, 大语言模型, 自动证明合成, Isabelle/HOL, 证明规划, 代码生成

## 3 点简述
- 核心问题：LLM如何辅助自动定理证明，以克服传统自动化工具如Sledgehammer的局限。
- 方法要点：结合逐步证明器和高级证明规划器，集成束搜索、重排序模型、前提选择、微RAG和反例引导修复。
- 实验或效果：在消费级计算机上运行，能证明某些标准自动化无法处理的引理，但LLM在复杂算法实现上仍面临挑战。

## 摘要（原文）

> We present Isabellm, an LLM-powered theorem prover for Isabelle/HOL that performs fully automatic proof synthesis. Isabellm works with any local LLM on Ollama and APIs such as Gemini CLI, and it is designed to run on consumer grade computers. The system combines a stepwise prover, which uses large language models to propose proof commands validated by Isabelle in a bounded search loop, with a higher-level proof planner that generates structured Isar outlines and attempts to fill and repair remaining gaps. The framework includes beam search for tactics, tactics reranker ML and RL models, premise selection with small transformer models, micro-RAG for Isar proofs built from AFP, and counter-example guided proof repair. All the code is implemented by GPT 4.1 - 5.2, Gemini 3 Pro, and Claude 4.5. Empirically, Isabellm can prove certain lemmas that defeat Isabelle's standard automation, including Sledgehammer, demonstrating the practical value of LLM-guided proof search. At the same time, we find that even state-of-the-art LLMs, such as GPT 5.2 Extended Thinking and Gemini 3 Pro struggle to reliably implement the intended fill-and-repair mechanisms with complex algorithmic designs, highlighting fundamental challenges in LLM code generation and reasoning. The code of Isabellm is available at https://github.com/zhehou/llm-isabelle

