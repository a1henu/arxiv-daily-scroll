---
layout: default
title: DreamHome-Pano: Design-Aware and Conflict-Free Panoramic Interior Generation
---

# DreamHome-Pano: Design-Aware and Conflict-Free Panoramic Interior Generation
**arXiv**：[2602.06494v1](https://arxiv.org/abs/2602.06494) · [PDF](https://arxiv.org/pdf/2602.06494.pdf)  
**作者**：Lulu Chen, Yijiang Hu, Yuanqing Liu, Yulong Li, Yue Yang  

**一句话要点**：提出DreamHome-Pano框架，通过Prompt-LLM和冲突控制解决室内全景生成中的条件冲突问题。

**关键词**：全景室内生成, 条件冲突控制, Prompt-LLM, 多条件解耦, 结构感知先验, 强化学习训练

## 3 点简述
- 核心问题：现有多条件生成框架在室内设计中难以平衡结构约束与风格偏好，导致条件冲突。
- 方法要点：引入Prompt-LLM作为语义桥梁，结合冲突控制架构，实现跨模态对齐和结构完整性保护。
- 实验或效果：建立全景室内基准和多阶段训练管道，实验显示在美学质量和结构一致性上取得优越平衡。

## 摘要（原文）

> In modern interior design, the generation of personalized spaces frequently necessitates a delicate balance between rigid architectural structural constraints and specific stylistic preferences. However, existing multi-condition generative frameworks often struggle to harmonize these inputs, leading to "condition conflicts" where stylistic attributes inadvertently compromise the geometric precision of the layout. To address this challenge, we present DreamHome-Pano, a controllable panoramic generation framework designed for high-fidelity interior synthesis. Our approach introduces a Prompt-LLM that serves as a semantic bridge, effectively translating layout constraints and style references into professional descriptive prompts to achieve precise cross-modal alignment. To safeguard architectural integrity during the generative process, we develop a Conflict-Free Control architecture that incorporates structural-aware geometric priors and a multi-condition decoupling strategy, effectively suppressing stylistic interference from eroding the spatial layout. Furthermore, we establish a comprehensive panoramic interior benchmark alongside a multi-stage training pipeline, encompassing progressive Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). Experimental results demonstrate that DreamHome-Pano achieves a superior balance between aesthetic quality and structural consistency, offering a robust and professional-grade solution for panoramic interior visualization.

