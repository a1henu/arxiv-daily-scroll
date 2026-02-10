---
layout: default
title: SoK: The Pitfalls of Deep Reinforcement Learning for Cybersecurity
---

# SoK: The Pitfalls of Deep Reinforcement Learning for Cybersecurity
**arXiv**：[2602.08690v1](https://arxiv.org/abs/2602.08690) · [PDF](https://arxiv.org/pdf/2602.08690.pdf)  
**作者**：Shae McFadden, Myles Foley, Elizabeth Bates, Ilias Tsingenopoulos, Sanyam Vyas, Vasilios Mavroudis, Chris Hicks, Fabio Pierazzi  

**一句话要点**：系统化分析深度强化学习在网络安全应用中的11个常见陷阱并提出改进建议

**关键词**：深度强化学习, 网络安全, 方法论陷阱, 环境建模, 性能评估, 系统部署

## 3 点简述
- 核心问题：深度强化学习从实验室模拟迁移到定制网络安全环境时易引入问题，且任务常具对抗性、非平稳性和部分可观测性
- 方法要点：通过分析66篇论文（2018-2025），量化了环境建模、代理训练、性能评估和系统部署阶段的陷阱普遍性
- 实验或效果：在自主网络防御、对抗性恶意软件生成和Web安全测试环境中进行控制实验，展示陷阱的实际影响

## 摘要（原文）

> Deep Reinforcement Learning (DRL) has achieved remarkable success in domains requiring sequential decision-making, motivating its application to cybersecurity problems. However, transitioning DRL from laboratory simulations to bespoke cyber environments can introduce numerous issues. This is further exacerbated by the often adversarial, non-stationary, and partially-observable nature of most cybersecurity tasks. In this paper, we identify and systematize 11 methodological pitfalls that frequently occur in DRL for cybersecurity (DRL4Sec) literature across the stages of environment modeling, agent training, performance evaluation, and system deployment. By analyzing 66 significant DRL4Sec papers (2018-2025), we quantify the prevalence of each pitfall and find an average of over five pitfalls per paper. We demonstrate the practical impact of these pitfalls using controlled experiments in (i) autonomous cyber defense, (ii) adversarial malware creation, and (iii) web security testing environments. Finally, we provide actionable recommendations for each pitfall to support the development of more rigorous and deployable DRL-based security systems.

