---
layout: default
title: Lifelong Language-Conditioned Robotic Manipulation Learning
---

# Lifelong Language-Conditioned Robotic Manipulation Learning
**arXiv**：[2603.05160v1](https://arxiv.org/abs/2603.05160) · [PDF](https://arxiv.org/pdf/2603.05160.pdf)  
**作者**：Xudong Wang, Zebin Han, Zhiyu Liu, Gan Li, Jiahua Dong, Baichen Liu, Lianqing Liu, Zhi Han  

**一句话要点**：提出SkillsCrafter框架以解决机器人操作中语言条件技能持续学习的灾难性遗忘问题

**关键词**：机器人操作学习, 语言条件控制, 持续学习, 灾难性遗忘, 技能语义子空间, 技能聚合

## 3 点简述
- 核心问题：传统语言条件操作代理在顺序学习新技能时易遗忘旧技能，限制动态场景部署。
- 方法要点：通过操作技能适应保留旧技能知识，并利用奇异值分解获取技能语义子空间以记录本质语义。
- 实验或效果：广泛实验验证SkillsCrafter在减少遗忘和提升泛化方面的有效性和优越性。

## 摘要（原文）

> Traditional language-conditioned manipulation agent sequential adaptation to new manipulation skills leads to catastrophic forgetting of old skills, limiting dynamic scene practical deployment. In this paper, we propose SkillsCrafter, a novel robotic manipulation framework designed to continually learn multiple skills while reducing catastrophic forgetting of old skills. Specifically, we propose a Manipulation Skills Adaptation to retain the old skills knowledge while inheriting the shared knowledge between new and old skills to facilitate learning of new skills. Meanwhile, we perform the singular value decomposition on the diverse skill instructions to obtain common skill semantic subspace projection matrices, thereby recording the essential semantic space of skills. To achieve forget-less and generalization manipulation, we propose a Skills Specialization Aggregation to compute inter-skills similarity in skill semantic subspaces, achieving aggregation of the previously learned skill knowledge for any new or unknown skill. Extensive experiments demonstrate the effectiveness and superiority of our proposed SkillsCrafter.

