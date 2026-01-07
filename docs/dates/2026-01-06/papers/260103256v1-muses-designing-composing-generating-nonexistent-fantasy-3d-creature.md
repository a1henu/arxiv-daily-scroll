---
layout: default
title: Muses: Designing, Composing, Generating Nonexistent Fantasy 3D Creatures without Training
---

# Muses: Designing, Composing, Generating Nonexistent Fantasy 3D Creatures without Training
**arXiv**：[2601.03256v1](https://arxiv.org/abs/2601.03256) · [PDF](https://arxiv.org/pdf/2601.03256.pdf)  
**作者**：Hexiao Lu, Xiaokun Sun, Zeyu Cai, Hao Guo, Ying Tai, Jian Yang, Zhenyu Zhang  

**一句话要点**：提出Muses方法，无需训练即可生成幻想3D生物，基于骨架引导的设计与生成流程。

**关键词**：3D生物生成, 训练免费方法, 骨架引导, 体素组装, 外观建模, 图约束推理

## 3 点简述
- 核心问题：现有方法依赖部件优化或2D生成，导致3D资产不真实或不连贯。
- 方法要点：利用3D骨架作为基础表示，通过图约束推理构建骨架，指导体素组装和外观建模。
- 实验或效果：在视觉保真度和文本对齐方面达到先进水平，支持灵活3D对象编辑。

## 摘要（原文）

> We present Muses, the first training-free method for fantastic 3D creature generation in a feed-forward paradigm. Previous methods, which rely on part-aware optimization, manual assembly, or 2D image generation, often produce unrealistic or incoherent 3D assets due to the challenges of intricate part-level manipulation and limited out-of-domain generation. In contrast, Muses leverages the 3D skeleton, a fundamental representation of biological forms, to explicitly and rationally compose diverse elements. This skeletal foundation formalizes 3D content creation as a structure-aware pipeline of design, composition, and generation. Muses begins by constructing a creatively composed 3D skeleton with coherent layout and scale through graph-constrained reasoning. This skeleton then guides a voxel-based assembly process within a structured latent space, integrating regions from different objects. Finally, image-guided appearance modeling under skeletal conditions is applied to generate a style-consistent and harmonious texture for the assembled shape. Extensive experiments establish Muses' state-of-the-art performance in terms of visual fidelity and alignment with textual descriptions, and potential on flexible 3D object editing. Project page: https://luhexiao.github.io/Muses.github.io/.

