---
layout: default
title: SkillVLA: Tackling Combinatorial Diversity in Dual-Arm Manipulation via Skill Reuse
---

# SkillVLA: Tackling Combinatorial Diversity in Dual-Arm Manipulation via Skill Reuse
**arXiv**：[2603.03836v1](https://arxiv.org/abs/2603.03836) · [PDF](https://arxiv.org/pdf/2603.03836.pdf)  
**作者**：Xuanran Zhai, Zekai Huang, Longyan Wu, Qianyou Zhao, Qiaojun Yu, Jieji Ren, Ce Hao, Harold Soh  

**一句话要点**：提出SkillVLA框架以解决双臂操作中的技能组合多样性问题

**关键词**：双臂操作, 技能重用, 视觉-语言-动作模型, 组合多样性, 机器人学习

## 3 点简述
- 核心问题：现有视觉-语言-动作模型忽视双臂行为组合多样性，阻碍技能重用。
- 方法要点：设计SkillVLA框架，支持单臂技能在新左右配对中重组，避免学习所有组合。
- 实验或效果：实验显示SkillVLA显著提升技能组合成功率，从0%增至51%，并在协作和长时任务中表现优异。

## 摘要（原文）

> Recent progress in vision-language-action (VLA) models has demonstrated strong potential for dual-arm manipulation, enabling complex behaviors and generalization to unseen environments. However, mainstream bimanual VLA formulations largely overlook the critical challenge of combinatorial diversity. Different pairings of single-arm behaviors can induce qualitatively distinct task behaviors, yet existing models do not explicitly account for this structure. We argue that effective bimanual VLAs should support skill reuse - the ability to recombine previously learned single-arm skills across novel left-right pairings - thereby avoiding the need to separately learn every possible combination. Current VLA designs entangle skills across arms, preventing such recomposition and limiting scalability. To address this limitation, we propose SkillVLA, a framework explicitly designed to enable skill reuse in dual-arm manipulation. Extensive experiments demonstrate that SkillVLA substantially improves skill composition, increasing overall success rate from 0% to 51%, and achieves strong performance on cooperative and long-horizon tasks.

