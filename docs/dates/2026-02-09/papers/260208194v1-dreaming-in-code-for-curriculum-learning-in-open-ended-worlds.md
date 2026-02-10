---
layout: default
title: Dreaming in Code for Curriculum Learning in Open-Ended Worlds
---

# Dreaming in Code for Curriculum Learning in Open-Ended Worlds
**arXiv**：[2602.08194v1](https://arxiv.org/abs/2602.08194) · [PDF](https://arxiv.org/pdf/2602.08194.pdf)  
**作者**：Konstantinos Mitsides, Maxence Faldor, Antoine Cully  

**一句话要点**：提出Dreaming in Code框架，通过生成代码级环境变体以解决开放世界中的课程学习难题。

**关键词**：开放世界学习, 课程学习, 代码生成, 环境设计, 长时程技能

## 3 点简述
- 核心问题：开放世界学习面临挑战空间大，难以发现持续可学习的经验序列。
- 方法要点：利用基础模型合成可执行环境代码，构建中间环境以桥接能力差距。
- 实验或效果：在Craftax基准上实现16%平均回报提升，并在后期战斗任务中取得非零成功率。

## 摘要（原文）

> Open-ended learning frames intelligence as emerging from continual interaction with an ever-expanding space of environments. While recent advances have utilized foundation models to programmatically generate diverse environments, these approaches often focus on discovering isolated behaviors rather than orchestrating sustained progression. In complex open-ended worlds, the large combinatorial space of possible challenges makes it difficult for agents to discover sequences of experiences that remain consistently learnable. To address this, we propose Dreaming in Code (DiCode), a framework in which foundation models synthesize executable environment code to scaffold learning toward increasing competence. In DiCode, "dreaming" takes the form of materializing code-level variations of the world. We instantiate DiCode in Craftax, a challenging open-ended benchmark characterized by rich mechanics and long-horizon progression. Empirically, DiCode enables agents to acquire long-horizon skills, achieving a $16\%$ improvement in mean return over the strongest baseline and non-zero success on late-game combat tasks where prior methods fail. Our results suggest that code-level environment design provides a practical mechanism for curriculum control, enabling the construction of intermediate environments that bridge competence gaps in open-ended worlds. Project page and source code are available at https://konstantinosmitsides.github.io/dreaming-in-code and https://github.com/konstantinosmitsides/dreaming-in-code.

