---
layout: default
title: FutureX: Enhance End-to-End Autonomous Driving via Latent Chain-of-Thought World Model
---

# FutureX: Enhance End-to-End Autonomous Driving via Latent Chain-of-Thought World Model
**arXiv**：[2512.11226v1](https://arxiv.org/abs/2512.11226) · [PDF](https://arxiv.org/pdf/2512.11226.pdf)  
**作者**：Hongbin Lin, Yiming Yang, Yifan Zhang, Chaoda Zheng, Jie Feng, Sheng Wang, Zhennan Wang, Shijia Chen, Boyang Wang, Yu Zhang, Xianming Liu, Shuguang Cui, Zhen Li  

**一句话要点**：提出FutureX以增强端到端自动驾驶规划，通过潜在思维链世界模型进行未来场景推理和轨迹优化。

**关键词**：自动驾驶规划, 世界模型, 思维链推理, 端到端学习, 轨迹优化

## 3 点简述
- 核心问题：端到端规划器仅依赖当前场景，在动态交通环境中可能导致次优响应。
- 方法要点：引入自动思维开关和潜在世界模型，通过思维链预测未来场景表示以优化轨迹。
- 实验或效果：在NAVSIM上提升TransFuser 6.2 PDMS，减少碰撞且不牺牲效率。

## 摘要（原文）

> In autonomous driving, end-to-end planners learn scene representations from raw sensor data and utilize them to generate a motion plan or control actions. However, exclusive reliance on the current scene for motion planning may result in suboptimal responses in highly dynamic traffic environments where ego actions further alter the future scene. To model the evolution of future scenes, we leverage the World Model to represent how the ego vehicle and its environment interact and change over time, which entails complex reasoning. The Chain of Thought (CoT) offers a promising solution by forecasting a sequence of future thoughts that subsequently guide trajectory refinement. In this paper, we propose FutureX, a CoT-driven pipeline that enhances end-to-end planners to perform complex motion planning via future scene latent reasoning and trajectory refinement. Specifically, the Auto-think Switch examines the current scene and decides whether additional reasoning is required to yield a higher-quality motion plan. Once FutureX enters the Thinking mode, the Latent World Model conducts a CoT-guided rollout to predict future scene representation, enabling the Summarizer Module to further refine the motion plan. Otherwise, FutureX operates in an Instant mode to generate motion plans in a forward pass for relatively simple scenes. Extensive experiments demonstrate that FutureX enhances existing methods by producing more rational motion plans and fewer collisions without compromising efficiency, thereby achieving substantial overall performance gains, e.g., 6.2 PDMS improvement for TransFuser on NAVSIM. Code will be released.

