---
layout: default
title: CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning
---

# CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning
**arXiv**：[2602.12532v1](https://arxiv.org/abs/2602.12532) · [PDF](https://arxiv.org/pdf/2602.12532.pdf)  
**作者**：Yike Zhang, Yaonan Wang, Xinxin Sun, Kaizhen Huang, Zhiyuan Xu, Junjie Ji, Zhengping Che, Jian Tang, Jingtao Sun  

**一句话要点**：提出CRAFT框架，通过力感知课程微调解决VLA模型在接触丰富操作任务中的性能问题

**关键词**：接触丰富操作, 力感知学习, 课程微调, 变分信息瓶颈, 视觉语言动作模型, 机器人操作

## 3 点简述
- 核心问题：VLA模型在接触丰富操作中因视觉语言高熵与力信号低熵不平衡导致过度依赖感知和不稳定控制
- 方法要点：引入变分信息瓶颈模块，采用力感知课程微调策略，优先学习力信号后逐步恢复多模态信息
- 实验或效果：在真实世界实验中提升任务成功率，泛化至未见对象和新任务变体，适应多种VLA架构

## 摘要（原文）

> Vision-Language-Action (VLA) models have shown a strong capability in enabling robots to execute general instructions, yet they struggle with contact-rich manipulation tasks, where success requires precise alignment, stable contact maintenance, and effective handling of deformable objects. A fundamental challenge arises from the imbalance between high-entropy vision and language inputs and low-entropy but critical force signals, which often leads to over-reliance on perception and unstable control. To address this, we introduce CRAFT, a force-aware curriculum fine-tuning framework that integrates a variational information bottleneck module to regulate vision and language embeddings during early training. This curriculum strategy encourages the model to prioritize force signals initially, before progressively restoring access to the full multimodal information. To enable force-aware learning, we further design a homologous leader-follower teleoperation system that collects synchronized vision, language, and force data across diverse contact-rich tasks. Real-world experiments demonstrate that CRAFT consistently improves task success, generalizes to unseen objects and novel task variations, and adapts effectively across diverse VLA architectures, enabling robust and generalizable contact-rich manipulation.

