---
layout: default
title: K-Gen: A Multimodal Language-Conditioned Approach for Interpretable Keypoint-Guided Trajectory Generation
---

# K-Gen: A Multimodal Language-Conditioned Approach for Interpretable Keypoint-Guided Trajectory Generation
**arXiv**：[2603.04868v1](https://arxiv.org/abs/2603.04868) · [PDF](https://arxiv.org/pdf/2603.04868.pdf)  
**作者**：Mingxuan Mu, Guo Yang, Lei Chen, Ping Wu, Jianxun Cui  

**一句话要点**：提出K-Gen，一种基于可解释关键点的多模态轨迹生成方法，用于自动驾驶仿真。

**关键词**：自动驾驶仿真, 轨迹生成, 多模态大语言模型, 可解释关键点, 强化微调

## 3 点简述
- 核心问题：现有方法依赖结构化地图数据，难以捕捉场景的丰富视觉上下文。
- 方法要点：结合多模态大语言模型，从栅格化BEV地图和文本描述生成可解释关键点及推理，再精炼为轨迹。
- 实验或效果：在WOMD和nuPlan数据集上优于基线，验证了多模态推理与关键点引导的有效性。

## 摘要（原文）

> Generating realistic and diverse trajectories is a critical challenge in autonomous driving simulation. While Large Language Models (LLMs) show promise, existing methods often rely on structured data like vectorized maps, which fail to capture the rich, unstructured visual context of a scene. To address this, we propose K-Gen, an interpretable keypoint-guided multimodal framework that leverages Multimodal Large Language Models (MLLMs) to unify rasterized BEV map inputs with textual scene descriptions. Instead of directly predicting full trajectories, K-Gen generates interpretable keypoints along with reasoning that reflects agent intentions, which are subsequently refined into accurate trajectories by a refinement module. To further enhance keypoint generation, we apply T-DAPO, a trajectory-aware reinforcement fine-tuning algorithm. Experiments on WOMD and nuPlan demonstrate that K-Gen outperforms existing baselines, highlighting the effectiveness of combining multimodal reasoning with keypoint-guided trajectory generation.

