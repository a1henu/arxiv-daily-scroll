---
layout: default
title: StyleVLA: Driving Style-Aware Vision Language Action Model for Autonomous Driving
---

# StyleVLA: Driving Style-Aware Vision Language Action Model for Autonomous Driving
**arXiv**：[2603.09482v1](https://arxiv.org/abs/2603.09482) · [PDF](https://arxiv.org/pdf/2603.09482.pdf)  
**作者**：Yuan Gao, Dengyuan Hua, Mattia Piccinini, Finn Rasmus Schäfer, Korbinian Moller, Lin Li, Johannes Betz  

**一句话要点**：提出StyleVLA，一种基于物理约束的视觉语言动作模型，用于生成多样且物理可行的自动驾驶行为。

**关键词**：自动驾驶, 视觉语言动作模型, 驾驶风格适应, 物理约束, 轨迹生成, 混合损失

## 3 点简述
- 现有VLA模型主要生成通用避撞轨迹，缺乏对多样化驾驶风格的适应能力。
- StyleVLA引入混合损失，结合运动学一致性约束和连续回归头，提升轨迹的物理可行性。
- 在BEV和FPV数据集上，StyleVLA在成功率、物理可行性和风格遵循方面显著优于专有模型。

## 摘要（原文）

> Vision Language Models (VLMs) bridge visual perception and linguistic reasoning. In Autonomous Driving (AD), this synergy has enabled Vision Language Action (VLA) models, which translate high-level multimodal understanding into driving behaviors, typically represented as future trajectories. However, existing VLA models mainly generate generic collision-free trajectories. Beyond collision avoidance, adapting to diverse driving styles (e.g., sporty, comfortable) is essential for personalized driving. Moreover, many methods treat trajectory generation as naive token prediction, which can produce kinematically infeasible actions. To address these limitations, we present StyleVLA, a physics-informed VLA framework for generating diverse and physically plausible driving behaviors. We introduce a hybrid loss that combines a kinematic consistency constraint with a continuous regression head to improve trajectory feasibility. To train StyleVLA, built on Qwen3-VL-4B, we construct a large-scale instruction dataset with over 1.2k scenarios, 76k Bird's Eye View (BEV) samples, and 42k First Person View (FPV) samples, with ground-truth trajectories for five driving styles and natural-language instructions. Experiments show that our 4B-parameter StyleVLA significantly outperforms proprietary models (e.g., Gemini-3-Pro) and state-of-the-art VLA models. Using a composite driving score measuring success rate, physical feasibility, and style adherence, StyleVLA achieves 0.55 on BEV and 0.51 on FPV, versus 0.32 and 0.35 for Gemini-3-Pro. These results show that a specialized, physics-informed, lightweight model can surpass closed-source models on domain-specific tasks.

