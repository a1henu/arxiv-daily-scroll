---
layout: default
title: AgentDrive: An Open Benchmark Dataset for Agentic AI Reasoning with LLM-Generated Scenarios in Autonomous Systems
---

# AgentDrive: An Open Benchmark Dataset for Agentic AI Reasoning with LLM-Generated Scenarios in Autonomous Systems
**arXiv**：[2601.16964v1](https://arxiv.org/abs/2601.16964) · [PDF](https://arxiv.org/pdf/2601.16964.pdf)  
**作者**：Mohamed Amine Ferrag, Abderrahmane Lakas, Merouane Debbah  

**一句话要点**：提出AgentDrive基准数据集，用于在自动驾驶系统中评估和训练基于LLM的智能体推理能力。

**关键词**：自动驾驶基准, LLM生成场景, 智能体推理, 多选问答评估, 安全关键系统

## 3 点简述
- 核心问题：缺乏大规模、结构化且安全关键的基准来评估和训练自主系统中的智能体AI模型。
- 方法要点：通过LLM驱动的提示到JSON管道生成30万个驾驶场景，涵盖七个正交轴，并进行模拟验证和标注。
- 实验或效果：评估50个领先LLM在AgentDrive-MCQ基准上的表现，显示专有模型在上下文推理领先，开源模型在结构化推理上快速追赶。

## 摘要（原文）

> The rapid advancement of large language models (LLMs) has sparked growing interest in their integration into autonomous systems for reasoning-driven perception, planning, and decision-making. However, evaluating and training such agentic AI models remains challenging due to the lack of large-scale, structured, and safety-critical benchmarks. This paper introduces AgentDrive, an open benchmark dataset containing 300,000 LLM-generated driving scenarios designed for training, fine-tuning, and evaluating autonomous agents under diverse conditions. AgentDrive formalizes a factorized scenario space across seven orthogonal axes: scenario type, driver behavior, environment, road layout, objective, difficulty, and traffic density. An LLM-driven prompt-to-JSON pipeline generates semantically rich, simulation-ready specifications that are validated against physical and schema constraints. Each scenario undergoes simulation rollouts, surrogate safety metric computation, and rule-based outcome labeling. To complement simulation-based evaluation, we introduce AgentDrive-MCQ, a 100,000-question multiple-choice benchmark spanning five reasoning dimensions: physics, policy, hybrid, scenario, and comparative reasoning. We conduct a large-scale evaluation of fifty leading LLMs on AgentDrive-MCQ. Results show that while proprietary frontier models perform best in contextual and policy reasoning, advanced open models are rapidly closing the gap in structured and physics-grounded reasoning. We release the AgentDrive dataset, AgentDrive-MCQ benchmark, evaluation code, and related materials at https://github.com/maferrag/AgentDrive

