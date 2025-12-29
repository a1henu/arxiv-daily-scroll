---
layout: default
title: LongFly: Long-Horizon UAV Vision-and-Language Navigation with Spatiotemporal Context Integration
---

# LongFly: Long-Horizon UAV Vision-and-Language Navigation with Spatiotemporal Context Integration
**arXiv**：[2512.22010v1](https://arxiv.org/abs/2512.22010) · [PDF](https://arxiv.org/pdf/2512.22010.pdf)  
**作者**：Wen Jiang, Li Wang, Kangyao Huang, Wei Fan, Jinyuan Liu, Shaoyu Liu, Hongwei Duan, Bin Xu, Xiangyang Ji  

**一句话要点**：提出LongFly框架，通过时空上下文建模解决无人机长时程视觉语言导航中的语义对齐与路径规划问题。

**关键词**：无人机视觉语言导航, 长时程导航, 时空上下文建模, 历史数据压缩, 多模态集成, 路径规划

## 3 点简述
- 核心问题：现有无人机视觉语言导航方法难以建模复杂环境中的长时程时空上下文，导致语义对齐不准确和路径规划不稳定。
- 方法要点：采用历史感知时空建模策略，包括基于槽的历史图像压缩、时空轨迹编码和提示引导多模态集成模块。
- 实验或效果：在成功率和路径长度加权成功率上分别超越现有基线7.89%和6.33%，在可见和未见环境中表现一致。

## 摘要（原文）

> Unmanned aerial vehicles (UAVs) are crucial tools for post-disaster search and rescue, facing challenges such as high information density, rapid changes in viewpoint, and dynamic structures, especially in long-horizon navigation. However, current UAV vision-and-language navigation(VLN) methods struggle to model long-horizon spatiotemporal context in complex environments, resulting in inaccurate semantic alignment and unstable path planning. To this end, we propose LongFly, a spatiotemporal context modeling framework for long-horizon UAV VLN. LongFly proposes a history-aware spatiotemporal modeling strategy that transforms fragmented and redundant historical data into structured, compact, and expressive representations. First, we propose the slot-based historical image compression module, which dynamically distills multi-view historical observations into fixed-length contextual representations. Then, the spatiotemporal trajectory encoding module is introduced to capture the temporal dynamics and spatial structure of UAV trajectories. Finally, to integrate existing spatiotemporal context with current observations, we design the prompt-guided multimodal integration module to support time-based reasoning and robust waypoint prediction. Experimental results demonstrate that LongFly outperforms state-of-the-art UAV VLN baselines by 7.89\% in success rate and 6.33\% in success weighted by path length, consistently across both seen and unseen environments.

