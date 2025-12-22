---
layout: default
title: ImagineNav++: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination
---

# ImagineNav++: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination
**arXiv**：[2512.17435v1](https://arxiv.org/abs/2512.17435) · [PDF](https://arxiv.org/pdf/2512.17435.pdf)  
**作者**：Teng Wang, Xinxin Zhao, Wenzhe Cai, Changyin Sun  

**一句话要点**：提出ImagineNav++框架，通过场景想象实现视觉语言模型的无地图视觉导航

**关键词**：视觉语言模型, 无地图导航, 场景想象, 空间推理, 选择性注视记忆

## 3 点简述
- 核心问题：现有基于大语言模型的导航方法受限于文本表示，无法有效捕捉空间占用和场景几何信息。
- 方法要点：利用未来视图想象模块生成语义丰富的候选视图，通过视觉语言模型选择最佳视图进行导航规划。
- 实验或效果：在开放词汇对象和实例导航基准测试中达到无地图设置下的最先进性能，超越多数基于地图的方法。

## 摘要（原文）

> Visual navigation is a fundamental capability for autonomous home-assistance robots, enabling long-horizon tasks such as object search. While recent methods have leveraged Large Language Models (LLMs) to incorporate commonsense reasoning and improve exploration efficiency, their planning remains constrained by textual representations, which cannot adequately capture spatial occupancy or scene geometry--critical factors for navigation decisions. We explore whether Vision-Language Models (VLMs) can achieve mapless visual navigation using only onboard RGB/RGB-D streams, unlocking their potential for spatial perception and planning. We achieve this through an imagination-powered navigation framework, ImagineNav++, which imagines future observation images from candidate robot views and translates navigation planning into a simple best-view image selection problem for VLMs. First, a future-view imagination module distills human navigation preferences to generate semantically meaningful viewpoints with high exploration potential. These imagined views then serve as visual prompts for the VLM to identify the most informative viewpoint. To maintain spatial consistency, we develop a selective foveation memory mechanism, which hierarchically integrates keyframe observations via a sparse-to-dense framework, constructing a compact yet comprehensive memory for long-term spatial reasoning. This approach transforms goal-oriented navigation into a series of tractable point-goal navigation tasks. Extensive experiments on open-vocabulary object and instance navigation benchmarks show that ImagineNav++ achieves SOTA performance in mapless settings, even surpassing most map-based methods, highlighting the importance of scene imagination and memory in VLM-based spatial reasoning.

