---
layout: default
title: PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records
---

# PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records
**arXiv**：[2601.09636v1](https://arxiv.org/abs/2601.09636) · [PDF](https://arxiv.org/pdf/2601.09636.pdf)  
**作者**：Yibo Lyu, Gongwei Chen, Rui Shao, Weili Guan, Liqiang Nie  

**一句话要点**：提出PersonalAlign框架，通过分层隐式意图对齐解决个性化GUI代理在模糊指令和主动协助中的挑战。

**关键词**：隐式意图对齐, 个性化GUI代理, 长期用户记录, 分层记忆组织, 主动协助

## 3 点简述
- 核心问题：GUI代理需对齐用户复杂隐式意图，利用长期记录处理模糊指令和预测潜在例行程序。
- 方法要点：引入HIM-Agent，维护持续更新的个人记忆，分层组织用户偏好和例行程序以实现个性化。
- 实验或效果：在AndroidIntent基准上评估，HIM-Agent显著提升执行和主动性能15.7%和7.3%。

## 摘要（原文）

> While GUI agents have shown strong performance under explicit and completion instructions, real-world deployment requires aligning with users' more complex implicit intents. In this work, we highlight Hierarchical Implicit Intent Alignment for Personalized GUI Agent (PersonalAlign), a new agent task that requires agents to leverage long-term user records as persistent context to resolve omitted preferences in vague instructions and anticipate latent routines by user state for proactive assistance. To facilitate this study, we introduce AndroidIntent, a benchmark designed to evaluate agents' ability in resolving vague instructions and providing proactive suggestions through reasoning over long-term user records. We annotated 775 user-specific preferences and 215 routines from 20k long-term records across different users for evaluation. Furthermore, we introduce Hierarchical Intent Memory Agent (HIM-Agent), which maintains a continuously updating personal memory and hierarchically organizes user preferences and routines for personalization. Finally, we evaluate a range of GUI agents on AndroidIntent, including GPT-5, Qwen3-VL, and UI-TARS, further results show that HIM-Agent significantly improves both execution and proactive performance by 15.7% and 7.3%.

