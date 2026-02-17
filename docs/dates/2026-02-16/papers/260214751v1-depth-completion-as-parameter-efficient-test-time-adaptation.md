---
layout: default
title: Depth Completion as Parameter-Efficient Test-Time Adaptation
---

# Depth Completion as Parameter-Efficient Test-Time Adaptation
**arXiv**：[2602.14751v1](https://arxiv.org/abs/2602.14751) · [PDF](https://arxiv.org/pdf/2602.14751.pdf)  
**作者**：Bingxin Ke, Qunjie Zhou, Jiahui Huang, Xuanchi Ren, Tianchang Shen, Konrad Schindler, Laura Leal-Taixé, Shengyu Huang  

**一句话要点**：提出CAPA框架，通过参数高效测试时优化，利用稀疏几何线索适配预训练3D基础模型以完成深度补全。

**关键词**：深度补全, 测试时适应, 参数高效微调, 3D基础模型, 稀疏几何线索, 视频序列优化

## 3 点简述
- 核心问题：传统方法训练任务特定编码器易过拟合，泛化能力差，难以有效利用稀疏观测。
- 方法要点：冻结基础模型主干，仅更新少量参数（如LoRA或VPT），基于推理时稀疏观测的梯度进行测试时优化。
- 实验或效果：在室内外数据集上实现最先进结果，支持视频序列级参数共享以提升鲁棒性和一致性。

## 摘要（原文）

> We introduce CAPA, a parameter-efficient test-time optimization framework that adapts pre-trained 3D foundation models (FMs) for depth completion, using sparse geometric cues. Unlike prior methods that train task-specific encoders for auxiliary inputs, which often overfit and generalize poorly, CAPA freezes the FM backbone. Instead, it updates only a minimal set of parameters using Parameter-Efficient Fine-Tuning (e.g. LoRA or VPT), guided by gradients calculated directly from the sparse observations available at inference time. This approach effectively grounds the foundation model's geometric prior in the scene-specific measurements, correcting distortions and misplaced structures. For videos, CAPA introduces sequence-level parameter sharing, jointly adapting all frames to exploit temporal correlations, improve robustness, and enforce multi-frame consistency. CAPA is model-agnostic, compatible with any ViT-based FM, and achieves state-of-the-art results across diverse condition patterns on both indoor and outdoor datasets. Project page: research.nvidia.com/labs/dvl/projects/capa.

