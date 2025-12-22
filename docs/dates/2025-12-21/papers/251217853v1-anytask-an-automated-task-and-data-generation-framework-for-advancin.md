---
layout: default
title: AnyTask: an Automated Task and Data Generation Framework for Advancing Sim-to-Real Policy Learning
---

# AnyTask: an Automated Task and Data Generation Framework for Advancing Sim-to-Real Policy Learning
**arXiv**：[2512.17853v1](https://arxiv.org/abs/2512.17853) · [PDF](https://arxiv.org/pdf/2512.17853.pdf)  
**作者**：Ran Gong, Xiaohan Zhang, Jinghuan Shang, Maria Vittoria Minniti, Jigarkumar Patel, Valerio Pepe, Riedana Yan, Ahmet Gundogdu, Ivan Kapelyukh, Ali Abbas, Xiaoqiang Yan, Harsh Patel, Laura Herlant, Karl Schmeckpeper  

**一句话要点**：提出AnyTask自动化框架，结合GPU并行仿真与基础模型，以解决机器人仿真到现实策略学习中的数据生成难题。

**关键词**：仿真到现实学习, 任务自动化生成, 机器人操纵, 基础模型应用, 行为克隆, GPU并行仿真

## 3 点简述
- 核心问题：机器人学习受限于真实世界数据收集的高成本与低多样性，仿真任务设计需大量人工干预。
- 方法要点：通过三个代理（ViPR、ViPR-Eureka、ViPR-RL）自动生成专家演示，结合视觉语言模型和强化学习优化任务与运动规划。
- 实验或效果：在真实机器人硬件上部署行为克隆策略，在拾放、推拉等任务中实现44%的平均成功率，泛化至新物体姿态。

## 摘要（原文）

> Generalist robot learning remains constrained by data: large-scale, diverse, and high-quality interaction data are expensive to collect in the real world. While simulation has become a promising way for scaling up data collection, the related tasks, including simulation task design, task-aware scene generation, expert demonstration synthesis, and sim-to-real transfer, still demand substantial human effort. We present AnyTask, an automated framework that pairs massively parallel GPU simulation with foundation models to design diverse manipulation tasks and synthesize robot data. We introduce three AnyTask agents for generating expert demonstrations aiming to solve as many tasks as possible: 1) ViPR, a novel task and motion planning agent with VLM-in-the-loop Parallel Refinement; 2) ViPR-Eureka, a reinforcement learning agent with generated dense rewards and LLM-guided contact sampling; 3) ViPR-RL, a hybrid planning and learning approach that jointly produces high-quality demonstrations with only sparse rewards. We train behavior cloning policies on generated data, validate them in simulation, and deploy them directly on real robot hardware. The policies generalize to novel object poses, achieving 44% average success across a suite of real-world pick-and-place, drawer opening, contact-rich pushing, and long-horizon manipulation tasks. Our project website is at https://anytask.rai-inst.com .

