---
layout: default
title: LLM-assisted Semantic Option Discovery for Facilitating Adaptive Deep Reinforcement Learning
---

# LLM-assisted Semantic Option Discovery for Facilitating Adaptive Deep Reinforcement Learning
**arXiv**：[2603.01488v1](https://arxiv.org/abs/2603.01488) · [PDF](https://arxiv.org/pdf/2603.01488.pdf)  
**作者**：Chang Yao, Jinghui Qin, Kebing Jin, Hankz Hankui Zhuo  

**一句话要点**：提出LLM驱动的闭环框架，通过语义选项发现促进自适应深度强化学习

**关键词**：深度强化学习, 大语言模型, 语义选项发现, 自适应学习, 可解释性, 跨环境迁移

## 3 点简述
- 核心问题：深度强化学习在数据效率、可解释性和跨环境迁移性方面存在不足，策略对环境变化敏感。
- 方法要点：利用大语言模型将自然语言指令映射为可执行规则，自动创建语义标注选项，实现技能重用和实时约束监控。
- 实验或效果：在Office World和Montezuma's Revenge实验中，框架在数据效率、约束合规性和跨任务迁移性上表现优异。

## 摘要（原文）

> Despite achieving remarkable success in complex tasks, Deep Reinforcement Learning (DRL) is still suffering from critical issues in practical applications, such as low data efficiency, lack of interpretability, and limited cross-environment transferability. However, the learned policy generating actions based on states are sensitive to the environmental changes, struggling to guarantee behavioral safety and compliance. Recent research shows that integrating Large Language Models (LLMs) with symbolic planning is promising in addressing these challenges. Inspired by this, we introduce a novel LLM-driven closed-loop framework, which enables semantic-driven skill reuse and real-time constraint monitoring by mapping natural language instructions into executable rules and semantically annotating automatically created options. The proposed approach utilizes the general knowledge of LLMs to facilitate exploration efficiency and adapt to transferable options for similar environments, and provides inherent interpretability through semantic annotations. To validate the effectiveness of this framework, we conduct experiments on two domains, Office World and Montezuma's Revenge, respectively. The results demonstrate superior performance in data efficiency, constraint compliance, and cross-task transferability.

