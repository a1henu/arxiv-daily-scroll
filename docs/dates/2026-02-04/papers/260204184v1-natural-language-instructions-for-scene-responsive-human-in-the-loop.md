---
layout: default
title: Natural Language Instructions for Scene-Responsive Human-in-the-Loop Motion Planning in Autonomous Driving using Vision-Language-Action Models
---

# Natural Language Instructions for Scene-Responsive Human-in-the-Loop Motion Planning in Autonomous Driving using Vision-Language-Action Models
**arXiv**：[2602.04184v1](https://arxiv.org/abs/2602.04184) · [PDF](https://arxiv.org/pdf/2602.04184.pdf)  
**作者**：Angel Martinez-Sanchez, Parthib Roy, Ross Greer  

**一句话要点**：提出基于doScenes数据集和OpenEMMA框架的指令条件化驾驶规划方法，以提升自动驾驶中语言指令跟随的鲁棒性。

**关键词**：指令条件化规划, 自动驾驶, 视觉-语言-动作模型, doScenes数据集, 轨迹生成, 鲁棒性评估

## 3 点简述
- 核心问题：现有指令跟随规划器依赖仿真或固定词汇，限制真实世界泛化能力。
- 方法要点：将doScenes自由形式指令作为乘客式提示集成到OpenEMMA视觉-语言接口中，实现轨迹生成前的语言条件化。
- 实验或效果：在849个场景上评估，指令条件化显著减少平均ADE 98.7%，优化提示可提升ADE达5.1%。

## 摘要（原文）

> Instruction-grounded driving, where passenger language guides trajectory planning, requires vehicles to understand intent before motion. However, most prior instruction-following planners rely on simulation or fixed command vocabularies, limiting real-world generalization. doScenes, the first real-world dataset linking free-form instructions (with referentiality) to nuScenes ground-truth motion, enables instruction-conditioned planning. In this work, we adapt OpenEMMA, an open-source MLLM-based end-to-end driving framework that ingests front-camera views and ego-state and outputs 10-step speed-curvature trajectories, to this setting, presenting a reproducible instruction-conditioned baseline on doScenes and investigate the effects of human instruction prompts on predicted driving behavior. We integrate doScenes directives as passenger-style prompts within OpenEMMA's vision-language interface, enabling linguistic conditioning before trajectory generation. Evaluated on 849 annotated scenes using ADE, we observe that instruction conditioning substantially improves robustness by preventing extreme baseline failures, yielding a 98.7% reduction in mean ADE. When such outliers are removed, instructions still influence trajectory alignment, with well-phrased prompts improving ADE by up to 5.1%. We use this analysis to discuss what makes a "good" instruction for the OpenEMMA framework. We release the evaluation prompts and scripts to establish a reproducible baseline for instruction-aware planning. GitHub: https://github.com/Mi3-Lab/doScenes-VLM-Planning

