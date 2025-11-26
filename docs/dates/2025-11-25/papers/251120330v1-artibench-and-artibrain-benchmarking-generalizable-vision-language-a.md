---
layout: default
title: ArtiBench and ArtiBrain: Benchmarking Generalizable Vision-Language Articulated Object Manipulation
---

# ArtiBench and ArtiBrain: Benchmarking Generalizable Vision-Language Articulated Object Manipulation
**arXiv**：[2511.20330v1](https://arxiv.org/abs/2511.20330) · [PDF](https://arxiv.org/pdf/2511.20330.pdf)  
**作者**：Yuhan Wu, Tiantian Wei, Shuo Wang, ZhiChao Wang, Yanyong Zhang, Daniel Cremers, Yan Xia  

**一句话要点**：提出ArtiBrain框架以解决铰接物体操作中的泛化挑战

**关键词**：铰接物体操作, 视觉语言模型, 基准测试, 扩散策略, 泛化能力, 模块化框架

## 3 点简述
- 核心问题：现有视觉语言和扩散策略在铰接物体操作中难以跨部件、实例和类别泛化
- 方法要点：ArtiBrain结合高层推理与自适应低层控制，使用VLM分解任务和混合控制器执行
- 实验或效果：在ArtiBench基准上，ArtiBrain在鲁棒性和泛化性上显著优于现有方法

## 摘要（原文）

> Interactive articulated manipulation requires long-horizon, multi-step interactions with appliances while maintaining physical consistency. Existing vision-language and diffusion-based policies struggle to generalize across parts, instances, and categories. We first introduce ArtiBench, a five-level benchmark covering kitchen, storage, office, and tool environments. ArtiBench enables structured evaluation from cross-part and cross-instance variation to long-horizon multi-object tasks, revealing the core generalization challenges of articulated object manipulation. Building on this benchmark, we propose ArtiBrain, a modular framework that unifies high-level reasoning with adaptive low-level control. ArtiBrain uses a VLM-based Task Reasoner (GPT-4.1) to decompose and validate subgoals, and employs a Hybrid Controller that combines geometry-aware keyframe execution with affordance-guided diffusion for precise and interpretable manipulation. An Affordance Memory Bank continually accumulates successful execution episodes and propagates part-level actionable affordances to unseen articulated parts and configurations. Extensive experiments on ArtiBench show that our ArtiBrain significantly outperforms state-of-the-art multimodal and diffusion-based methods in robustness and generalization. Code and dataset will be released upon acceptance.

