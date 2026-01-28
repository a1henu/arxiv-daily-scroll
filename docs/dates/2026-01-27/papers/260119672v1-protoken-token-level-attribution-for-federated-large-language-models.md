---
layout: default
title: ProToken: Token-Level Attribution for Federated Large Language Models
---

# ProToken: Token-Level Attribution for Federated Large Language Models
**arXiv**：[2601.19672v1](https://arxiv.org/abs/2601.19672) · [PDF](https://arxiv.org/pdf/2601.19672.pdf)  
**作者**：Waris Gill, Ahmad Humayun, Ali Anwar, Muhammad Ali Gulzar  

**一句话要点**：提出ProToken方法以解决联邦大语言模型中客户端对生成令牌的贡献溯源问题

**关键词**：联邦学习, 大语言模型, 令牌级溯源, 客户端贡献, 隐私保护, 梯度加权

## 3 点简述
- 核心问题：联邦学习部署大语言模型时，难以确定哪些客户端对特定生成响应有贡献，影响调试、恶意检测和公平奖励分配。
- 方法要点：利用Transformer架构任务信号集中在后层的特点，结合基于梯度的相关性加权，实现令牌级客户端溯源。
- 实验或效果：在四种模型和四个领域共16种配置下测试，平均溯源准确率达98%，且随客户端数量增加保持高精度。

## 摘要（原文）

> Federated Learning (FL) enables collaborative training of Large Language Models (LLMs) across distributed data sources while preserving privacy. However, when federated LLMs are deployed in critical applications, it remains unclear which client(s) contributed to specific generated responses, hindering debugging, malicious client identification, fair reward allocation, and trust verification. We present ProToken, a novel Provenance methodology for Token-level attribution in federated LLMs that addresses client attribution during autoregressive text generation while maintaining FL privacy constraints. ProToken leverages two key insights to enable provenance at each token: (1) transformer architectures concentrate task-specific signals in later blocks, enabling strategic layer selection for computational tractability, and (2) gradient-based relevance weighting filters out irrelevant neural activations, focusing attribution on neurons that directly influence token generation. We evaluate ProToken across 16 configurations spanning four LLM architectures (Gemma, Llama, Qwen, SmolLM) and four domains (medical, financial, mathematical, coding). ProToken achieves 98% average attribution accuracy in correctly localizing responsible client(s), and maintains high accuracy when the number of clients are scaled, validating its practical viability for real-world deployment settings.

