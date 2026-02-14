---
layout: default
title: Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation
---

# Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation
**arXiv**：[2602.12125v1](https://arxiv.org/abs/2602.12125) · [PDF](https://arxiv.org/pdf/2602.12125.pdf)  
**作者**：Wenkai Yang, Weijie Liu, Ruobing Xie, Kai Yang, Saiyong Yang, Yankai Lin  

**一句话要点**：提出广义策略蒸馏框架，通过奖励外推提升学生模型性能

**关键词**：策略蒸馏, 强化学习, 模型蒸馏, 奖励外推, 数学推理, 代码生成

## 3 点简述
- 理论证明策略蒸馏是密集KL约束强化学习的特例
- 引入灵活参考模型和奖励缩放因子扩展标准目标
- 实验显示奖励外推能超越教师性能边界

## 摘要（原文）

> On-policy distillation (OPD), which aligns the student with the teacher's logit distribution on student-generated trajectories, has demonstrated strong empirical gains in improving student performance and often outperforms off-policy distillation and reinforcement learning (RL) paradigms. In this work, we first theoretically show that OPD is a special case of dense KL-constrained RL where the reward function and the KL regularization are always weighted equally and the reference model can by any model. Then, we propose the Generalized On-Policy Distillation (G-OPD) framework, which extends the standard OPD objective by introducing a flexible reference model and a reward scaling factor that controls the relative weight of the reward term against the KL regularization. Through comprehensive experiments on math reasoning and code generation tasks, we derive two novel insights: (1) Setting the reward scaling factor to be greater than 1 (i.e., reward extrapolation), which we term ExOPD, consistently improves over standard OPD across a range of teacher-student size pairings. In particular, in the setting where we merge the knowledge from different domain experts, obtained by applying domain-specific RL to the same student model, back into the original student, ExOPD enables the student to even surpass the teacher's performance boundary and outperform the domain teachers. (2) Building on ExOPD, we further find that in the strong-to-weak distillation setting (i.e., distilling a smaller student from a larger teacher), performing reward correction by choosing the reference model as the teacher's base model before RL yields a more accurate reward signal and further improves distillation performance. However, this choice assumes access to the teacher's pre-RL variant and incurs more computational overhead. We hope our work offers new insights for future research on OPD.

