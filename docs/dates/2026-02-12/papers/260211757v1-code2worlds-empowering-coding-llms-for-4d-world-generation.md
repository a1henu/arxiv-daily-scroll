---
layout: default
title: Code2Worlds: Empowering Coding LLMs for 4D World Generation
---

# Code2Worlds: Empowering Coding LLMs for 4D World Generation
**arXiv**：[2602.11757v1](https://arxiv.org/abs/2602.11757) · [PDF](https://arxiv.org/pdf/2602.11757.pdf)  
**作者**：Yi Zhang, Yunshuang Wang, Zeyu Zhang, Hao Tang  

**一句话要点**：提出Code2Worlds框架，通过语言到模拟代码生成实现4D世界生成

**关键词**：4D世界生成, 代码生成LLM, 物理模拟, 多尺度解耦, 闭环优化

## 3 点简述
- 核心问题：4D生成面临多尺度上下文纠缠和语义-物理执行差距两大挑战
- 方法要点：采用双流架构解耦对象生成与环境编排，建立物理感知闭环机制
- 实验效果：在Code4D基准上超越基线，SGS提升41%，丰富度提高49%

## 摘要（原文）

> Achieving spatial intelligence requires moving beyond visual plausibility to build world simulators grounded in physical laws. While coding LLMs have advanced static 3D scene generation, extending this paradigm to 4D dynamics remains a critical frontier. This task presents two fundamental challenges: multi-scale context entanglement, where monolithic generation fails to balance local object structures with global environmental layouts; and a semantic-physical execution gap, where open-loop code generation leads to physical hallucinations lacking dynamic fidelity. We introduce Code2Worlds, a framework that formulates 4D generation as language-to-simulation code generation. First, we propose a dual-stream architecture that disentangles retrieval-augmented object generation from hierarchical environmental orchestration. Second, to ensure dynamic fidelity, we establish a physics-aware closed-loop mechanism in which a PostProcess Agent scripts dynamics, coupled with a VLM-Motion Critic that performs self-reflection to iteratively refine simulation code. Evaluations on the Code4D benchmark show Code2Worlds outperforms baselines with a 41% SGS gain and 49% higher Richness, while uniquely generating physics-aware dynamics absent in prior static methods. Code: https://github.com/AIGeeksGroup/Code2Worlds. Website: https://aigeeksgroup.github.io/Code2Worlds.

