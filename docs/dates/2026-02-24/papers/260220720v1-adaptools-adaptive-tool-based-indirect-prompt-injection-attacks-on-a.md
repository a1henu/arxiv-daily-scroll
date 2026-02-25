---
layout: default
title: AdapTools: Adaptive Tool-based Indirect Prompt Injection Attacks on Agentic LLMs
---

# AdapTools: Adaptive Tool-based Indirect Prompt Injection Attacks on Agentic LLMs
**arXiv**：[2602.20720v1](https://arxiv.org/abs/2602.20720) · [PDF](https://arxiv.org/pdf/2602.20720.pdf)  
**作者**：Che Wang, Jiaming Zhang, Ziqi Zhang, Zijie Wang, Yinghui Wang, Jianbo Gao, Tao Wei, Zhong Chen, Wei Yang Bryan Lim  

**一句话要点**：提出AdapTools自适应工具框架以增强对基于大语言模型的智能代理的间接提示注入攻击评估。

**关键词**：间接提示注入攻击, 自适应攻击框架, 智能代理安全, 工具选择优化, 攻击策略构建

## 3 点简述
- 核心问题：外部数据服务集成引入间接提示注入攻击漏洞，现有方法依赖静态模式且评估不足。
- 方法要点：自适应攻击策略构建和攻击增强，选择隐蔽工具并生成自适应提示以优化攻击。
- 实验或效果：攻击成功率提升2.13倍，系统效用降低1.78倍，对先进防御机制保持有效性。

## 摘要（原文）

> The integration of external data services (e.g., Model Context Protocol, MCP) has made large language model-based agents increasingly powerful for complex task execution. However, this advancement introduces critical security vulnerabilities, particularly indirect prompt injection (IPI) attacks. Existing attack methods are limited by their reliance on static patterns and evaluation on simple language models, failing to address the fast-evolving nature of modern AI agents. We introduce AdapTools, a novel adaptive IPI attack framework that selects stealthier attack tools and generates adaptive attack prompts to create a rigorous security evaluation environment. Our approach comprises two key components: (1) Adaptive Attack Strategy Construction, which develops transferable adversarial strategies for prompt optimization, and (2) Attack Enhancement, which identifies stealthy tools capable of circumventing task-relevance defenses. Comprehensive experimental evaluation shows that AdapTools achieves a 2.13 times improvement in attack success rate while degrading system utility by a factor of 1.78. Notably, the framework maintains its effectiveness even against state-of-the-art defense mechanisms. Our method advances the understanding of IPI attacks and provides a useful reference for future research.

