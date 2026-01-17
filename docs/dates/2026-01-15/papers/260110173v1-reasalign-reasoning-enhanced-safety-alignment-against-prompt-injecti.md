---
layout: default
title: ReasAlign: Reasoning Enhanced Safety Alignment against Prompt Injection Attack
---

# ReasAlign: Reasoning Enhanced Safety Alignment against Prompt Injection Attack
**arXiv**：[2601.10173v1](https://arxiv.org/abs/2601.10173) · [PDF](https://arxiv.org/pdf/2601.10173.pdf)  
**作者**：Hao Li, Yankai Yang, G. Edward Suh, Ning Zhang, Chaowei Xiao  

**一句话要点**：提出ReasAlign模型级解决方案，通过结构化推理增强安全对齐以防御间接提示注入攻击。

**关键词**：安全对齐, 提示注入攻击, 结构化推理, 代理系统, 模型级防御

## 3 点简述
- 核心问题：大型语言模型代理系统易受间接提示注入攻击，恶意指令可劫持行为。
- 方法要点：结合结构化推理步骤分析查询、检测冲突指令，保持用户任务连续性。
- 实验或效果：在CyberSecEval2基准上，ReasAlign实现94.6%效用和3.6%攻击成功率，优于现有最佳防御模型。

## 摘要（原文）

> Large Language Models (LLMs) have enabled the development of powerful agentic systems capable of automating complex workflows across various fields. However, these systems are highly vulnerable to indirect prompt injection attacks, where malicious instructions embedded in external data can hijack agent behavior. In this work, we present ReasAlign, a model-level solution to improve safety alignment against indirect prompt injection attacks. The core idea of ReasAlign is to incorporate structured reasoning steps to analyze user queries, detect conflicting instructions, and preserve the continuity of the user's intended tasks to defend against indirect injection attacks. To further ensure reasoning logic and accuracy, we introduce a test-time scaling mechanism with a preference-optimized judge model that scores reasoning steps and selects the best trajectory. Comprehensive evaluations across various benchmarks show that ReasAlign maintains utility comparable to an undefended model while consistently outperforming Meta SecAlign, the strongest prior guardrail. On the representative open-ended CyberSecEval2 benchmark, which includes multiple prompt-injected tasks, ReasAlign achieves 94.6% utility and only 3.6% ASR, far surpassing the state-of-the-art defensive model of Meta SecAlign (56.4% utility and 74.4% ASR). These results demonstrate that ReasAlign achieves the best trade-off between security and utility, establishing a robust and practical defense against prompt injection attacks in real-world agentic systems. Our code and experimental results could be found at https://github.com/leolee99/ReasAlign.

