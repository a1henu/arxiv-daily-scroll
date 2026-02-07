---
layout: default
title: Hallucination-Resistant Security Planning with a Large Language Model
---

# Hallucination-Resistant Security Planning with a Large Language Model
**arXiv**：[2602.05279v1](https://arxiv.org/abs/2602.05279) · [PDF](https://arxiv.org/pdf/2602.05279.pdf)  
**作者**：Kim Hammar, Tansu Alpcan, Emil Lupu  

**一句话要点**：提出抗幻觉安全规划框架，通过迭代约束检查与上下文学习提升LLM在安全管理中的可靠性。

**关键词**：大语言模型, 安全管理, 抗幻觉, 上下文学习, 数字孪生, 决策支持

## 3 点简述
- 核心问题：LLM在安全管理中易产生幻觉，导致不可靠决策。
- 方法要点：集成LLM于迭代循环，检查动作一致性，低时收集外部反馈并利用上下文学习优化。
- 实验或效果：在四个公共数据集上，相比前沿LLM，恢复时间最多减少30%。

## 摘要（原文）

> Large language models (LLMs) are promising tools for supporting security management tasks, such as incident response planning. However, their unreliability and tendency to hallucinate remain significant challenges. In this paper, we address these challenges by introducing a principled framework for using an LLM as decision support in security management. Our framework integrates the LLM in an iterative loop where it generates candidate actions that are checked for consistency with system constraints and lookahead predictions. When consistency is low, we abstain from the generated actions and instead collect external feedback, e.g., by evaluating actions in a digital twin. This feedback is then used to refine the candidate actions through in-context learning (ICL). We prove that this design allows to control the hallucination risk by tuning the consistency threshold. Moreover, we establish a bound on the regret of ICL under certain assumptions. To evaluate our framework, we apply it to an incident response use case where the goal is to generate a response and recovery plan based on system logs. Experiments on four public datasets show that our framework reduces recovery times by up to 30% compared to frontier LLMs.

