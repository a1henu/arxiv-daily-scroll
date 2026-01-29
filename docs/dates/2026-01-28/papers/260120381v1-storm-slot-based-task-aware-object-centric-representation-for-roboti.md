---
layout: default
title: STORM: Slot-based Task-aware Object-centric Representation for robotic Manipulation
---

# STORM: Slot-based Task-aware Object-centric Representation for robotic Manipulation
**arXiv**：[2601.20381v1](https://arxiv.org/abs/2601.20381) · [PDF](https://arxiv.org/pdf/2601.20381.pdf)  
**作者**：Alexandre Chapin, Emmanuel Dellandréa, Liming Chen  

**一句话要点**：提出STORM模块，通过槽位化任务感知对象中心表示增强视觉基础模型，以提升机器人操作的鲁棒性。

**关键词**：机器人操作, 对象中心表示, 视觉基础模型, 槽位学习, 多阶段训练, 语义感知

## 3 点简述
- 视觉基础模型的密集表示缺乏对象级结构，限制机器人操作的鲁棒性和可收缩性。
- STORM采用多阶段训练策略：先通过视觉-语义预训练稳定对象中心槽位，再与下游策略联合适应。
- 实验显示STORM在对象发现和模拟操作任务中优于直接使用基础模型特征或端到端训练方法。

## 摘要（原文）

> Visual foundation models provide strong perceptual features for robotics, but their dense representations lack explicit object-level structure, limiting robustness and contractility in manipulation tasks. We propose STORM (Slot-based Task-aware Object-centric Representation for robotic Manipulation), a lightweight object-centric adaptation module that augments frozen visual foundation models with a small set of semantic-aware slots for robotic manipulation. Rather than retraining large backbones, STORM employs a multi-phase training strategy: object-centric slots are first stabilized through visual--semantic pretraining using language embeddings, then jointly adapted with a downstream manipulation policy. This staged learning prevents degenerate slot formation and preserves semantic consistency while aligning perception with task objectives. Experiments on object discovery benchmarks and simulated manipulation tasks show that STORM improves generalization to visual distractors, and control performance compared to directly using frozen foundation model features or training object-centric representations end-to-end. Our results highlight multi-phase adaptation as an efficient mechanism for transforming generic foundation model features into task-aware object-centric representations for robotic control.

