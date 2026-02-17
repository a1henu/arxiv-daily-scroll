---
layout: default
title: Affordance Transfer Across Object Instances via Semantically Anchored Functional Map
---

# Affordance Transfer Across Object Instances via Semantically Anchored Functional Map
**arXiv**：[2602.14874v1](https://arxiv.org/abs/2602.14874) · [PDF](https://arxiv.org/pdf/2602.14874.pdf)  
**作者**：Xiaoxiang Dong, Weiming Zhi  

**一句话要点**：提出语义锚定功能映射以跨对象实例迁移功能可供性

**关键词**：功能可供性迁移, 语义对应, 功能映射, 机器人学习, 视觉演示

## 3 点简述
- 核心问题：如何从单次视觉演示中，将交互区域迁移到几何差异大但功能相似的不同对象实例上
- 方法要点：通过语义锚定功能映射，识别语义对应区域并传播约束，实现密集语义一致对应
- 实验或效果：在合成对象类别和真实机器人操作任务中验证，能以较低计算成本准确迁移功能可供性

## 摘要（原文）

> Traditional learning from demonstration (LfD) generally demands a cumbersome collection of physical demonstrations, which can be time-consuming and challenging to scale. Recent advances show that robots can instead learn from human videos by extracting interaction cues without direct robot involvement. However, a fundamental challenge remains: how to generalize demonstrated interactions across different object instances that share similar functionality but vary significantly in geometry. In this work, we propose \emph{Semantic Anchored Functional Maps} (SemFM), a framework for transferring affordances across objects from a single visual demonstration. Starting from a coarse mesh reconstructed from an image, our method identifies semantically corresponding functional regions between objects, selects mutually exclusive semantic anchors, and propagates these constraints over the surface using a functional map to obtain a dense, semantically consistent correspondence. This enables demonstrated interaction regions to be transferred across geometrically diverse objects in a lightweight and interpretable manner. Experiments on synthetic object categories and real-world robotic manipulation tasks show that our approach enables accurate affordance transfer with modest computational cost, making it well-suited for practical robotic perception-to-action pipelines.

