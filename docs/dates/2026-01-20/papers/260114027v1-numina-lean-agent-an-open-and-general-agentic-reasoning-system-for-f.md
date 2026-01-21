---
layout: default
title: Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics
---

# Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics
**arXiv**：[2601.14027v1](https://arxiv.org/abs/2601.14027) · [PDF](https://arxiv.org/pdf/2601.14027.pdf)  
**作者**：Junqi Liu, Zihao Zhou, Zekai Zhu, Marco Dos Santos, Weikun He, Jiawei Liu, Ran Wang, Yunzhou Xie, Junqiao Zhao, Qiufeng Wang, Lihong Zhi, Jia Li, Wenda Li  

**一句话要点**：提出Numina-Lean-Agent，使用通用编码代理作为形式数学推理系统，以提升灵活性和性能。

**关键词**：形式定理证明, 通用编码代理, 自主推理系统, 数学形式化, 工具调用

## 3 点简述
- 现有形式定理证明系统依赖任务特定管道和训练模型，限制灵活性和可复现性。
- 采用通用编码代理范式，结合Claude Code与Numina-Lean-MCP，实现与Lean的自主交互和工具调用。
- 在Putnam 2025问题中解决全部12题，并成功形式化Brascamp-Lieb定理，展示通用性。

## 摘要（原文）

> Agentic systems have recently become the dominant paradigm for formal theorem proving, achieving strong performance by coordinating multiple models and tools. However, existing approaches often rely on task-specific pipelines and trained formal provers, limiting their flexibility and reproducibility. In this paper, we propose the paradigm that directly uses a general coding agent as a formal math reasoner. This paradigm is motivated by (1) A general coding agent provides a natural interface for diverse reasoning tasks beyond proving, (2) Performance can be improved by simply replacing the underlying base model, without training, and (3) MCP enables flexible extension and autonomous calling of specialized tools, avoiding complex design. Based on this paradigm, we introduce Numina-Lean-Agent, which combines Claude Code with Numina-Lean-MCP to enable autonomous interaction with Lean, retrieval of relevant theorems, informal proving and auxiliary reasoning tools. Using Claude Opus 4.5 as the base model, Numina-Lean-Agent solves all problems in Putnam 2025 (12 / 12), matching the best closed-source system. Beyond benchmark evaluation, we further demonstrate its generality by interacting with mathematicians to successfully formalize the Brascamp-Lieb theorem. We release Numina-Lean-Agent and all solutions at https://github.com/project-numina/numina-lean-agent.

