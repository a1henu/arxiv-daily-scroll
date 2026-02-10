---
layout: default
title: UniPlan: Vision-Language Task Planning for Mobile Manipulation with Unified PDDL Formulation
---

# UniPlan: Vision-Language Task Planning for Mobile Manipulation with Unified PDDL Formulation
**arXiv**：[2602.08537v1](https://arxiv.org/abs/2602.08537) · [PDF](https://arxiv.org/pdf/2602.08537.pdf)  
**作者**：Haoming Ye, Yunxiao Xiao, Cewu Lu, Panpan Cai  

**一句话要点**：提出UniPlan系统，通过统一PDDL表示实现大规模室内环境中的视觉语言任务规划

**关键词**：视觉语言任务规划, 移动操作, PDDL统一表示, 拓扑地图, 大语言模型推理, 机器人自主导航

## 3 点简述
- 核心问题：现有基于PDDL的规划方法局限于桌面操作，难以处理长时程移动操作任务
- 方法要点：将场景拓扑、视觉信息和机器人能力统一为PDDL表示，扩展学习领域以支持导航和双手协调
- 实验或效果：在真实图像的大规模地图上评估，成功率和计算效率显著优于VLM和LLM+PDDL方法

## 摘要（原文）

> Integration of VLM reasoning with symbolic planning has proven to be a promising approach to real-world robot task planning. Existing work like UniDomain effectively learns symbolic manipulation domains from real-world demonstrations, described in Planning Domain Definition Language (PDDL), and has successfully applied them to real-world tasks. These domains, however, are restricted to tabletop manipulation. We propose UniPlan, a vision-language task planning system for long-horizon mobile-manipulation in large-scale indoor environments, that unifies scene topology, visuals, and robot capabilities into a holistic PDDL representation. UniPlan programmatically extends learned tabletop domains from UniDomain to support navigation, door traversal, and bimanual coordination. It operates on a visual-topological map, comprising navigation landmarks anchored with scene images. Given a language instruction, UniPlan retrieves task-relevant nodes from the map and uses a VLM to ground the anchored image into task-relevant objects and their PDDL states; next, it reconnects these nodes to a compressed, densely-connected topological map, also represented in PDDL, with connectivity and costs derived from the original map; Finally, a mobile-manipulation plan is generated using off-the-shelf PDDL solvers. Evaluated on human-raised tasks in a large-scale map with real-world imagery, UniPlan significantly outperforms VLM and LLM+PDDL planning in success rate, plan quality, and computational efficiency.

