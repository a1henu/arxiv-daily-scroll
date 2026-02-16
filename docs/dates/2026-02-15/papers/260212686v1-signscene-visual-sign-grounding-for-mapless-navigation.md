---
layout: default
title: SignScene: Visual Sign Grounding for Mapless Navigation
---

# SignScene: Visual Sign Grounding for Mapless Navigation
**arXiv**：[2602.12686v1](https://arxiv.org/abs/2602.12686) · [PDF](https://arxiv.org/pdf/2602.12686.pdf)  
**作者**：Nicky Zimmerman, Joel Loo, Benjamin Koh, Zishuo Wang, David Hsu  

**一句话要点**：提出SignScene表示法，利用视觉语言模型实现无地图导航中的标志视觉接地

**关键词**：无地图导航, 视觉接地, 视觉语言模型, 空间语义表示, 机器人导航, 标志理解

## 3 点简述
- 核心问题：机器人需在开放世界中基于多样复杂标志进行无地图导航，需将标志语义指令接地到局部3D场景元素和导航动作
- 方法要点：设计标志中心的空间语义表示SignScene，捕获导航相关场景和标志信息，以促进视觉语言模型有效推理的形式呈现
- 实验或效果：在9种环境类型的114个查询数据集上评估，接地准确率达88%，显著优于基线，并在Spot机器人上实现真实世界无地图导航

## 摘要（原文）

> Navigational signs enable humans to navigate unfamiliar environments without maps. This work studies how robots can similarly exploit signs for mapless navigation in the open world. A central challenge lies in interpreting signs: real-world signs are diverse and complex, and their abstract semantic contents need to be grounded in the local 3D scene. We formalize this as sign grounding, the problem of mapping semantic instructions on signs to corresponding scene elements and navigational actions. Recent Vision-Language Models (VLMs) offer the semantic common-sense and reasoning capabilities required for this task, but are sensitive to how spatial information is represented. We propose SignScene, a sign-centric spatial-semantic representation that captures navigation-relevant scene elements and sign information, and presents them to VLMs in a form conducive to effective reasoning. We evaluate our grounding approach on a dataset of 114 queries collected across nine diverse environment types, achieving 88% grounding accuracy and significantly outperforming baselines. Finally, we demonstrate that it enables real-world mapless navigation on a Spot robot using only signs.

