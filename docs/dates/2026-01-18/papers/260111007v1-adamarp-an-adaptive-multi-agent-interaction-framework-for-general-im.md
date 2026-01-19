---
layout: default
title: AdaMARP: An Adaptive Multi-Agent Interaction Framework for General Immersive Role-Playing
---

# AdaMARP: An Adaptive Multi-Agent Interaction Framework for General Immersive Role-Playing
**arXiv**：[2601.11007v1](https://arxiv.org/abs/2601.11007) · [PDF](https://arxiv.org/pdf/2601.11007.pdf)  
**作者**：Zhenhua Xu, Dongsheng Chen, Shuo Wang, Jian Li, Chengjie Wang, Meng Han, Yabiao Wang  

**一句话要点**：提出自适应多智能体角色扮演框架AdaMARP，以增强沉浸式交互叙事中的适应性和沉浸感。

**关键词**：多智能体角色扮演, 沉浸式交互叙事, 自适应框架, 场景管理, LLM训练集, 轨迹评估

## 3 点简述
- 现有LLM角色扮演系统存在沉浸感和适应性不足，难以处理动态环境和多角色编排。
- AdaMARP采用沉浸式消息格式和显式场景管理器，通过离散动作控制角色扮演过程。
- 实验表明，AdaRPSet和AdaSMSet训练集提升角色一致性、环境接地和场景过渡，小模型超越商业LLM。

## 摘要（原文）

> LLM role-playing aims to portray arbitrary characters in interactive narratives, yet existing systems often suffer from limited immersion and adaptability. They typically under-model dynamic environmental information and assume largely static scenes and casts, offering insufficient support for multi-character orchestration, scene transitions, and on-the-fly character introduction. We propose an adaptive multi-agent role-playing framework, AdaMARP, featuring an immersive message format that interleaves [Thought], (Action), <Environment>, and Speech, together with an explicit Scene Manager that governs role-playing through discrete actions (init_scene, pick_speaker, switch_scene, add_role, end) accompanied by rationales. To train these capabilities, we construct AdaRPSet for the Actor Model and AdaSMSet for supervising orchestration decisions, and introduce AdaptiveBench for trajectory-level evaluation. Experiments across multiple backbones and model scales demonstrate consistent improvements: AdaRPSet enhances character consistency, environment grounding, and narrative coherence, with an 8B actor outperforming several commercial LLMs, while AdaSMSet enables smoother scene transitions and more natural role introductions, surpassing Claude Sonnet 4.5 using only a 14B LLM.

