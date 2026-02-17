---
layout: default
title: PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement
---

# PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement
**arXiv**：[2602.14968v1](https://arxiv.org/abs/2602.14968) · [PDF](https://arxiv.org/pdf/2602.14968.pdf)  
**作者**：Yian Wang, Han Yang, Minghao Guo, Xiaowen Qiu, Tsun-Hsuan Wang, Wojciech Matusik, Joshua B. Tenenbaum, Chuang Gan  

**一句话要点**：提出PhyScensis框架，通过LLM代理与物理引擎生成复杂物理场景布局

**关键词**：物理场景生成, LLM代理, 物理引擎, 3D布局, 机器人仿真, 空间关系建模

## 3 点简述
- 核心问题：现有3D环境生成方法忽视物体间物理关系，难以创建复杂真实场景。
- 方法要点：结合LLM代理迭代提议、物理引擎求解器实现及反馈机制，确保物理合理性。
- 实验或效果：在场景复杂度、视觉质量和物理准确性上优于先前方法，适用于机器人操作。

## 摘要（原文）

> Automatically generating interactive 3D environments is crucial for scaling up robotic data collection in simulation. While prior work has primarily focused on 3D asset placement, it often overlooks the physical relationships between objects (e.g., contact, support, balance, and containment), which are essential for creating complex and realistic manipulation scenarios such as tabletop arrangements, shelf organization, or box packing. Compared to classical 3D layout generation, producing complex physical scenes introduces additional challenges: (a) higher object density and complexity (e.g., a small shelf may hold dozens of books), (b) richer supporting relationships and compact spatial layouts, and (c) the need to accurately model both spatial placement and physical properties. To address these challenges, we propose PhyScensis, an LLM agent-based framework powered by a physics engine, to produce physically plausible scene configurations with high complexity. Specifically, our framework consists of three main components: an LLM agent iteratively proposes assets with spatial and physical predicates; a solver, equipped with a physics engine, realizes these predicates into a 3D scene; and feedback from the solver informs the agent to refine and enrich the configuration. Moreover, our framework preserves strong controllability over fine-grained textual descriptions and numerical parameters (e.g., relative positions, scene stability), enabled through probabilistic programming for stability and a complementary heuristic that jointly regulates stability and spatial relations. Experimental results show that our method outperforms prior approaches in scene complexity, visual quality, and physical accuracy, offering a unified pipeline for generating complex physical scene layouts for robotic manipulation.

