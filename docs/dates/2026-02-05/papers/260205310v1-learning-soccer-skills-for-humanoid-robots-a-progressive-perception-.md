---
layout: default
title: Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework
---

# Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework
**arXiv**：[2602.05310v1](https://arxiv.org/abs/2602.05310) · [PDF](https://arxiv.org/pdf/2602.05310.pdf)  
**作者**：Jipeng Kong, Xinzhe Liu, Yuhang Lin, Jinrui Han, Sören Schwertfeger, Chenjia Bai, Xuelong Li  

**一句话要点**：提出渐进式感知-动作框架PAiD以解决人形机器人足球技能学习中的模块不稳定和训练冲突问题。

**关键词**：人形机器人足球, 感知-动作集成, 渐进式学习, 仿真到现实迁移, 运动技能获取

## 3 点简述
- 核心问题：现有方法存在模块间不稳定或端到端训练目标冲突，难以实现稳健的感知-动作集成。
- 方法要点：分三阶段渐进学习，包括运动技能获取、轻量感知-动作集成和物理感知的仿真到现实迁移。
- 实验或效果：在Unitree G1上实现高保真踢球，在多样条件下保持稳健性能，室内外场景一致执行。

## 摘要（原文）

> Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions-including static or rolling balls, various positions, and disturbances-while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

