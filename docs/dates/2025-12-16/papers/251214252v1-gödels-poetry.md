---
layout: default
title: Gödel's Poetry
---

# Gödel's Poetry
**arXiv**：[2512.14252v1](https://arxiv.org/abs/2512.14252) · [PDF](https://arxiv.org/pdf/2512.14252.pdf)  
**作者**：Kelly J. Davis  

**一句话要点**：提出基于语言模型与递归分解的多智能体定理证明系统，提升Lean4证明生成性能

**关键词**：定理证明, 语言模型, 递归分解, 多智能体系统, Lean4, 自动化推理

## 3 点简述
- 核心问题：自动化定理证明是人工智能的长期挑战，需高效处理复杂定理。
- 方法要点：结合专用语言模型生成Lean4证明，通过递归分解将困难定理简化为更简单命题。
- 实验或效果：在miniF2F基准上，无分解时通过率90.4%，引入分解后性能显著提升。

## 摘要（原文）

> Formal, automated theorem proving has long been viewed as a challenge to artificial intelligence. We introduce here a new approach to computer theorem proving, one that employs specialized language models for Lean4 proof generation combined with recursive decomposition of difficult theorems into simpler entailing propositions. These models are coordinated through a multi-agent architecture that orchestrates autoformalization (if required), proof generation, decomposition of difficult theorems into simpler entailing propositions, and recursive proof (and/or decomposition) of these propositions. Without decomposition, we achieve a 90.4% pass rate on miniF2F. With decomposition, this is significantly improved. A key technical contribution lies in our extension of the Kimina Lean Server with abstract syntax tree (AST) parsing capabilities to facilitate automated, recursive proof decomposition. The system is made available on PyPI as goedels-poetry (at https://pypi.org/project/goedels-poetry ), and the open-source implementation KellyJDavis/goedels-poetry (at https://github.com/KellyJDavis/goedels-poetry ) facilitates both adaptation to alternative language models and extension with custom functionality.

