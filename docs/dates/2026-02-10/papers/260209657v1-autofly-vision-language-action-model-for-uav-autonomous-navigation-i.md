---
layout: default
title: AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild
---

# AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild
**arXiv**：[2602.09657v1](https://arxiv.org/abs/2602.09657) · [PDF](https://arxiv.org/pdf/2602.09657.pdf)  
**作者**：Xiaolou Sun, Wufei Si, Wenhui Ni, Yuntian Li, Dongming Wu, Fei Xie, Runwei Guan, He-Yang Xu, Henghui Ding, Yuan Wu, Yutao Yue, Yongming Huang, Hui Xiong  

**一句话要点**：提出AutoFly端到端视觉-语言-动作模型，解决无人机在未知野外环境中的自主导航问题。

**关键词**：无人机自主导航, 视觉-语言-动作模型, 伪深度编码, 渐进训练策略, 自主导航数据集

## 3 点简述
- 核心问题：现有视觉语言导航依赖详细指令，不适用于未知野外环境，缺乏自主决策和真实数据。
- 方法要点：结合伪深度编码器增强空间推理，采用渐进两阶段训练策略对齐视觉、深度、语言与动作策略。
- 实验或效果：构建新数据集，AutoFly在模拟和真实环境中比先进基线成功率提高3.9%。

## 摘要（原文）

> Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in Embodied AI. Current VLN research for unmanned aerial vehicles (UAVs) relies on detailed, pre-specified instructions to guide the UAV along predetermined routes. However, real-world outdoor exploration typically occurs in unknown environments where detailed navigation instructions are unavailable. Instead, only coarse-grained positional or directional guidance can be provided, requiring UAVs to autonomously navigate through continuous planning and obstacle avoidance. To bridge this gap, we propose AutoFly, an end-to-end Vision-Language-Action (VLA) model for autonomous UAV navigation. AutoFly incorporates a pseudo-depth encoder that derives depth-aware features from RGB inputs to enhance spatial reasoning, coupled with a progressive two-stage training strategy that effectively aligns visual, depth, and linguistic representations with action policies. Moreover, existing VLN datasets have fundamental limitations for real-world autonomous navigation, stemming from their heavy reliance on explicit instruction-following over autonomous decision-making and insufficient real-world data. To address these issues, we construct a novel autonomous navigation dataset that shifts the paradigm from instruction-following to autonomous behavior modeling through: (1) trajectory collection emphasizing continuous obstacle avoidance, autonomous planning, and recognition workflows; (2) comprehensive real-world data integration. Experimental results demonstrate that AutoFly achieves a 3.9% higher success rate compared to state-of-the-art VLA baselines, with consistent performance across simulated and real environments.

