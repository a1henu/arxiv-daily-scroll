---
layout: default
title: A Diffusion-Driven Fine-Grained Nodule Synthesis Framework for Enhanced Lung Nodule Detection from Chest Radiographs
---

# A Diffusion-Driven Fine-Grained Nodule Synthesis Framework for Enhanced Lung Nodule Detection from Chest Radiographs
**arXiv**：[2603.01659v1](https://arxiv.org/abs/2603.01659) · [PDF](https://arxiv.org/pdf/2603.01659.pdf)  
**作者**：Aryan Goyal, Shreshtha Singh, Ashish Mittal, Manoj Tadepalli, Piyush Kumar, Preetham Putha  

**一句话要点**：提出基于扩散模型与LoRA适配器的细粒度结节合成框架，以增强胸部X光片中的肺结节检测。

**关键词**：肺结节检测, 扩散模型, LoRA适配器, 细粒度合成, 胸部X光片, 计算机辅助诊断

## 3 点简述
- 核心问题：肺结节检测因结节外观细微且特征多样而困难，现有合成方法缺乏细粒度控制。
- 方法要点：通过结节掩码条件训练扩散模型，并利用LoRA模块实现多放射学特征的独立与组合控制。
- 实验或效果：在内部和公共数据集上验证，下游检测性能提升，放射科医生评估确认可控性。

## 摘要（原文）

> Early detection of lung cancer in chest radiographs (CXRs) is crucial for improving patient outcomes, yet nodule detection remains challenging due to their subtle appearance and variability in radiological characteristics like size, texture, and boundary. For robust analysis, this diversity must be well represented in training datasets for deep learning based Computer-Assisted Diagnosis (CAD) systems. However, assembling such datasets is costly and often impractical, motivating the need for realistic synthetic data generation. Existing methods lack fine-grained control over synthetic nodule generation, limiting their utility in addressing data scarcity. This paper proposes a novel diffusion-based framework with low-rank adaptation (LoRA) adapters for characteristic controlled nodule synthesis on CXRs. We begin by addressing size and shape control through nodule mask conditioned training of the base diffusion model. To achieve individual characteristic control, we train separate LoRA modules, each dedicated to a specific radiological feature. However, since nodules rarely exhibit isolated characteristics, effective multi-characteristic control requires a balanced integration of features. We address this by leveraging the dynamic composability of LoRAs and revisiting existing merging strategies. Building on this, we identify two key issues, overlapping attention regions and non-orthogonal parameter spaces. To overcome these limitations, we introduce a novel orthogonality loss term during LoRA composition training. Extensive experiments on both in-house and public datasets demonstrate improved downstream nodule detection. Radiologist evaluations confirm the fine-grained controllability of our generated nodules, and across multiple quantitative metrics, our method surpasses existing nodule generation approaches for CXRs.

