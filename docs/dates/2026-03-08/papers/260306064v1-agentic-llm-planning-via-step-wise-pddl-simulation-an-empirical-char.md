---
layout: default
title: Agentic LLM Planning via Step-Wise PDDL Simulation: An Empirical Characterisation
---

# Agentic LLM Planning via Step-Wise PDDL Simulation: An Empirical Characterisation
**arXiv**：[2603.06064v1](https://arxiv.org/abs/2603.06064) · [PDF](https://arxiv.org/pdf/2603.06064.pdf)  
**作者**：Kai Göbel, Pierrick Lorang, Patrik Zips, Tobias Glück  

**一句话要点**：提出PyPDDLEngine通过逐步PDDL模拟实现代理式LLM规划，评估其在Blocksworld任务中的性能。

**关键词**：任务规划, 大语言模型, PDDL模拟, 代理式规划, Blocksworld, 规划评估

## 3 点简述
- 核心问题：探究LLM能否作为可行规划器，与经典符号方法相比在任务规划中的表现。
- 方法要点：开发PyPDDLEngine，将PDDL规划操作作为LLM工具调用，支持逐步交互式搜索。
- 实验或效果：在IPC Blocksworld实例上评估，代理式LLM规划成功率66.7%，略高于直接规划，但成本更高。

## 摘要（原文）

> Task planning, the problem of sequencing actions to reach a goal from an initial state, is a core capability requirement for autonomous robotic systems. Whether large language models (LLMs) can serve as viable planners alongside classical symbolic methods remains an open question. We present PyPDDLEngine, an open-source Planning Domain Definition Language (PDDL) simulation engine that exposes planning operations as LLM tool calls through a Model Context Protocol (MCP) interface. Rather than committing to a complete action sequence upfront, the LLM acts as an interactive search policy that selects one action at a time, observes each resulting state, and can reset and retry. We evaluate four approaches on 102 International Planning Competition (IPC) Blocksworld instances under a uniform 180-second budget: Fast Downward lama-first and seq-sat-lama-2011 as classical baselines, direct LLM planning (Claude Haiku 4.5), and agentic LLM planning via PyPDDLEngine. Fast Downward achieves 85.3% success. The direct and agentic LLM approaches achieve 63.7% and 66.7%, respectively, a consistent but modest three-percentage-point advantage for the agentic approach at $5.7\times$ higher token cost per solution. Across most co-solved difficulty blocks, both LLM approaches produce shorter plans than seq-sat-lama-2011 despite its iterative quality improvement, a result consistent with training-data recall rather than generalisable planning. These results suggest that agentic gains depend on the nature of environmental feedback. Coding agents benefit from externally grounded signals such as compiler errors and test failures, whereas PDDL step feedback is self-assessed, leaving the agent to evaluate its own progress without external verification.

