---
layout: default
title: PACE: A Personalized Adaptive Curriculum Engine for 9-1-1 Call-taker Training
---

# PACE: A Personalized Adaptive Curriculum Engine for 9-1-1 Call-taker Training
**arXiv**：[2603.05361v1](https://arxiv.org/abs/2603.05361) · [PDF](https://arxiv.org/pdf/2603.05361.pdf)  
**作者**：Zirong Chen, Hongchao Zhang, Meiyi Ma  

**一句话要点**：提出PACE个性化自适应课程引擎，以解决911接线员培训中技能复杂且个性化教学难以规模化的问题。

**关键词**：个性化学习, 自适应课程, 技能建模, 情境老虎机, 培训系统, 紧急通信

## 3 点简述
- 核心问题：911接线员培训需掌握上千项技能，但劳动力短缺和个性化教学负担限制了培训效率。
- 方法要点：PACE通过概率技能状态建模、学习遗忘动态建模和基于情境老虎机的场景推荐，辅助培训师决策。
- 实验或效果：实证显示PACE提升19.50%能力达成速度、10.95%最终掌握度，并与专家判断95.45%对齐。

## 摘要（原文）

> 9-1-1 call-taking training requires mastery of over a thousand interdependent skills, covering diverse incident types and protocol-specific nuances. A nationwide labor shortage is already straining training capacity, but effective instruction still demands that trainers tailor objectives to each trainee's evolving competencies. This personalization burden is one that current practice cannot scale. Partnering with Metro Nashville Department of Emergency Communications (MNDEC), we propose PACE (Personalized Adaptive Curriculum Engine), a co-pilot system that augments trainer decision-making by (1) maintaining probabilistic beliefs over trainee skill states, (2) modeling individual learning and forgetting dynamics, and (3) recommending training scenarios that balance acquisition of new competencies with retention of existing ones. PACE propagates evidence over a structured skill graph to accelerate diagnostic coverage and applies contextual bandits to select scenarios that target gaps the trainee is prepared to address. Empirical results show that PACE achieves 19.50% faster time-to-competence and 10.95% higher terminal mastery compared to state-of-the-art frameworks. Co-pilot studies with practicing training officers further demonstrate a 95.45% alignment rate between PACE's and experts' pedagogical judgments on real-world cases. Under estimation, PACE cuts turnaround time to merely 34 seconds from 11.58 minutes, up to 95.08% reduction.

