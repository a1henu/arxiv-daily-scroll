---
layout: default
title: Learning to Inject: Automated Prompt Injection via Reinforcement Learning
---

# Learning to Inject: Automated Prompt Injection via Reinforcement Learning
**arXiv**：[2602.05746v1](https://arxiv.org/abs/2602.05746) · [PDF](https://arxiv.org/pdf/2602.05746.pdf)  
**作者**：Xin Chen, Jie Zhang, Florian Tramer  

**一句话要点**：提出AutoInject强化学习框架，自动生成通用对抗后缀以优化LLM代理的提示注入攻击。

**关键词**：提示注入, 强化学习, 对抗攻击, LLM代理, 自动化优化

## 3 点简述
- 核心问题：LLM代理的提示注入漏洞缺乏自动化攻击方法，依赖人工限制可扩展性。
- 方法要点：使用强化学习框架生成通用对抗后缀，联合优化攻击成功率和良性任务效用。
- 实验或效果：在AgentDojo基准上成功攻击GPT 5 Nano等前沿系统，建立自动化提示注入基线。

## 摘要（原文）

> Prompt injection is one of the most critical vulnerabilities in LLM agents; yet, effective automated attacks remain largely unexplored from an optimization perspective. Existing methods heavily depend on human red-teamers and hand-crafted prompts, limiting their scalability and adaptability. We propose AutoInject, a reinforcement learning framework that generates universal, transferable adversarial suffixes while jointly optimizing for attack success and utility preservation on benign tasks. Our black-box method supports both query-based optimization and transfer attacks to unseen models and tasks. Using only a 1.5B parameter adversarial suffix generator, we successfully compromise frontier systems including GPT 5 Nano, Claude Sonnet 3.5, and Gemini 2.5 Flash on the AgentDojo benchmark, establishing a stronger baseline for automated prompt injection research.

