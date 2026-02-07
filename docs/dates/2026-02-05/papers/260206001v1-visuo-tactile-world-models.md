---
layout: default
title: Visuo-Tactile World Models
---

# Visuo-Tactile World Models
**arXiv**：[2602.06001v1](https://arxiv.org/abs/2602.06001) · [PDF](https://arxiv.org/pdf/2602.06001.pdf)  
**作者**：Carolina Higuera, Sergio Arnaud, Byron Boots, Mustafa Mukadam, Francois Robert Hogan, Franziska Meier  

**一句话要点**：提出多任务视觉-触觉世界模型以增强接触丰富任务中的物理推理能力

**关键词**：视觉-触觉融合, 世界模型, 接触物理推理, 机器人操作, 多任务学习, 零样本迁移

## 3 点简述
- 核心问题：仅视觉模型在遮挡或模糊接触状态下易出现物体消失、瞬移或违反物理规律等失败模式
- 方法要点：通过结合视觉与触觉感知，捕捉接触物理，提升机器人-物体交互的理解
- 实验或效果：在自回归推演中，物体持久性提升33%，运动规律符合度提升29%；零样本真实机器人实验成功率最高提升35%

## 摘要（原文）

> We introduce multi-task Visuo-Tactile World Models (VT-WM), which capture the physics of contact through touch reasoning. By complementing vision with tactile sensing, VT-WM better understands robot-object interactions in contact-rich tasks, avoiding common failure modes of vision-only models under occlusion or ambiguous contact states, such as objects disappearing, teleporting, or moving in ways that violate basic physics. Trained across a set of contact-rich manipulation tasks, VT-WM improves physical fidelity in imagination, achieving 33% better performance at maintaining object permanence and 29% better compliance with the laws of motion in autoregressive rollouts. Moreover, experiments show that grounding in contact dynamics also translates to planning. In zero-shot real-robot experiments, VT-WM achieves up to 35% higher success rates, with the largest gains in multi-step, contact-rich tasks. Finally, VT-WM demonstrates significant downstream versatility, effectively adapting its learned contact dynamics to a novel task and achieving reliable planning success with only a limited set of demonstrations.

