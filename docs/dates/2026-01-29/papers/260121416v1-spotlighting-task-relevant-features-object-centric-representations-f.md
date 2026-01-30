---
layout: default
title: Spotlighting Task-Relevant Features: Object-Centric Representations for Better Generalization in Robotic Manipulation
---

# Spotlighting Task-Relevant Features: Object-Centric Representations for Better Generalization in Robotic Manipulation
**arXiv**：[2601.21416v1](https://arxiv.org/abs/2601.21416) · [PDF](https://arxiv.org/pdf/2601.21416.pdf)  
**作者**：Alexandre Chapin, Bruno Machado, Emmanuel Dellandréa, Liming Chen  

**一句话要点**：提出基于槽的对象中心表示以提升机器人操作策略在视觉分布变化下的泛化能力

**关键词**：机器人操作, 视觉表示, 对象中心表示, 泛化能力, 槽基表示, 分布变化

## 3 点简述
- 核心问题：现有全局和密集特征混合任务相关与无关信息，导致光照、纹理变化或干扰物存在时泛化差
- 方法要点：引入槽基对象中心表示，将密集特征分组为有限对象实体，减少噪声并保留任务信息
- 实验或效果：在模拟和真实世界任务中，该表示优于全局和密集特征，无需任务特定预训练即提升泛化

## 摘要（原文）

> The generalization capabilities of robotic manipulation policies are heavily influenced by the choice of visual representations. Existing approaches typically rely on representations extracted from pre-trained encoders, using two dominant types of features: global features, which summarize an entire image via a single pooled vector, and dense features, which preserve a patch-wise embedding from the final encoder layer. While widely used, both feature types mix task-relevant and irrelevant information, leading to poor generalization under distribution shifts, such as changes in lighting, textures, or the presence of distractors. In this work, we explore an intermediate structured alternative: Slot-Based Object-Centric Representations (SBOCR), which group dense features into a finite set of object-like entities. This representation permits to naturally reduce the noise provided to the robotic manipulation policy while keeping enough information to efficiently perform the task. We benchmark a range of global and dense representations against intermediate slot-based representations, across a suite of simulated and real-world manipulation tasks ranging from simple to complex. We evaluate their generalization under diverse visual conditions, including changes in lighting, texture, and the presence of distractors. Our findings reveal that SBOCR-based policies outperform dense and global representation-based policies in generalization settings, even without task-specific pretraining. These insights suggest that SBOCR is a promising direction for designing visual systems that generalize effectively in dynamic, real-world robotic environments.

