---
layout: default
title: SkillOrchestra: Learning to Route Agents via Skill Transfer
---

# SkillOrchestra: Learning to Route Agents via Skill Transfer
**arXiv**：[2602.19672v1](https://arxiv.org/abs/2602.19672) · [PDF](https://arxiv.org/pdf/2602.19672.pdf)  
**作者**：Jiayu Wang, Yifei Ming, Zixuan Ke, Shafiq Joty, Aws Albarghouthi, Frederic Sala  

**一句话要点**：提出SkillOrchestra框架，通过技能建模实现高效多智能体路由，解决现有路由方法在细粒度决策和适应性上的不足。

**关键词**：复合AI系统, 智能体路由, 技能建模, 性能-成本权衡, 样本高效学习, 可解释性

## 3 点简述
- 现有路由方法面临粗粒度决策和路由崩溃问题，限制复合AI系统性能。
- SkillOrchestra学习细粒度技能并建模智能体能力与成本，实现基于技能需求的动态路由。
- 在十个基准测试中，性能提升达22.5%，学习成本降低数百倍，验证了方法的有效性和高效性。

## 摘要（原文）

> Compound AI systems promise capabilities beyond those of individual models, yet their success depends critically on effective orchestration. Existing routing approaches face two limitations: (1) input-level routers make coarse query-level decisions that ignore evolving task requirements; (2) RL-trained orchestrators are expensive to adapt and often suffer from routing collapse, repeatedly invoking one strong but costly option in multi-turn scenarios. We introduce SkillOrchestra, a framework for skill-aware orchestration. Instead of directly learning a routing policy end-to-end, SkillOrchestra learns fine-grained skills from execution experience and models agent-specific competence and cost under those skills. At deployment, the orchestrator infers the skill demands of the current interaction and selects agents that best satisfy them under an explicit performance-cost trade-off. Extensive experiments across ten benchmarks demonstrate that SkillOrchestra outperforms SoTA RL-based orchestrators by up to 22.5% with 700x and 300x learning cost reduction compared to Router-R1 and ToolOrchestra, respectively. These results show that explicit skill modeling enables scalable, interpretable, and sample-efficient orchestration, offering a principled alternative to data-intensive RL-based approaches. The code is available at: https://github.com/jiayuww/SkillOrchestra.

