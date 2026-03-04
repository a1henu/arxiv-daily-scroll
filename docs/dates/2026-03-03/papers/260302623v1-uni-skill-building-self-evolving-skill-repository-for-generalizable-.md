---
layout: default
title: Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation
---

# Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation
**arXiv**：[2603.02623v1](https://arxiv.org/abs/2603.02623) · [PDF](https://arxiv.org/pdf/2603.02623.pdf)  
**作者**：Senwei Xie, Yuntian Zhang, Ruiping Wang, Xilin Chen  

**一句话要点**：提出Uni-Skill框架以解决机器人操作中技能库固定导致泛化能力受限的问题

**关键词**：机器人操作, 技能演化, 分层技能分类, 零样本泛化, 离线检索

## 3 点简述
- 核心问题：现有技能中心方法依赖固定技能库，难以适应新任务，需手动干预
- 方法要点：构建SkillFolder技能库，支持分层技能分类和自动技能演化，实现离线检索和少样本推理
- 实验或效果：在仿真和真实环境中验证了优于现有VLM方法的性能，具备零样本泛化能力

## 摘要（原文）

> While skill-centric approaches leverage foundation models to enhance generalization in compositional tasks, they often rely on fixed skill libraries, limiting adaptability to new tasks without manual intervention. To address this, we propose Uni-Skill, a Unified Skill-centric framework that supports skill-aware planning and facilitates automatic skill evolution. Unlike prior methods that restrict planning to predefined skills, Uni-Skill requests for new skill implementations when existing ones are insufficient, ensuring adaptable planning with self-augmented skill library. To support automatic implementation of diverse skills requested by the planning module, we construct SkillFolder, a VerbNet-inspired repository derived from large-scale unstructured robotic videos. SkillFolder introduces a hierarchical skill taxonomy that captures diverse skill descriptions at multiple levels of abstraction. By populating this taxonomy with large-scale, automatically annotated demonstrations, Uni-Skill shifts the paradigm of skill acquisition from inefficient manual annotation to efficient offline structural retrieval. Retrieved examples provide semantic supervision over behavior patterns and fine-grained references for spatial trajectories, enabling few-shot skill inference without deployment-time demonstrations. Comprehensive experiments in both simulation and real-world settings verify the state-of-the-art performance of Uni-Skill over existing VLM-based skill-centric approaches, highlighting its advanced reasoning capabilities and strong zero-shot generalization across a wide range of novel tasks.

