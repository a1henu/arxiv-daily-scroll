---
layout: default
title: SceneReVis: A Self-Reflective Vision-Grounded Framework for 3D Indoor Scene Synthesis via Multi-turn RL
---

# SceneReVis: A Self-Reflective Vision-Grounded Framework for 3D Indoor Scene Synthesis via Multi-turn RL
**arXiv**：[2602.09432v1](https://arxiv.org/abs/2602.09432) · [PDF](https://arxiv.org/pdf/2602.09432.pdf)  
**作者**：Yang Zhao, Shizhao Sun, Meisheng Zhang, Yingdong Shi, Xubo Yang, Jiang Bian  

**一句话要点**：提出SceneReVis框架，通过多轮强化学习解决3D室内场景合成中的空间幻觉问题。

**关键词**：3D场景合成, 自反思框架, 多轮强化学习, 空间冲突解决, 视觉基础模型, 室内场景生成

## 3 点简述
- 核心问题：现有单次3D场景合成方法因缺乏深思熟虑推理，常产生碰撞等空间幻觉。
- 方法要点：引入视觉基础的自反思框架，采用迭代诊断-行动循环，利用多模态反馈拦截和解决空间冲突。
- 实验或效果：构建SceneChain-12k数据集，通过两阶段训练实现高保真生成和目标优化，在长尾领域泛化性强。

## 摘要（原文）

> Current one-pass 3D scene synthesis methods often suffer from spatial hallucinations, such as collisions, due to a lack of deliberative reasoning. To bridge this gap, we introduce SceneReVis, a vision-grounded self-reflection framework that employs an iterative ``diagnose-and-act'' loop to explicitly intercept and resolve spatial conflicts using multi-modal feedback. To support this step-wise paradigm, we construct SceneChain-12k, a large-scale dataset of causal construction trajectories derived through a novel reverse engineering pipeline. We further propose a two-stage training recipe that transitions from Supervised Fine-Tuning to Agentic Reinforcement Learning, evolving the model into an active spatial planner. Extensive experiments demonstrate that SceneReVis achieves state-of-the-art performance in high-fidelity generation and goal-oriented optimization, with robust generalization to long-tail domains.

