---
layout: default
title: Capturing P: On the Expressive Power and Efficient Evaluation of Boolean Retrieval
---

# Capturing P: On the Expressive Power and Efficient Evaluation of Boolean Retrieval
**arXiv**：[2601.18747v1](https://arxiv.org/abs/2601.18747) · [PDF](https://arxiv.org/pdf/2601.18747.pdf)  
**作者**：Amir Aavani  

**一句话要点**：提出基于DAG的检索语言和ComputePN算法，以高效评估复杂逻辑查询，解决信息检索中的效率困境。

**关键词**：信息检索, 复杂度理论, DAG检索语言, 多项式时间评估, ComputePN算法, 神经符号推理

## 3 点简述
- 核心问题：现代信息检索面临复杂逻辑约束下的效率困境，传统引擎难以平衡运行时间和内存消耗。
- 方法要点：定义基于DAG的检索语言，证明其捕获P类复杂度，并设计ComputePN算法实现高效评估。
- 实验或效果：ComputePN通过DAG遍历和正负响应机制，确保任何查询在多项式时间内可高效执行。

## 摘要（原文）

> Modern information retrieval is transitioning from simple document filtering to complex, neuro-symbolic reasoning workflows. However, current retrieval architectures face a fundamental efficiency dilemma when handling the rigorous logical and arithmetic constraints required by this new paradigm. Standard iterator-based engines (Document-at-a-Time) do not natively support complex, nested logic graphs; forcing them to execute such queries typically results in intractable runtime performance. Conversely, naive recursive approaches (Term-at-a-Time), while capable of supporting these structures, suffer from prohibitive memory consumption when enforcing broad logical exclusions.
>   In this paper, we propose that a retrieval engine must be capable of ``Capturing $\mathbf{P}$'' -- evaluating any polynomial-time property directly over its index in a computationally efficient manner. We define a formal Retrieval Language ($\mathcal{L}_R$) based on Directed Acyclic Graphs (DAGs) and prove it precisely captures the complexity class $\mathbf{P}$. We introduce \texttt{ComputePN}, a novel evaluation algorithm that makes $\mathcal{L}_R$ tractable. By combining native DAG traversal with a memory-efficient ``Positive-Negative'' response mechanism, \texttt{ComputePN} ensures the efficient evaluation of any query in $\mathcal{L}_R$. This work establishes the theoretical foundation for turning the search index into a general-purpose computational engine.

