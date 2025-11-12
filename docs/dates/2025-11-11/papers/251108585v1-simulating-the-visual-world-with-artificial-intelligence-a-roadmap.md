---
layout: default
title: Simulating the Visual World with Artificial Intelligence: A Roadmap
---

# Simulating the Visual World with Artificial Intelligence: A Roadmap
**arXiv**：[2511.08585v1](https://arxiv.org/abs/2511.08585) · [PDF](https://arxiv.org/pdf/2511.08585.pdf)  
**作者**：Jingtong Yue, Ziqi Huang, Zhaoxi Chen, Xintao Wang, Pengfei Wan, Ziwei Liu  

**一句话要点**：提出视频基础模型作为隐式世界模型，以构建交互式虚拟环境。

**关键词**：视频基础模型, 隐式世界模型, 视频渲染器, 物理合理性, 交互模拟, 多尺度规划

## 3 点简述
- 核心问题：视频生成从视觉吸引力转向物理合理性和交互性。
- 方法要点：结合隐式世界模型和视频渲染器，编码物理知识与动态。
- 实验或效果：应用于机器人、自动驾驶和游戏等领域。

## 摘要（原文）

> The landscape of video generation is shifting, from a focus on generating visually appealing clips to building virtual environments that support interaction and maintain physical plausibility. These developments point toward the emergence of video foundation models that function not only as visual generators but also as implicit world models, models that simulate the physical dynamics, agent-environment interactions, and task planning that govern real or imagined worlds. This survey provides a systematic overview of this evolution, conceptualizing modern video foundation models as the combination of two core components: an implicit world model and a video renderer. The world model encodes structured knowledge about the world, including physical laws, interaction dynamics, and agent behavior. It serves as a latent simulation engine that enables coherent visual reasoning, long-term temporal consistency, and goal-driven planning. The video renderer transforms this latent simulation into realistic visual observations, effectively producing videos as a "window" into the simulated world. We trace the progression of video generation through four generations, in which the core capabilities advance step by step, ultimately culminating in a world model, built upon a video generation model, that embodies intrinsic physical plausibility, real-time multimodal interaction, and planning capabilities spanning multiple spatiotemporal scales. For each generation, we define its core characteristics, highlight representative works, and examine their application domains such as robotics, autonomous driving, and interactive gaming. Finally, we discuss open challenges and design principles for next-generation world models, including the role of agent intelligence in shaping and evaluating these systems. An up-to-date list of related works is maintained at this link.

