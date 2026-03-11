---
layout: default
title: Deep Tabular Research via Continual Experience-Driven Execution
---

# Deep Tabular Research via Continual Experience-Driven Execution
**arXiv**：[2603.09151v1](https://arxiv.org/abs/2603.09151) · [PDF](https://arxiv.org/pdf/2603.09151.pdf)  
**作者**：Junnan Dong, Chuang Zhou, Zheng Yuan, Yifei Yu, Siyu An, Di Yin, Xing Sun, Feiyue Huang  

**一句话要点**：提出基于持续经验驱动的执行框架以解决深度表格研究中的长程推理挑战

**关键词**：深度表格研究, 长程推理, 表格理解, 代理框架, 持续学习, 非规范布局

## 3 点简述
- 核心问题：大语言模型在处理具有层次和双向表头的非规范布局表格时，难以完成复杂长程分析任务。
- 方法要点：构建分层元图捕获语义，引入期望感知选择策略，并利用孪生结构记忆持续优化执行路径。
- 实验或效果：在挑战性非结构化表格基准上验证有效性，强调战略规划与低级执行分离的必要性。

## 摘要（原文）

> Large language models often struggle with complex long-horizon analytical tasks over unstructured tables, which typically feature hierarchical and bidirectional headers and non-canonical layouts. We formalize this challenge as Deep Tabular Research (DTR), requiring multi-step reasoning over interdependent table regions. To address DTR, we propose a novel agentic framework that treats tabular reasoning as a closed-loop decision-making process. We carefully design a coupled query and table comprehension for path decision making and operational execution. Specifically, (i) DTR first constructs a hierarchical meta graph to capture bidirectional semantics, mapping natural language queries into an operation-level search space; (ii) To navigate this space, we introduce an expectation-aware selection policy that prioritizes high-utility execution paths; (iii) Crucially, historical execution outcomes are synthesized into a siamese structured memory, i.e., parameterized updates and abstracted texts, enabling continual refinement. Extensive experiments on challenging unstructured tabular benchmarks verify the effectiveness and highlight the necessity of separating strategic planning from low-level execution for long-horizon tabular reasoning.

