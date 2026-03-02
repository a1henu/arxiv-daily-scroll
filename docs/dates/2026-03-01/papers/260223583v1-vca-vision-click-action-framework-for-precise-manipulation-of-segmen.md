---
layout: default
title: VCA: Vision-Click-Action Framework for Precise Manipulation of Segmented Objects in Target Ambiguous Environments
---

# VCA: Vision-Click-Action Framework for Precise Manipulation of Segmented Objects in Target Ambiguous Environments
**arXiv**：[2602.23583v1](https://arxiv.org/abs/2602.23583) · [PDF](https://arxiv.org/pdf/2602.23583.pdf)  
**作者**：Donggeon Kim, Seungwon Jan, Hyeonjun Park, Daegyu Lim  

**一句话要点**：提出Vision-Click-Action框架，通过点击交互解决目标模糊环境中分割对象的精确操控问题

**关键词**：视觉-点击-动作框架, 分割对象操控, 目标模糊环境, 机器人交互, 视觉选择

## 3 点简述
- 核心问题：视觉-语言-动作模型依赖语言导致目标模糊和认知负担，尤其在多相似对象环境中
- 方法要点：用预训练分割模型实现点击式视觉交互，替代文本命令以明确指定目标对象
- 实验或效果：实验验证VCA能有效操控指定目标对象，降低错误和认知负载

## 摘要（原文）

> The reliance on language in Vision-Language-Action (VLA) models introduces ambiguity, cognitive overhead, and difficulties in precise object identification and sequential task execution, particularly in environments with multiple visually similar objects. To address these limitations, we propose Vision-Click-Action (VCA), a framework that replaces verbose textual commands with direct, click-based visual interaction using pretrained segmentation models. By allowing operators to specify target objects clearly through visual selection in the robot's 2D camera view, VCA reduces interpretation errors, lowers cognitive load, and provides a practical and scalable alternative to language-driven interfaces for real-world robotic manipulation. Experimental results validate that the proposed VCA framework achieves effective instance-level manipulation of specified target objects. Experiment videos are available at https://robrosinc.github.io/vca/.

