---
layout: default
title: On Safer Reinforcement Learning Policies for Sedation and Analgesia in Intensive Care
---

# On Safer Reinforcement Learning Policies for Sedation and Analgesia in Intensive Care
**arXiv**：[2601.23154v1](https://arxiv.org/abs/2601.23154) · [PDF](https://arxiv.org/pdf/2601.23154.pdf)  
**作者**：Joel Romero-Hernandez, Oscar Camara  

**一句话要点**：提出基于强化学习的ICU镇静镇痛策略，通过优化长期生存目标提升治疗安全性

**关键词**：强化学习, ICU镇静镇痛, 部分可观测性, 药物剂量策略, 患者安全, MIMIC-IV数据库

## 3 点简述
- 核心问题：ICU疼痛管理中治疗不足或过度均可能导致严重后遗症，现有方法忽视患者生存目标。
- 方法要点：在部分可观测环境下，使用深度强化学习框架学习每小时药物剂量策略，优化疼痛减少或联合减少疼痛与死亡率。
- 实验或效果：基于MIMIC-IV数据库数据训练，发现仅优化疼痛的策略与死亡率正相关，而联合优化策略与死亡率负相关。

## 摘要（原文）

> Pain management in intensive care usually involves complex trade-offs between therapeutic goals and patient safety, since both inadequate and excessive treatment may induce serious sequelae. Reinforcement learning can help address this challenge by learning medication dosing policies from retrospective data. However, prior work on sedation and analgesia has optimized for objectives that do not value patient survival while relying on algorithms unsuitable for imperfect information settings. We investigated the risks of these design choices by implementing a deep reinforcement learning framework to suggest hourly medication doses under partial observability. Using data from 47,144 ICU stays in the MIMIC-IV database, we trained policies to prescribe opioids, propofol, benzodiazepines, and dexmedetomidine according to two goals: reduce pain or jointly reduce pain and mortality. We found that, although the two policies were associated with lower pain, actions from the first policy were positively correlated with mortality, while those proposed by the second policy were negatively correlated. This suggests that valuing long-term outcomes could be critical for safer treatment policies, even if a short-term goal remains the primary objective.

