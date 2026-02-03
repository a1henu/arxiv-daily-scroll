---
layout: default
title: S1-NexusAgent: a Self-Evolving Agent Framework for Multidisciplinary Scientific Research
---

# S1-NexusAgent: a Self-Evolving Agent Framework for Multidisciplinary Scientific Research
**arXiv**：[2602.01550v1](https://arxiv.org/abs/2602.01550) · [PDF](https://arxiv.org/pdf/2602.01550.pdf)  
**作者**：S1-NexusAgent Team  

**一句话要点**：提出S1-NexusAgent自进化代理框架，以解决多学科科学研究中长程规划与工具协调的挑战。

**关键词**：自进化代理, 多学科科学研究, 长程规划, 工具协调, 稀疏上下文管理, 科学技能蒸馏

## 3 点简述
- 核心问题：现有LLM和工具代理在长程规划、目标维护和持续学习方面存在局限，难以处理大规模数据和复杂科学工作流。
- 方法要点：采用分层Plan-and-CodeAct执行范式，通过双循环架构解耦全局规划与子任务执行，支持MCP协议和动态工具检索。
- 实验或效果：在生物、化学和材料科学基准测试中达到最先进性能，验证了在复杂科学任务中的有效性和泛化能力。

## 摘要（原文）

> Modern scientific research relies on large-scale data, complex workflows, and specialized tools, which existing LLMs and tool-based agents struggle to handle due to limitations in long-horizon planning, robust goal maintenance, and continual learning from execution. To address these issues, in this work, we propose S1-NexusAgent, a self-evolving agent framework designed for multidisciplinary scientific research. S1-NexusAgent adopts a hierarchical Plan-and-CodeAct execution paradigm, decoupling global scientific planning from subtask-level tool execution through a dual-loop architecture, thereby enabling stable modeling of complex research workflows. The system natively supports the Model Context Protocol (MCP), integrates up to thousands of cross-disciplinary scientific tools, and achieves efficient orchestration of heterogeneous research tools via intention-aware dynamic tool retrieval and hot-plug mechanisms. To address long-context and large-scale data challenges in scientific settings, S1-NexusAgent introduces object-reference-based sparse context management, which enables sub-task context isolation and intermediate result compression. Building on this, a Critic Agent automatically evaluates complete execution trajectories and distills high-quality research paths into reusable Scientific Skills, forming a closed loop for continuous self-evolution, which is valuable for sustainable and long-horizon scientific research. Experiments on authoritative scientific benchmarks involving long-horizon planning and complex specialized tool orchestration, including biomini-eval (biology), ChemBench (chemistry), and MatSciBench (material science), demonstrate that S1-NexusAgent achieves state-of-the-art performance, validating its effectiveness and generalization capability in complex scientific tasks.

