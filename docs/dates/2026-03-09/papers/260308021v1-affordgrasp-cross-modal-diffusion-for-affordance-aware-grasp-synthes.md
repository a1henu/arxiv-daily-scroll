---
layout: default
title: AffordGrasp: Cross-Modal Diffusion for Affordance-Aware Grasp Synthesis
---

# AffordGrasp: Cross-Modal Diffusion for Affordance-Aware Grasp Synthesis
**arXiv**：[2603.08021v1](https://arxiv.org/abs/2603.08021) · [PDF](https://arxiv.org/pdf/2603.08021.pdf)  
**作者**：Xiaofei Wu, Yi Zhang, Yumeng Liu, Yuexin Ma, Yujiao Shi, Xuming He  

**一句话要点**：提出AffordGrasp框架，通过跨模态扩散生成物理稳定且语义一致的人手抓取姿态，用于AR/VR和具身AI交互。

**关键词**：人手抓取合成, 跨模态扩散, 可供性感知, 语义对齐, 物理接触一致性, AR/VR交互

## 3 点简述
- 核心问题：现有语义抓取方法存在3D对象与文本指令间的模态鸿沟，缺乏空间或语义约束，导致抓取无效或不一致。
- 方法要点：引入可扩展标注流程生成细粒度语言标签，结合可供性感知潜在表示与双条件扩散过程，联合推理几何、空间可供性和语义。
- 实验或效果：在四个指令增强基准测试中评估，在抓取质量、语义准确性和多样性上显著优于现有方法。

## 摘要（原文）

> Generating human grasping poses that accurately reflect both object geometry and user-specified interaction semantics is essential for natural hand-object interactions in AR/VR and embodied AI. However, existing semantic grasping approaches struggle with the large modality gap between 3D object representations and textual instructions, and often lack explicit spatial or semantic constraints, leading to physically invalid or semantically inconsistent grasps. In this work, we present AffordGrasp, a diffusion-based framework that produces physically stable and semantically faithful human grasps with high precision. We first introduce a scalable annotation pipeline that automatically enriches hand-object interaction datasets with fine-grained structured language labels capturing interaction intent. Building upon these annotations, AffordGrasp integrates an affordance-aware latent representation of hand poses with a dual-conditioning diffusion process, enabling the model to jointly reason over object geometry, spatial affordances, and instruction semantics. A distribution adjustment module further enforces physical contact consistency and semantic alignment. We evaluate AffordGrasp across four instruction-augmented benchmarks derived from HO-3D, OakInk, GRAB, and AffordPose, and observe substantial improvements over state-of-the-art methods in grasp quality, semantic accuracy, and diversity.

