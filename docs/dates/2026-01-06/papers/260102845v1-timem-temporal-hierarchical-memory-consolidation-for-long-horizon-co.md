---
layout: default
title: TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents
---

# TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents
**arXiv**：[2601.02845v1](https://arxiv.org/abs/2601.02845) · [PDF](https://arxiv.org/pdf/2601.02845.pdf)  
**作者**：Kai Li, Xuanqing Yu, Ziyi Ni, Yi Zeng, Yao Xu, Zheqing Zhang, Xin Li, Jitao Sang, Xiaogang Duan, Xuelei Wang, Chengbao Liu, Jie Tan  

**一句话要点**：提出TiMem框架，通过时间层次记忆整合解决长程对话代理中历史信息管理问题。

**关键词**：长程对话代理, 记忆整合, 时间层次结构, 记忆树, 语义引导, 复杂度感知召回

## 3 点简述
- 核心问题：长程对话代理需管理超出LLM上下文窗口的交互历史，现有方法在时间层次结构支持不足。
- 方法要点：采用时间记忆树组织对话，实现从原始观察到抽象人物表征的系统记忆整合，无需微调。
- 实验或效果：在LoCoMo和LongMemEval-S基准上达到SOTA准确率，召回记忆长度减少52.20%。

## 摘要（原文）

> Long-horizon conversational agents have to manage ever-growing interaction histories that quickly exceed the finite context windows of large language models (LLMs). Existing memory frameworks provide limited support for temporally structured information across hierarchical levels, often leading to fragmented memories and unstable long-horizon personalization. We present TiMem, a temporal--hierarchical memory framework that organizes conversations through a Temporal Memory Tree (TMT), enabling systematic memory consolidation from raw conversational observations to progressively abstracted persona representations. TiMem is characterized by three core properties: (1) temporal--hierarchical organization through TMT; (2) semantic-guided consolidation that enables memory integration across hierarchical levels without fine-tuning; and (3) complexity-aware memory recall that balances precision and efficiency across queries of varying complexity. Under a consistent evaluation setup, TiMem achieves state-of-the-art accuracy on both benchmarks, reaching 75.30% on LoCoMo and 76.88% on LongMemEval-S. It outperforms all evaluated baselines while reducing the recalled memory length by 52.20% on LoCoMo. Manifold analysis indicates clear persona separation on LoCoMo and reduced dispersion on LongMemEval-S. Overall, TiMem treats temporal continuity as a first-class organizing principle for long-horizon memory in conversational agents.

