---
layout: default
title: MATRIX AS PLAN: Structured Logical Reasoning with Feedback-Driven Replanning
---

# MATRIX AS PLAN: Structured Logical Reasoning with Feedback-Driven Replanning
**arXiv**：[2601.10101v1](https://arxiv.org/abs/2601.10101) · [PDF](https://arxiv.org/pdf/2601.10101.pdf)  
**作者**：Ke Chen, Jiandian Zeng, Zihao Peng, Guo Li, Guangxue Zhang, Tian Wang  

**一句话要点**：提出MatrixCoT框架以增强大语言模型在复杂符号推理任务中的鲁棒性和可解释性。

**关键词**：逻辑推理, 矩阵化规划, 反馈驱动重规划, 符号推理, 大语言模型

## 3 点简述
- 核心问题：现有方法在符号推理任务中面临格式敏感性和缺乏结构化错误纠正机制。
- 方法要点：引入矩阵化规划与反馈驱动重规划，提升执行稳定性和可信度。
- 实验或效果：在五个逻辑推理基准上验证，无需外部求解器即可保持竞争力。

## 摘要（原文）

> As knowledge and semantics on the web grow increasingly complex, enhancing Large Language Models (LLMs) comprehension and reasoning capabilities has become particularly important. Chain-of-Thought (CoT) prompting has been shown to enhance the reasoning capabilities of LLMs. However, it still falls short on logical reasoning tasks that rely on symbolic expressions and strict deductive rules. Neuro-symbolic methods address this gap by enforcing formal correctness through external solvers. Yet these solvers are highly format-sensitive, and small instabilities in model outputs can lead to frequent processing failures. LLM-driven approaches avoid parsing brittleness, but they lack structured representations and process-level error-correction mechanisms. To further enhance the logical reasoning capabilities of LLMs, we propose MatrixCoT, a structured CoT framework with a matrix-based plan. Specifically, we normalize and type natural language expressions, attach explicit citation fields, and introduce a matrix-based planning method to preserve global relations among steps. The plan becomes a verifiable artifact, making execution more stable. For verification, we also add a feedback-driven replanning mechanism. Under semantic-equivalence constraints, it identifies omissions and defects, rewrites and compresses the dependency matrix, and produces a more trustworthy final answer. Experiments on five logical-reasoning benchmarks and five LLMs show that, without relying on external solvers, MatrixCoT enhances both robustness and interpretability when tackling complex symbolic reasoning tasks, while maintaining competitive performance.

