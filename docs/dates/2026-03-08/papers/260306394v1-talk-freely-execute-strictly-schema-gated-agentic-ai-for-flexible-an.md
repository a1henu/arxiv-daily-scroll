---
layout: default
title: Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows
---

# Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows
**arXiv**：[2603.06394v1](https://arxiv.org/abs/2603.06394) · [PDF](https://arxiv.org/pdf/2603.06394.pdf)  
**作者**：Joel Strickland, Arjun Vijeta, Chris Moores, Oliwia Bodek, Bogdan Nenchev, Thomas Whitehead, Charles Phillips, Karl Tassenberg, Gareth Conduit, Ben Pellegrini  

**一句话要点**：提出模式门控编排以解决科学工作流中确定性与灵活性的权衡问题

**关键词**：模式门控编排, 科学工作流自动化, LLM代理, 执行确定性, 对话灵活性, 多模型评估

## 3 点简述
- 核心问题：LLM驱动的科学工作流需平衡确定性执行与对话灵活性，现有系统难以兼顾
- 方法要点：引入模式门控编排，将模式作为强制执行边界，确保动作验证后才运行
- 实验或效果：通过多模型LLM评分评估20个系统，发现帕累托前沿，模式门控架构有望解耦权衡

## 摘要（原文）

> Large language models (LLMs) can now translate a researcher's plain-language goal into executable computation, yet scientific workflows demand determinism, provenance, and governance that are difficult to guarantee when an LLM decides what runs. Semi-structured interviews with 18 experts across 10 industrial R&D stakeholders surface 2 competing requirements--deterministic, constrained execution and conversational flexibility without workflow rigidity--together with boundary properties (human-in-the-loop control and transparency) that any resolution must satisfy. We propose schema-gated orchestration as the resolving principle: the schema becomes a mandatory execution boundary at the composed-workflow level, so that nothing runs unless the complete action--including cross-step dependencies--validates against a machine-checkable specification.
>   We operationalize the 2 requirements as execution determinism (ED) and conversational flexibility (CF), and use these axes to review 20 systems spanning 5 architectural groups along a validation-scope spectrum. Scores are assigned via a multi-model protocol--15 independent sessions across 3 LLM families--yielding substantial-to-near-perfect inter-model agreement (Krippendorff a=0.80 for ED and a=0.98 for CF), demonstrating that multi-model LLM scoring can serve as a reusable alternative to human expert panels for architectural assessment.
>   The resulting landscape reveals an empirical Pareto front--no reviewed system achieves both high flexibility and high determinism--but a convergence zone emerges between the generative and workflow-centric extremes. We argue that a schema-gated architecture, separating conversational from execution authority, is positioned to decouple this trade-off, and distill 3 operational principles--clarification-before-execution, constrained plan-act orchestration, and tool-to-workflow-level gating--to guide adoption.

