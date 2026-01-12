---
layout: default
title: DynaDebate: Breaking Homogeneity in Multi-Agent Debate with Dynamic Path Generation
---

# DynaDebate: Breaking Homogeneity in Multi-Agent Debate with Dynamic Path Generation
**arXiv**：[2601.05746v1](https://arxiv.org/abs/2601.05746) · [PDF](https://arxiv.org/pdf/2601.05746.pdf)  
**作者**：Zhenghao Li, Zhi Zheng, Wei Chen, Jielun Zhao, Yong Chen, Tong Xu, Enhong Chen  

**一句话要点**：提出DynaDebate框架以解决多智能体辩论中因同质化推理导致的错误传播问题

**关键词**：多智能体辩论, 动态路径生成, 过程中心辩论, 触发式验证, 大型语言模型系统

## 3 点简述
- 核心问题：现有多智能体辩论方法因无引导初始化导致智能体推理路径同质化，阻碍有效辩论，常退化为简单多数投票
- 方法要点：通过动态路径生成与分配、过程中心辩论和触发式验证代理，增强辩论多样性与逻辑严谨性
- 实验或效果：在多个基准测试中表现优异，超越现有最先进的多智能体辩论方法

## 摘要（原文）

> Recent years have witnessed the rapid development of Large Language Model-based Multi-Agent Systems (MAS), which excel at collaborative decision-making and complex problem-solving. Recently, researchers have further investigated Multi-Agent Debate (MAD) frameworks, which enhance the reasoning and collaboration capabilities of MAS through information exchange and debate among multiple agents. However, existing approaches often rely on unguided initialization, causing agents to adopt identical reasoning paths that lead to the same errors. As a result, effective debate among agents is hindered, and the final outcome frequently degenerates into simple majority voting. To solve the above problem, in this paper, we introduce Dynamic Multi-Agent Debate (DynaDebate), which enhances the effectiveness of multi-agent debate through three key mechanisms: (1) Dynamic Path Generation and Allocation, which employs a dedicated Path Generation Agent to generate diverse and logical solution paths with adaptive redundancy; (2) Process-Centric Debate, which shifts the focus from surface-level outcome voting to rigorous step-by-step logic critique to ensure process correctness; (3) A Trigger-Based Verification Agent, which is activated upon disagreement and uses external tools to objectively resolve deadlocks. Extensive experiments demonstrate that DynaDebate achieves superior performance across various benchmarks, surpassing existing state-of-the-art MAD methods.

