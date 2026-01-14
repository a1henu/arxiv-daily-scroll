---
layout: default
title: Evaluating Implicit Regulatory Compliance in LLM Tool Invocation via Logic-Guided Synthesis
---

# Evaluating Implicit Regulatory Compliance in LLM Tool Invocation via Logic-Guided Synthesis
**arXiv**：[2601.08196v1](https://arxiv.org/abs/2601.08196) · [PDF](https://arxiv.org/pdf/2601.08196.pdf)  
**作者**：Da Song, Yuheng Huang, Boqi Chen, Tianshuo Cong, Randy Goebel, Lei Ma, Foutse Khomh  

**一句话要点**：提出LogiSafetyGen框架以评估LLM工具调用中的隐式合规性

**关键词**：大语言模型, 工具调用, 监管合规, 线性时序逻辑, 安全评估, 基准测试

## 3 点简述
- 问题：现有基准忽视LLM在自主工具使用中的隐式监管合规性，无法评估安全约束执行能力。
- 方法：将非结构化法规转换为线性时序逻辑预言机，通过逻辑引导模糊测试合成安全关键轨迹。
- 效果：构建LogiSafetyBench基准，评估13个SOTA LLM发现大模型常优先任务完成而忽视安全合规。

## 摘要（原文）

> The integration of large language models (LLMs) into autonomous agents has enabled complex tool use, yet in high-stakes domains, these systems must strictly adhere to regulatory standards beyond simple functional correctness. However, existing benchmarks often overlook implicit regulatory compliance, thus failing to evaluate whether LLMs can autonomously enforce mandatory safety constraints. To fill this gap, we introduce LogiSafetyGen, a framework that converts unstructured regulations into Linear Temporal Logic oracles and employs logic-guided fuzzing to synthesize valid, safety-critical traces. Building on this framework, we construct LogiSafetyBench, a benchmark comprising 240 human-verified tasks that require LLMs to generate Python programs that satisfy both functional objectives and latent compliance rules. Evaluations of 13 state-of-the-art (SOTA) LLMs reveal that larger models, despite achieving better functional correctness, frequently prioritize task completion over safety, which results in non-compliant behavior.

