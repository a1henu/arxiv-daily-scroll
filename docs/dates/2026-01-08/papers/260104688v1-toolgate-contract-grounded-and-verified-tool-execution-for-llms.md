---
layout: default
title: ToolGate: Contract-Grounded and Verified Tool Execution for LLMs
---

# ToolGate: Contract-Grounded and Verified Tool Execution for LLMs
**arXiv**：[2601.04688v1](https://arxiv.org/abs/2601.04688) · [PDF](https://arxiv.org/pdf/2601.04688.pdf)  
**作者**：Yanming Liu, Xinyue Peng, Jiannan Cao, Xinyi Wang, Songhang Deng, Jintao Chen, Jianwei Yin, Xuhong Zhang  

**一句话要点**：提出ToolGate框架，通过合约式工具执行保障LLM工具调用的逻辑安全与可验证性

**关键词**：大语言模型工具调用, 形式化验证, 逻辑安全, 符号状态空间, Hoare合约, 可验证执行

## 3 点简述
- 现有LLM工具调用框架依赖自然语言推理，缺乏逻辑安全的形式化保证
- ToolGate采用Hoare式合约形式化工具，通过前置条件门控调用、后置条件验证结果
- 实验表明该框架显著提升工具增强LLM系统的可靠性与可验证性，保持多步推理性能

## 摘要（原文）

> Large Language Models (LLMs) augmented with external tools have demonstrated remarkable capabilities in complex reasoning tasks. However, existing frameworks rely heavily on natural language reasoning to determine when tools can be invoked and whether their results should be committed, lacking formal guarantees for logical safety and verifiability. We present \textbf{ToolGate}, a forward execution framework that provides logical safety guarantees and verifiable state evolution for LLM tool calling. ToolGate maintains an explicit symbolic state space as a typed key-value mapping representing trusted world information throughout the reasoning process. Each tool is formalized as a Hoare-style contract consisting of a precondition and a postcondition, where the precondition gates tool invocation by checking whether the current state satisfies the required conditions, and the postcondition determines whether the tool's result can be committed to update the state through runtime verification. Our approach guarantees that the symbolic state evolves only through verified tool executions, preventing invalid or hallucinated results from corrupting the world representation. Experimental validation demonstrates that ToolGate significantly improves the reliability and verifiability of tool-augmented LLM systems while maintaining competitive performance on complex multi-step reasoning tasks. This work establishes a foundation for building more trustworthy and debuggable AI systems that integrate language models with external tools.

