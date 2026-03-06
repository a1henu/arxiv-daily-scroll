---
layout: default
title: RelaxFlow: Text-Driven Amodal 3D Generation
---

# RelaxFlow: Text-Driven Amodal 3D Generation
**arXiv**：[2603.05425v1](https://arxiv.org/abs/2603.05425) · [PDF](https://arxiv.org/pdf/2603.05425.pdf)  
**作者**：Jiayin Zhu, Guoji Fu, Xiaolu Liu, Qiyuan He, Yicong Li, Angela Yao  

**一句话要点**：提出RelaxFlow框架以解决文本驱动下遮挡3D生成中的语义模糊问题

**关键词**：文本驱动3D生成, 遮挡处理, 训练免费框架, 多先验共识, 松弛机制, 几何结构隔离

## 3 点简述
- 核心问题：图像到3D生成在遮挡下存在语义模糊，部分观察不足以确定物体类别
- 方法要点：通过双分支框架解耦控制粒度，结合多先验共识模块和松弛机制，理论证明松弛等价于低通滤波
- 实验或效果：引入两个诊断基准，实验显示能引导未见区域生成匹配文本意图且保持视觉保真度

## 摘要（原文）

> Image-to-3D generation faces inherent semantic ambiguity under occlusion, where partial observation alone is often insufficient to determine object category. In this work, we formalize text-driven amodal 3D generation, where text prompts steer the completion of unseen regions while strictly preserving input observation. Crucially, we identify that these objectives demand distinct control granularities: rigid control for the observation versus relaxed structural control for the prompt. To this end, we propose RelaxFlow, a training-free dual-branch framework that decouples control granularity via a Multi-Prior Consensus Module and a Relaxation Mechanism. Theoretically, we prove that our relaxation is equivalent to applying a low-pass filter on the generative vector field, which suppresses high-frequency instance details to isolate geometric structure that accommodates the observation. To facilitate evaluation, we introduce two diagnostic benchmarks, ExtremeOcc-3D and AmbiSem-3D. Extensive experiments demonstrate that RelaxFlow successfully steers the generation of unseen regions to match the prompt intent without compromising visual fidelity.

