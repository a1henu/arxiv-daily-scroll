---
layout: default
title: Imagine a City: CityGenAgent for Procedural 3D City Generation
---

# Imagine a City: CityGenAgent for Procedural 3D City Generation
**arXiv**：[2602.05362v1](https://arxiv.org/abs/2602.05362) · [PDF](https://arxiv.org/pdf/2602.05362.pdf)  
**作者**：Zishan Liu, Zecong Tang, RuoCheng Wu, Xinzhe Zheng, Jingyu Hu, Ka-Hei Hui, Haoran Xie, Bo Dai, Zhengzhe Liu  

**一句话要点**：提出CityGenAgent框架，通过自然语言驱动分层程序生成高质量3D城市，提升可控性与视觉质量。

**关键词**：3D城市生成, 程序生成, 自然语言驱动, 分层结构, 强化学习, 语义对齐

## 3 点简述
- 核心问题：现有方法在高保真资产创建、可控性和操作方面存在不足，影响3D城市生成的实用性。
- 方法要点：采用Block Program和Building Program分层结构，结合监督微调与强化学习两阶段策略，确保结构正确性和语义对齐。
- 实验或效果：评估显示在语义对齐、视觉质量和可控性上优于现有方法，支持自然语言编辑与操作。

## 摘要（原文）

> The automated generation of interactive 3D cities is a critical challenge with broad applications in autonomous driving, virtual reality, and embodied intelligence. While recent advances in generative models and procedural techniques have improved the realism of city generation, existing methods often struggle with high-fidelity asset creation, controllability, and manipulation. In this work, we introduce CityGenAgent, a natural language-driven framework for hierarchical procedural generation of high-quality 3D cities. Our approach decomposes city generation into two interpretable components, Block Program and Building Program. To ensure structural correctness and semantic alignment, we adopt a two-stage learning strategy: (1) Supervised Fine-Tuning (SFT). We train BlockGen and BuildingGen to generate valid programs that adhere to schema constraints, including non-self-intersecting polygons and complete fields; (2) Reinforcement Learning (RL). We design Spatial Alignment Reward to enhance spatial reasoning ability and Visual Consistency Reward to bridge the gap between textual descriptions and the visual modality. Benefiting from the programs and the models' generalization, CityGenAgent supports natural language editing and manipulation. Comprehensive evaluations demonstrate superior semantic alignment, visual quality, and controllability compared to existing methods, establishing a robust foundation for scalable 3D city generation.

