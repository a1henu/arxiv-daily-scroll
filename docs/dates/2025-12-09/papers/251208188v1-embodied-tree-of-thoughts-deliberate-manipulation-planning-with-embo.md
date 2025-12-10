---
layout: default
title: Embodied Tree of Thoughts: Deliberate Manipulation Planning with Embodied World Model
---

# Embodied Tree of Thoughts: Deliberate Manipulation Planning with Embodied World Model
**arXiv**：[2512.08188v1](https://arxiv.org/abs/2512.08188) · [PDF](https://arxiv.org/pdf/2512.08188.pdf)  
**作者**：Wenjiang Xu, Cindy Wang, Rui Fang, Mingkang Zhang, Lusong Li, Jing Xu, Jiayuan Gu, Zecui Zeng, Rui Chen  

**一句话要点**：提出Embodied Tree of Thoughts框架，利用物理数字孪生解决机器人操作规划中的幻觉与约束一致性问题。

**关键词**：机器人操作规划, 物理世界模型, 数字孪生, 树搜索, Real2Sim2Real框架, 视觉语言模型

## 3 点简述
- 问题：视频生成模型在机器人操作规划中缺乏物理基础，导致幻觉和长时程物理约束不一致。
- 方法：结合先验分支和反思分支的树搜索，通过物理模拟器实现Real2Sim2Real规划。
- 效果：在短长时程任务中优于基线，有效预测物理动态并适应失败。

## 摘要（原文）

> World models have emerged as a pivotal component in robot manipulation planning, enabling agents to predict future environmental states and reason about the consequences of actions before execution. While video-generation models are increasingly adopted, they often lack rigorous physical grounding, leading to hallucinations and a failure to maintain consistency in long-horizon physical constraints. To address these limitations, we propose Embodied Tree of Thoughts (EToT), a novel Real2Sim2Real planning framework that leverages a physics-based interactive digital twin as an embodied world model. EToT formulates manipulation planning as a tree search expanded through two synergistic mechanisms: (1) Priori Branching, which generates diverse candidate execution paths based on semantic and spatial analysis; and (2) Reflective Branching, which utilizes VLMs to diagnose execution failures within the simulator and iteratively refine the planning tree with corrective actions. By grounding high-level reasoning in a physics simulator, our framework ensures that generated plans adhere to rigid-body dynamics and collision constraints. We validate EToT on a suite of short- and long-horizon manipulation tasks, where it consistently outperforms baselines by effectively predicting physical dynamics and adapting to potential failures. Website at https://embodied-tree-of-thoughts.github.io .

