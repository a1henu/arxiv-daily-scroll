---
layout: default
title: When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent
---

# When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent
**arXiv**：[2601.07263v1](https://arxiv.org/abs/2601.07263) · [PDF](https://arxiv.org/pdf/2601.07263.pdf)  
**作者**：Xinyi Wu, Geng Hong, Yueyue Chen, MingXuan Liu, Feier Jin, Xudong Pan, Jiarun Dai, Baojun Liu  

**一句话要点**：提出AgentBait攻击范式与SUPERVISOR防御模块，以应对Web自动化代理中的社会工程攻击风险。

**关键词**：Web自动化代理, 社会工程攻击, AgentBait攻击, SUPERVISOR防御, 运行时安全, 意图一致性

## 3 点简述
- 核心问题：Web自动化代理易受社会工程攻击，现有研究多关注模型威胁，此风险未充分探索。
- 方法要点：设计AgentBait攻击范式利用代理执行弱点，提出SUPERVISOR运行时模块进行环境和意图一致性对齐。
- 实验或效果：主流框架攻击成功率平均67.5%，SUPERVISOR可降低成功率达78.1%，运行时开销仅7.7%。

## 摘要（原文）

> Web agents, powered by large language models (LLMs), are increasingly deployed to automate complex web interactions. The rise of open-source frameworks (e.g., Browser Use, Skyvern-AI) has accelerated adoption, but also broadened the attack surface. While prior research has focused on model threats such as prompt injection and backdoors, the risks of social engineering remain largely unexplored. We present the first systematic study of social engineering attacks against web automation agents and design a pluggable runtime mitigation solution. On the attack side, we introduce the AgentBait paradigm, which exploits intrinsic weaknesses in agent execution: inducement contexts can distort the agent's reasoning and steer it toward malicious objectives misaligned with the intended task. On the defense side, we propose SUPERVISOR, a lightweight runtime module that enforces environment and intention consistency alignment between webpage context and intended goals to mitigate unsafe operations before execution.
>   Empirical results show that mainstream frameworks are highly vulnerable to AgentBait, with an average attack success rate of 67.5% and peaks above 80% under specific strategies (e.g., trusted identity forgery). Compared with existing lightweight defenses, our module can be seamlessly integrated across different web automation frameworks and reduces attack success rates by up to 78.1% on average while incurring only a 7.7% runtime overhead and preserving usability. This work reveals AgentBait as a critical new threat surface for web agents and establishes a practical, generalizable defense, advancing the security of this rapidly emerging ecosystem. We reported the details of this attack to the framework developers and received acknowledgment before submission.

