---
layout: default
title: RelaxFlow: Text-Driven Amodal 3D Generation
---

# RelaxFlow: Text-Driven Amodal 3D Generation
**arXiv**：[2603.05425v1](https://arxiv.org/abs/2603.05425) · [PDF](https://arxiv.org/pdf/2603.05425.pdf)  
**作者**：Jiayin Zhu, Guoji Fu, Xiaolu Liu, Qiyuan He, Yicong Li, Angela Yao  

**一句话要点**：提出RelaxFlow框架，通过解耦控制粒度实现文本驱动的无模态3D生成，解决遮挡下的语义模糊问题。

**关键词**：无模态3D生成, 文本驱动生成, 遮挡处理, 控制粒度解耦, 训练免费框架, 几何结构隔离

## 3 点简述
- 核心问题：图像到3D生成在遮挡下存在语义模糊，部分观察不足以确定物体类别。
- 方法要点：提出训练免费的双分支框架，通过多先验共识模块和松弛机制，分离观察的刚性控制与提示的结构控制。
- 实验或效果：引入两个诊断基准，实验显示RelaxFlow能引导未见区域生成匹配提示意图，同时保持视觉保真度。

## 摘要（原文）

> Image-to-3D generation faces inherent semantic ambiguity under occlusion, where partial observation alone is often insufficient to determine object category. In this work, we formalize text-driven amodal 3D generation, where text prompts steer the completion of unseen regions while strictly preserving input observation. Crucially, we identify that these objectives demand distinct control granularities: rigid control for the observation versus relaxed structural control for the prompt. To this end, we propose RelaxFlow, a training-free dual-branch framework that decouples control granularity via a Multi-Prior Consensus Module and a Relaxation Mechanism. Theoretically, we prove that our relaxation is equivalent to applying a low-pass filter on the generative vector field, which suppresses high-frequency instance details to isolate geometric structure that accommodates the observation. To facilitate evaluation, we introduce two diagnostic benchmarks, ExtremeOcc-3D and AmbiSem-3D. Extensive experiments demonstrate that RelaxFlow successfully steers the generation of unseen regions to match the prompt intent without compromising visual fidelity.

