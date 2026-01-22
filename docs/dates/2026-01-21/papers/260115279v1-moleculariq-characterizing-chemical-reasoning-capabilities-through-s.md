---
layout: default
title: MolecularIQ: Characterizing Chemical Reasoning Capabilities Through Symbolic Verification on Molecular Graphs
---

# MolecularIQ: Characterizing Chemical Reasoning Capabilities Through Symbolic Verification on Molecular Graphs
**arXiv**：[2601.15279v1](https://arxiv.org/abs/2601.15279) · [PDF](https://arxiv.org/pdf/2601.15279.pdf)  
**作者**：Christoph Bartmann, Johannes Schimunek, Mykyta Ielanskyi, Philipp Seidl, Günter Klambauer, Sohvi Luukkonen  

**一句话要点**：提出MolecularIQ基准，通过符号验证评估大语言模型在分子图上的推理能力。

**关键词**：分子图推理, 符号验证, 大语言模型评估, 化学基准, 细粒度分析

## 3 点简述
- 现有化学基准依赖文献或选择题，存在泄漏或偏差风险。
- MolecularIQ专注于符号可验证任务，实现分子图推理的细粒度评估。
- 基准揭示模型能力模式，定位失败于特定任务和分子结构，指导模型开发。

## 摘要（原文）

> A molecule's properties are fundamentally determined by its composition and structure encoded in its molecular graph. Thus, reasoning about molecular properties requires the ability to parse and understand the molecular graph. Large Language Models (LLMs) are increasingly applied to chemistry, tackling tasks such as molecular name conversion, captioning, text-guided generation, and property or reaction prediction. Most existing benchmarks emphasize general chemical knowledge, rely on literature or surrogate labels that risk leakage or bias, or reduce evaluation to multiple-choice questions. We introduce MolecularIQ, a molecular structure reasoning benchmark focused exclusively on symbolically verifiable tasks. MolecularIQ enables fine-grained evaluation of reasoning over molecular graphs and reveals capability patterns that localize model failures to specific tasks and molecular structures. This provides actionable insights into the strengths and limitations of current chemistry LLMs and guides the development of models that reason faithfully over molecular structure.

