---
layout: default
title: Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs
---

# Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs
**arXiv**：[2602.21198v1](https://arxiv.org/abs/2602.21198) · [PDF](https://arxiv.org/pdf/2602.21198.pdf)  
**作者**：Yining Hong, Huang Huang, Manling Li, Li Fei-Fei, Jiajun Wu, Yejin Choi  

**一句话要点**：提出反射测试时规划方法，以解决具身大语言模型在部署中错误重复而非积累经验的问题。

**关键词**：具身大语言模型, 测试时规划, 反思学习, 长时程任务, 机器人部署, 信用分配

## 3 点简述
- 核心问题：具身大语言模型缺乏反思能力，导致错误在独立试验中重复而非转化为经验积累。
- 方法要点：集成反射中行动和反射后行动两种模式，结合测试时缩放和训练，以及回顾性反思进行长期信用分配。
- 实验或效果：在新设计的长时程家庭基准和MuJoCo橱柜装配基准上显著超越基线模型，并通过消融研究验证反射模式的互补作用。

## 摘要（原文）

> Embodied LLMs endow robots with high-level task reasoning, but they cannot reflect on what went wrong or why, turning deployment into a sequence of independent trials where mistakes repeat rather than accumulate into experience. Drawing upon human reflective practitioners, we introduce Reflective Test-Time Planning, which integrates two modes of reflection: \textit{reflection-in-action}, where the agent uses test-time scaling to generate and score multiple candidate actions using internal reflections before execution; and \textit{reflection-on-action}, which uses test-time training to update both its internal reflection model and its action policy based on external reflections after execution. We also include retrospective reflection, allowing the agent to re-evaluate earlier decisions and perform model updates with hindsight for proper long-horizon credit assignment. Experiments on our newly-designed Long-Horizon Household benchmark and MuJoCo Cupboard Fitting benchmark show significant gains over baseline models, with ablative studies validating the complementary roles of reflection-in-action and reflection-on-action. Qualitative analyses, including real-robot trials, highlight behavioral correction through reflection.

