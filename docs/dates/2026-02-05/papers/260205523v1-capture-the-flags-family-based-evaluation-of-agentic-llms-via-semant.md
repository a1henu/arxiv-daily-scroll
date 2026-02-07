---
layout: default
title: Capture the Flags: Family-Based Evaluation of Agentic LLMs via Semantics-Preserving Transformations
---

# Capture the Flags: Family-Based Evaluation of Agentic LLMs via Semantics-Preserving Transformations
**arXiv**：[2602.05523v1](https://arxiv.org/abs/2602.05523) · [PDF](https://arxiv.org/pdf/2602.05523.pdf)  
**作者**：Shahin Honarvar, Amber Gorzynski, James Lee-Jones, Harry Coppock, Marek Rei, Joseph Ryan, Alastair F. Donaldson  

**一句话要点**：提出基于语义保留变换的CTF挑战家族方法，以评估智能体LLM在网络安全任务中的鲁棒性。

**关键词**：智能体大语言模型, 网络安全评估, 语义保留变换, CTF挑战家族, 鲁棒性分析, 工具使用

## 3 点简述
- 现有CTF基准在评估智能体LLM对源代码变换的鲁棒性和泛化能力方面有限。
- 引入CTF挑战家族，通过语义保留程序变换生成语义等价挑战，实现可控评估。
- 使用Evolve-CTF工具评估13个智能体LLM配置，发现模型对某些变换鲁棒，但复杂变换影响性能。

## 摘要（原文）

> Agentic large language models (LLMs) are increasingly evaluated on cybersecurity tasks using capture-the-flag (CTF) benchmarks. However, existing pointwise benchmarks have limited ability to shed light on the robustness and generalisation abilities of agents across alternative versions of the source code. We introduce CTF challenge families, whereby a single CTF is used as the basis for generating a family of semantically-equivalent challenges via semantics-preserving program transformations. This enables controlled evaluation of agent robustness to source code transformations while keeping the underlying exploit strategy fixed. We introduce a new tool, Evolve-CTF, that generates CTF families from Python challenges using a range of transformations. Using Evolve-CTF to derive families from Cybench and Intercode challenges, we evaluate 13 agentic LLM configurations with tool access. We find that models are remarkably robust to intrusive renaming and code insertion-based transformations, but that composed transformations and deeper obfuscation affect performance by requiring more sophisticated use of tools. We also find that enabling explicit reasoning has little effect on solution success rates across challenge families. Our work contributes a valuable technique and tool for future LLM evaluations, and a large dataset characterising the capabilities of current state-of-the-art models in this domain.

