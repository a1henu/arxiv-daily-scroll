---
layout: default
title: CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation
---

# CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation
**arXiv**：[2602.18424v1](https://arxiv.org/abs/2602.18424) · [PDF](https://arxiv.org/pdf/2602.18424.pdf)  
**作者**：Xia Su, Ruiqi Chen, Benlin Liu, Jingwei Ma, Zonglin Di, Ranjay Krishna, Jon Froehlich  

**一句话要点**：提出CapNav基准以评估视觉语言模型在能力约束下的室内导航性能

**关键词**：能力约束导航, 视觉语言模型评估, 室内导航基准, 空间推理, 机器人导航

## 3 点简述
- 核心问题：真实导航受限于代理的移动能力，现有VLM评估未充分考量此因素
- 方法要点：定义五种代表性代理，结合物理维度和能力，构建包含45场景和473任务的基准
- 实验或效果：测试13个VLM，发现性能随约束收紧而下降，模型在空间维度推理上存在困难

## 摘要（原文）

> Vision-Language Models (VLMs) have shown remarkable progress in Vision-Language Navigation (VLN), offering new possibilities for navigation decision-making that could benefit both robotic platforms and human users. However, real-world navigation is inherently conditioned by the agent's mobility constraints. For example, a sweeping robot cannot traverse stairs, while a quadruped can. We introduce Capability-Conditioned Navigation (CapNav), a benchmark designed to evaluate how well VLMs can navigate complex indoor spaces given an agent's specific physical and operational capabilities. CapNav defines five representative human and robot agents, each described with physical dimensions, mobility capabilities, and environmental interaction abilities. CapNav provides 45 real-world indoor scenes, 473 navigation tasks, and 2365 QA pairs to test if VLMs can traverse indoor environments based on agent capabilities. We evaluate 13 modern VLMs and find that current VLM's navigation performance drops sharply as mobility constraints tighten, and that even state-of-the-art models struggle with obstacle types that require reasoning on spatial dimensions. We conclude by discussing the implications for capability-aware navigation and the opportunities for advancing embodied spatial reasoning in future VLMs. The benchmark is available at https://github.com/makeabilitylab/CapNav

