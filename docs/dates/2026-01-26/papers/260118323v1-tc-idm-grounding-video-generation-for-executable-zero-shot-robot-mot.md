---
layout: default
title: TC-IDM: Grounding Video Generation for Executable Zero-shot Robot Motion
---

# TC-IDM: Grounding Video Generation for Executable Zero-shot Robot Motion
**arXiv**：[2601.18323v1](https://arxiv.org/abs/2601.18323) · [PDF](https://arxiv.org/pdf/2601.18323.pdf)  
**作者**：Weishi Mi, Yong Bao, Xiaowei Chi, Xiaozhu Ju, Zhiyuan Qin, Kuangzhi Ge, Kai Tang, Peidong Jia, Shanghang Zhang, Jian Tang  

**一句话要点**：提出TC-IDM以通过工具轨迹桥接生成世界模型的视觉规划与机器人物理控制

**关键词**：机器人控制, 生成世界模型, 逆动力学模型, 零样本泛化, 可变形物体交互, 视觉语言动作范式

## 3 点简述
- 核心问题：生成世界模型的像素级规划与物理可执行动作之间存在鸿沟，限制机器人控制的泛化能力
- 方法要点：TC-IDM从生成视频中提取工具点云轨迹，使用解耦动作头映射为6自由度末端执行器运动和控制信号
- 实验或效果：在真实世界评估中，TC-IDM平均成功率61.11%，优于端到端VLA基线和其他逆动力学模型

## 摘要（原文）

> The vision-language-action (VLA) paradigm has enabled powerful robotic control by leveraging vision-language models, but its reliance on large-scale, high-quality robot data limits its generalization. Generative world models offer a promising alternative for general-purpose embodied AI, yet a critical gap remains between their pixel-level plans and physically executable actions.
>   To this end, we propose the Tool-Centric Inverse Dynamics Model (TC-IDM). By focusing on the tool's imagined trajectory as synthesized by the world model, TC-IDM establishes a robust intermediate representation that bridges the gap between visual planning and physical control.
>   TC-IDM extracts the tool's point cloud trajectories via segmentation and 3D motion estimation from generated videos. Considering diverse tool attributes, our architecture employs decoupled action heads to project these planned trajectories into 6-DoF end-effector motions and corresponding control signals.
>   This plan-and-translate paradigm not only supports a wide range of end-effectors but also significantly improves viewpoint invariance. Furthermore, it exhibits strong generalization capabilities across long-horizon and out-of-distribution tasks, including interacting with deformable objects.
>   In real-world evaluations, the world model with TC-IDM achieves an average success rate of 61.11 percent, with 77.7 percent on simple tasks and 38.46 percent on zero-shot deformable object tasks. It substantially outperforms end-to-end VLA-style baselines and other inverse dynamics models.

