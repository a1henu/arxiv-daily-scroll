---
layout: default
title: Reasoning While Asking: Transforming Reasoning Large Language Models from Passive Solvers to Proactive Inquirers
---

# Reasoning While Asking: Transforming Reasoning Large Language Models from Passive Solvers to Proactive Inquirers
**arXiv**：[2601.22139v1](https://arxiv.org/abs/2601.22139) · [PDF](https://arxiv.org/pdf/2601.22139.pdf)  
**作者**：Xin Chen, Feng Jiang, Yiqian Zhang, Hardy Chen, Shuo Yan, Wenya Xie, Min Yang, Shujian Huang  

**一句话要点**：提出主动交互推理范式，将推理大语言模型从被动求解器转变为主动询问者

**关键词**：主动交互推理, 不确定性感知, 监督微调, 策略优化, 数学推理, 代码生成

## 3 点简述
- 核心问题：现有推理大语言模型在关键信息缺失或模糊时仍盲目自思，导致效率低下和错误
- 方法要点：通过不确定性感知监督微调和用户模拟器策略优化，实现推理与澄清的交替进行
- 实验或效果：在数学推理、代码生成和文档编辑任务中，准确率、通过率和BLEU分数显著提升，同时减少近半推理计算和交互轮次

## 摘要（原文）

> Reasoning-oriented Large Language Models (LLMs) have achieved remarkable progress with Chain-of-Thought (CoT) prompting, yet they remain fundamentally limited by a \emph{blind self-thinking} paradigm: performing extensive internal reasoning even when critical information is missing or ambiguous. We propose Proactive Interactive Reasoning (PIR), a new reasoning paradigm that transforms LLMs from passive solvers into proactive inquirers that interleave reasoning with clarification. Unlike existing search- or tool-based frameworks that primarily address knowledge uncertainty by querying external environments, PIR targets premise- and intent-level uncertainty through direct interaction with the user. PIR is implemented via two core components: (1) an uncertainty-aware supervised fine-tuning procedure that equips models with interactive reasoning capability, and (2) a user-simulator-based policy optimization framework driven by a composite reward that aligns model behavior with user intent. Extensive experiments on mathematical reasoning, code generation, and document editing demonstrate that PIR consistently outperforms strong baselines, achieving up to 32.70\% higher accuracy, 22.90\% higher pass rate, and 41.36 BLEU improvement, while reducing nearly half of the reasoning computation and unnecessary interaction turns. Further reliability evaluations on factual knowledge, question answering, and missing-premise scenarios confirm the strong generalization and robustness of PIR. Model and code are publicly available at: \href{https://github.com/SUAT-AIRI/Proactive-Interactive-R1}

