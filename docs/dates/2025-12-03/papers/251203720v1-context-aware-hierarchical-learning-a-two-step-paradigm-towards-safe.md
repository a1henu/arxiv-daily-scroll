---
layout: default
title: Context-Aware Hierarchical Learning: A Two-Step Paradigm towards Safer LLMs
---

# Context-Aware Hierarchical Learning: A Two-Step Paradigm towards Safer LLMs
**arXiv**：[2512.03720v1](https://arxiv.org/abs/2512.03720) · [PDF](https://arxiv.org/pdf/2512.03720.pdf)  
**作者**：Tengyun Ma, Jiaqi Yao, Daojing He, Shihao Peng, Yu Li, Shaohui Liu, Zhuotao Tian  

**一句话要点**：提出上下文感知分层学习以增强大语言模型在对抗场景下的安全性

**关键词**：大语言模型安全, 工具完成攻击, 上下文感知分层学习, 对抗性评估, 零样本泛化

## 3 点简述
- 识别工具完成攻击，利用函数调用机制颠覆模型行为
- 引入上下文感知分层学习，动态平衡语义理解与角色特定指令约束
- 实验显示该方法显著提升模型鲁棒性，在零样本评估中表现良好

## 摘要（原文）

> Large Language Models (LLMs) have emerged as powerful tools for diverse applications. However, their uniform token processing paradigm introduces critical vulnerabilities in instruction handling, particularly when exposed to adversarial scenarios. In this work, we identify and propose a novel class of vulnerabilities, termed Tool-Completion Attack (TCA), which exploits function-calling mechanisms to subvert model behavior. To evaluate LLM robustness against such threats, we introduce the Tool-Completion benchmark, a comprehensive security assessment framework, which reveals that even state-of-the-art models remain susceptible to TCA, with surprisingly high attack success rates. To address these vulnerabilities, we introduce Context-Aware Hierarchical Learning (CAHL), a sophisticated mechanism that dynamically balances semantic comprehension with role-specific instruction constraints. CAHL leverages the contextual correlations between different instruction segments to establish a robust, context-aware instruction hierarchy. Extensive experiments demonstrate that CAHL significantly enhances LLM robustness against both conventional attacks and the proposed TCA, exhibiting strong generalization capabilities in zero-shot evaluations while still preserving model performance on generic tasks. Our code is available at https://github.com/S2AILab/CAHL.

