---
layout: default
title: MM-tau-p$^2$: Persona-Adaptive Prompting for Robust Multi-Modal Agent Evaluation in Dual-Control Settings
---

# MM-tau-p$^2$: Persona-Adaptive Prompting for Robust Multi-Modal Agent Evaluation in Dual-Control Settings
**arXiv**：[2603.09643v1](https://arxiv.org/abs/2603.09643) · [PDF](https://arxiv.org/pdf/2603.09643.pdf)  
**作者**：Anupam Purwar, Aditya Choudhary  

**一句话要点**：提出MM-tau-p²基准以评估多模态代理在双控制设置中的鲁棒性，支持用户角色自适应。

**关键词**：多模态代理评估, 用户角色自适应, 双控制设置, 鲁棒性指标, LLM-as-judge, 客户体验管理

## 3 点简述
- 当前评估框架忽略用户角色，无法适应客户体验管理中的个性化需求。
- 引入12个新指标，在双控制设置中评估多模态代理的鲁棒性和开销。
- 在电信和零售领域使用LLM-as-judge方法提供指标估计，验证基准实用性。

## 摘要（原文）

> Current evaluation frameworks and benchmarks for LLM powered agents focus on text chat driven agents, these frameworks do not expose the persona of user to the agent, thus operating in a user agnostic environment. Importantly, in customer experience management domain, the agent's behaviour evolves as the agent learns about user personality. With proliferation of real time TTS and multi-modal language models, LLM based agents are gradually going to become multi-modal. Towards this, we propose the MM-tau-p$^2$ benchmark with metrics for evaluating the robustness of multi-modal agents in dual control setting with and without persona adaption of user, while also taking user inputs in the planning process to resolve a user query. In particular, our work shows that even with state of-the-art frontier LLMs like GPT-5, GPT 4.1, there are additional considerations measured using metrics viz. multi-modal robustness, turn overhead while introducing multi-modality into LLM based agents. Overall, MM-tau-p$^2$ builds on our prior work FOCAL and provides a holistic way of evaluating multi-modal agents in an automated way by introducing 12 novel metrics. We also provide estimates of these metrics on the telecom and retail domains by using the LLM-as-judge approach using carefully crafted prompts with well defined rubrics for evaluating each conversation.

