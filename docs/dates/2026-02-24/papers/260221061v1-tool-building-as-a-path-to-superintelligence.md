---
layout: default
title: Tool Building as a Path to "Superintelligence"
---

# Tool Building as a Path to "Superintelligence"
**arXiv**：[2602.21061v1](https://arxiv.org/abs/2602.21061) · [PDF](https://arxiv.org/pdf/2602.21061.pdf)  
**作者**：David Koplow, Tomer Galanti, Tomaso Poggio  

**一句话要点**：提出GF(2)电路重建基准以评估LLM在Diligent Learner框架下的推理能力

**关键词**：Diligent Learner框架, 步成功概率γ, GF(2)电路重建, 逻辑分布外推理, 工具设计, 超级智能

## 3 点简述
- 核心问题：LLM在逻辑分布外推理中，步成功概率γ随深度增加而下降，影响超级智能实现
- 方法要点：设计基于GF(2)电路重建的任务，难度随推理步数增加，要求信息整合
- 实验或效果：前沿模型在任务中表现部分鲁棒，工具调用精度对大规模推理至关重要

## 摘要（原文）

> The Diligent Learner framework suggests LLMs can achieve superintelligence via test-time search, provided a sufficient step-success probability $γ$. In this work, we design a benchmark to measure $γ$ on logical out-of-distribution inference. We construct a class of tasks involving GF(2) circuit reconstruction that grow more difficult with each reasoning step, and that are, from an information-theoretic standpoint, impossible to reliably solve unless the LLM carefully integrates all of the information provided. Our analysis demonstrates that while the $γ$ value for small LLMs declines superlinearly as depth increases, frontier models exhibit partial robustness on this task. Furthermore, we find that successful reasoning at scale is contingent upon precise tool calls, identifying tool design as a critical capability for LLMs to achieve general superintelligence through the Diligent Learner framework.

