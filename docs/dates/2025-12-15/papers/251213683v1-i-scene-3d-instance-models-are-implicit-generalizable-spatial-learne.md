---
layout: default
title: I-Scene: 3D Instance Models are Implicit Generalizable Spatial Learners
---

# I-Scene: 3D Instance Models are Implicit Generalizable Spatial Learners
**arXiv**：[2512.13683v1](https://arxiv.org/abs/2512.13683) · [PDF](https://arxiv.org/pdf/2512.13683.pdf)  
**作者**：Lu Ling, Yunhao Ge, Yichen Sheng, Aniket Bera  

**一句话要点**：提出I-Scene方法，利用预训练3D实例生成器作为隐式空间学习器，实现交互式3D场景生成中的泛化问题。

**关键词**：3D场景生成, 空间泛化, 实例模型, 隐式学习, 交互式理解

## 3 点简述
- 核心问题：交互式3D场景生成面临泛化挑战，现有方法受限于数据集布局，难以适应新布局和对象组合。
- 方法要点：通过重新编程预训练3D实例生成器，以模型为中心进行空间监督，解锁其可转移空间知识，实现泛化。
- 实验或效果：在未见布局和新对象组合上展示泛化能力，空间推理从几何线索中涌现，支持接近、支撑和对称推断。

## 摘要（原文）

> Generalization remains the central challenge for interactive 3D scene generation. Existing learning-based approaches ground spatial understanding in limited scene dataset, restricting generalization to new layouts. We instead reprogram a pre-trained 3D instance generator to act as a scene level learner, replacing dataset-bounded supervision with model-centric spatial supervision. This reprogramming unlocks the generator transferable spatial knowledge, enabling generalization to unseen layouts and novel object compositions. Remarkably, spatial reasoning still emerges even when the training scenes are randomly composed objects. This demonstrates that the generator's transferable scene prior provides a rich learning signal for inferring proximity, support, and symmetry from purely geometric cues. Replacing widely used canonical space, we instantiate this insight with a view-centric formulation of the scene space, yielding a fully feed-forward, generalizable scene generator that learns spatial relations directly from the instance model. Quantitative and qualitative results show that a 3D instance generator is an implicit spatial learner and reasoner, pointing toward foundation models for interactive 3D scene understanding and generation. Project page: https://luling06.github.io/I-Scene-project/

