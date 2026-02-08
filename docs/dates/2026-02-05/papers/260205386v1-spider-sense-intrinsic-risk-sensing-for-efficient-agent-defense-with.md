---
layout: default
title: Spider-Sense: Intrinsic Risk Sensing for Efficient Agent Defense with Hierarchical Adaptive Screening
---

# Spider-Sense: Intrinsic Risk Sensing for Efficient Agent Defense with Hierarchical Adaptive Screening
**arXiv**：[2602.05386v1](https://arxiv.org/abs/2602.05386) · [PDF](https://arxiv.org/pdf/2602.05386.pdf)  
**作者**：Zhenxiong Yu, Zhi Yang, Zhiheng Jin, Shuhe Wang, Heng Zhang, Yanlin Fei, Lingfeng Zeng, Fangqi Lou, Shuo Zhang, Tu Hu, Jingping Liu, Rongze Chen, Xingyu Zhu, Kunyi Wang, Chaofa Yuan, Xin Guo, Zhaowei Liu, Feipeng Zhang, Jie Huang, Huacan Wang, Ronghao Chen, Liwen Zhang  

**一句话要点**：提出Spider-Sense框架，基于内在风险感知实现高效自主代理防御

**关键词**：自主代理安全, 内在风险感知, 分层防御机制, 事件驱动框架, 基准评估

## 3 点简述
- 核心问题：现有代理防御机制多为强制检查，效率低且与架构解耦，难以适应动态安全挑战。
- 方法要点：引入事件驱动的内在风险感知，仅在感知风险时触发分层防御，结合轻量匹配与深度推理。
- 实验或效果：在S$^2$Bench基准上，Spider-Sense实现最低攻击成功率与误报率，延迟开销仅8.3%。

## 摘要（原文）

> As large language models (LLMs) evolve into autonomous agents, their real-world applicability has expanded significantly, accompanied by new security challenges. Most existing agent defense mechanisms adopt a mandatory checking paradigm, in which security validation is forcibly triggered at predefined stages of the agent lifecycle. In this work, we argue that effective agent security should be intrinsic and selective rather than architecturally decoupled and mandatory. We propose Spider-Sense framework, an event-driven defense framework based on Intrinsic Risk Sensing (IRS), which allows agents to maintain latent vigilance and trigger defenses only upon risk perception. Once triggered, the Spider-Sense invokes a hierarchical defence mechanism that trades off efficiency and precision: it resolves known patterns via lightweight similarity matching while escalating ambiguous cases to deep internal reasoning, thereby eliminating reliance on external models. To facilitate rigorous evaluation, we introduce S$^2$Bench, a lifecycle-aware benchmark featuring realistic tool execution and multi-stage attacks. Extensive experiments demonstrate that Spider-Sense achieves competitive or superior defense performance, attaining the lowest Attack Success Rate (ASR) and False Positive Rate (FPR), with only a marginal latency overhead of 8.3\%.

