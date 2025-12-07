---
layout: default
title: Object Reconstruction under Occlusion with Generative Priors and Contact-induced Constraints
---

# Object Reconstruction under Occlusion with Generative Priors and Contact-induced Constraints
**arXiv**：[2512.05079v1](https://arxiv.org/abs/2512.05079) · [PDF](https://arxiv.org/pdf/2512.05079.pdf)  
**作者**：Minghan Zhu, Zhiyi Wang, Qihang Sun, Maani Ghaffari, Michael Posa  

**一句话要点**：提出结合生成先验与接触约束的方法，以解决遮挡下物体重建的歧义问题

**关键词**：物体重建, 遮挡处理, 生成先验, 接触约束, 3D生成, 机器人操作

## 3 点简述
- 核心问题：相机仅捕获部分观测，遮挡导致物体重建困难，几何信息不完整
- 方法要点：利用生成模型学习形状先验，结合接触信息提供边界约束，通过接触引导的3D生成整合两者
- 实验或效果：在合成和真实数据上验证，相比纯生成或接触优化，重建效果提升

## 摘要（原文）

> Object geometry is key information for robot manipulation. Yet, object reconstruction is a challenging task because cameras only capture partial observations of objects, especially when occlusion occurs. In this paper, we leverage two extra sources of information to reduce the ambiguity of vision signals. First, generative models learn priors of the shapes of commonly seen objects, allowing us to make reasonable guesses of the unseen part of geometry. Second, contact information, which can be obtained from videos and physical interactions, provides sparse constraints on the boundary of the geometry. We combine the two sources of information through contact-guided 3D generation. The guidance formulation is inspired by drag-based editing in generative models. Experiments on synthetic and real-world data show that our approach improves the reconstruction compared to pure 3D generation and contact-based optimization.

