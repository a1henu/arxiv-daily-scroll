---
layout: default
title: Reinforcement Learning for Follow-the-Leader Robotic Endoscopic Navigation via Synthetic Data
---

# Reinforcement Learning for Follow-the-Leader Robotic Endoscopic Navigation via Synthetic Data
**arXiv**：[2601.02798v1](https://arxiv.org/abs/2601.02798) · [PDF](https://arxiv.org/pdf/2601.02798.pdf)  
**作者**：Sicong Gao, Chen Qian, Laurence Xian, Liao Wu, Maurice Pagnucco, Yang Song  

**一句话要点**：提出基于深度强化学习的跟随式内窥镜机器人导航方法，通过合成数据优化单目深度估计以最小化接触。

**关键词**：内窥镜机器人导航, 深度强化学习, 单目深度估计, 合成数据生成, 几何感知奖励机制, 柔性连续体结构

## 3 点简述
- 核心问题：内窥镜机器人在狭窄管状环境中自主导航时，避免与内壁接触是长期挑战，影响患者舒适度。
- 方法要点：采用柔性连续体结构设计机器人，结合单目深度估计引导的深度强化学习框架，利用合成数据微调深度模型。
- 实验或效果：在模拟环境中训练，深度精度提升39.2%，导航J指数降低0.67，验证了方法的鲁棒性和有效性。

## 摘要（原文）

> Autonomous navigation is crucial for both medical and industrial endoscopic robots, enabling safe and efficient exploration of narrow tubular environments without continuous human intervention, where avoiding contact with the inner walls has been a longstanding challenge for prior approaches. We present a follow-the-leader endoscopic robot based on a flexible continuum structure designed to minimize contact between the endoscope body and intestinal walls, thereby reducing patient discomfort. To achieve this objective, we propose a vision-based deep reinforcement learning framework guided by monocular depth estimation. A realistic intestinal simulation environment was constructed in \textit{NVIDIA Omniverse} to train and evaluate autonomous navigation strategies. Furthermore, thousands of synthetic intraluminal images were generated using NVIDIA Replicator to fine-tune the Depth Anything model, enabling dense three-dimensional perception of the intestinal environment with a single monocular camera. Subsequently, we introduce a geometry-aware reward and penalty mechanism to enable accurate lumen tracking. Compared with the original Depth Anything model, our method improves $δ_{1}$ depth accuracy by 39.2% and reduces the navigation J-index by 0.67 relative to the second-best method, demonstrating the robustness and effectiveness of the proposed approach.

