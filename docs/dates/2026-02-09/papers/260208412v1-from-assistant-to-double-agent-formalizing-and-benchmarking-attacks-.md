---
layout: default
title: From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent
---

# From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent
**arXiv**：[2602.08412v1](https://arxiv.org/abs/2602.08412) · [PDF](https://arxiv.org/pdf/2602.08412.pdf)  
**作者**：Yuhang Wang, Feiming Xu, Zheng Lin, Guangyu He, Yuzhe Huang, Haichang Gao, Zhenxing Niu  

**一句话要点**：提出PASB框架以评估个性化AI代理在真实部署中的安全风险

**关键词**：个性化AI代理, 安全评估框架, 黑盒攻击, 端到端测试, 工具链安全, 风险传播

## 3 点简述
- 核心问题：现有安全评估框架未能准确捕捉个性化代理在真实场景中的攻击面和风险传播机制
- 方法要点：构建PASB框架，集成个性化场景、真实工具链和长时交互，支持黑盒端到端安全评估
- 实验或效果：以OpenClaw为例，系统评估其在多场景下的漏洞，揭示用户提示处理、工具使用和记忆检索等阶段的关键风险

## 摘要（原文）

> Although large language model (LLM)-based agents, exemplified by OpenClaw, are increasingly evolving from task-oriented systems into personalized AI assistants for solving complex real-world tasks, their practical deployment also introduces severe security risks. However, existing agent security research and evaluation frameworks primarily focus on synthetic or task-centric settings, and thus fail to accurately capture the attack surface and risk propagation mechanisms of personalized agents in real-world deployments. To address this gap, we propose Personalized Agent Security Bench (PASB), an end-to-end security evaluation framework tailored for real-world personalized agents. Building upon existing agent attack paradigms, PASB incorporates personalized usage scenarios, realistic toolchains, and long-horizon interactions, enabling black-box, end-to-end security evaluation on real systems. Using OpenClaw as a representative case study, we systematically evaluate its security across multiple personalized scenarios, tool capabilities, and attack types. Our results indicate that OpenClaw exhibits critical vulnerabilities at different execution stages, including user prompt processing, tool usage, and memory retrieval, highlighting substantial security risks in personalized agent deployments. The code for the proposed PASB framework is available at https://github.com/AstorYH/PASB.

