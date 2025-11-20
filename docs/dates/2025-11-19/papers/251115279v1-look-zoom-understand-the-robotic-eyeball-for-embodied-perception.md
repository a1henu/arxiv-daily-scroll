---
layout: default
title: Look, Zoom, Understand: The Robotic Eyeball for Embodied Perception
---

# Look, Zoom, Understand: The Robotic Eyeball for Embodied Perception
**arXiv**：[2511.15279v1](https://arxiv.org/abs/2511.15279) · [PDF](https://arxiv.org/pdf/2511.15279.pdf)  
**作者**：Jiashu Yang, Yifan Han, Yucheng Xie, Ning Guo, Wenzhao Lian  

**一句话要点**：提出EyeVLA机器人眼球系统，以解决具身AI中视觉感知的主动数据获取问题。

**关键词**：具身AI, 主动视觉感知, 视觉语言动作模型, 强化学习, 机器人视觉系统

## 3 点简述
- 核心问题：现有视觉模型和固定相机系统无法兼顾广域覆盖与细粒度细节获取。
- 方法要点：将动作行为离散化为动作令牌，与视觉语言模型集成进行联合建模。
- 实验或效果：系统在真实环境中高效执行指令，通过旋转和缩放主动获取准确视觉信息。

## 摘要（原文）

> In embodied AI perception systems, visual perception should be active: the goal is not to passively process static images, but to actively acquire more informative data within pixel and spatial budget constraints. Existing vision models and fixed RGB-D camera systems fundamentally fail to reconcile wide-area coverage with fine-grained detail acquisition, severely limiting their efficacy in open-world robotic applications. To address this issue, we propose EyeVLA, a robotic eyeball for active visual perception that can take proactive actions based on instructions, enabling clear observation of fine-grained target objects and detailed information across a wide spatial extent. EyeVLA discretizes action behaviors into action tokens and integrates them with vision-language models (VLMs) that possess strong open-world understanding capabilities, enabling joint modeling of vision, language, and actions within a single autoregressive sequence. By using the 2D bounding box coordinates to guide the reasoning chain and applying reinforcement learning to refine the viewpoint selection policy, we transfer the open-world scene understanding capability of the VLM to a vision language action (VLA) policy using only minimal real-world data. Experiments show that our system efficiently performs instructed scenes in real-world environments and actively acquires more accurate visual information through instruction-driven actions of rotation and zoom, thereby achieving strong environmental perception capabilities. EyeVLA introduces a novel robotic vision system that leverages detailed and spatially rich, large-scale embodied data, and actively acquires highly informative visual observations for downstream embodied tasks.

