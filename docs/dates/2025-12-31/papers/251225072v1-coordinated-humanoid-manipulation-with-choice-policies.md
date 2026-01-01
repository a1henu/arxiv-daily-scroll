---
layout: default
title: Coordinated Humanoid Manipulation with Choice Policies
---

# Coordinated Humanoid Manipulation with Choice Policies
**arXiv**：[2512.25072v1](https://arxiv.org/abs/2512.25072) · [PDF](https://arxiv.org/pdf/2512.25072.pdf)  
**作者**：Haozhi Qi, Yen-Jen Wang, Toru Lin, Brent Yi, Yi Ma, Koushil Sreenath, Jitendra Malik  

**一句话要点**：提出Choice Policy模仿学习框架，结合模块化遥操作，以解决人形机器人全身协调操控问题。

**关键词**：人形机器人操控, 模仿学习, 模块化遥操作, 全身协调, 手眼协调, 长时任务

## 3 点简述
- 核心问题：人形机器人在人机环境中实现头、手、腿的稳健全身协调操控是重大挑战。
- 方法要点：通过模块化遥操作分解控制，并引入Choice Policy生成多候选动作并评分，支持快速推理和多模态行为建模。
- 实验或效果：在洗碗机装载和白板擦拭任务中，Choice Policy显著优于扩散策略和标准行为克隆，手眼协调对长时任务至关重要。

## 摘要（原文）

> Humanoid robots hold great promise for operating in human-centric environments, yet achieving robust whole-body coordination across the head, hands, and legs remains a major challenge. We present a system that combines a modular teleoperation interface with a scalable learning framework to address this problem. Our teleoperation design decomposes humanoid control into intuitive submodules, which include hand-eye coordination, grasp primitives, arm end-effector tracking, and locomotion. This modularity allows us to collect high-quality demonstrations efficiently. Building on this, we introduce Choice Policy, an imitation learning approach that generates multiple candidate actions and learns to score them. This architecture enables both fast inference and effective modeling of multimodal behaviors. We validate our approach on two real-world tasks: dishwasher loading and whole-body loco-manipulation for whiteboard wiping. Experiments show that Choice Policy significantly outperforms diffusion policies and standard behavior cloning. Furthermore, our results indicate that hand-eye coordination is critical for success in long-horizon tasks. Our work demonstrates a practical path toward scalable data collection and learning for coordinated humanoid manipulation in unstructured environments.

