---
layout: default
title: Instruction-based Image Editing with Planning, Reasoning, and Generation
---

# Instruction-based Image Editing with Planning, Reasoning, and Generation
**arXiv**：[2602.22624v1](https://arxiv.org/abs/2602.22624) · [PDF](https://arxiv.org/pdf/2602.22624.pdf)  
**作者**：Liya Ji, Chenyang Qi, Qifeng Chen  

**一句话要点**：提出基于多模态思维链的指令图像编辑方法，以提升复杂场景下的编辑质量

**关键词**：指令图像编辑, 多模态思维链, 区域推理, 扩散模型, 场景理解

## 3 点简述
- 核心问题：现有方法依赖单模态理解模型，限制复杂指令图像编辑的质量
- 方法要点：采用多模态思维链，包括规划、区域推理和生成，以桥接理解与生成
- 实验或效果：在复杂真实图像上展示出竞争力的编辑能力

## 摘要（原文）

> Editing images via instruction provides a natural way to generate interactive content, but it is a big challenge due to the higher requirement of scene understanding and generation. Prior work utilizes a chain of large language models, object segmentation models, and editing models for this task. However, the understanding models provide only a single modality ability, restricting the editing quality. We aim to bridge understanding and generation via a new multi-modality model that provides the intelligent abilities to instruction-based image editing models for more complex cases. To achieve this goal, we individually separate the instruction editing task with the multi-modality chain of thought prompts, i.e., Chain-of-Thought (CoT) planning, editing region reasoning, and editing. For Chain-of-Thought planning, the large language model could reason the appropriate sub-prompts considering the instruction provided and the ability of the editing network. For editing region reasoning, we train an instruction-based editing region generation network with a multi-modal large language model. Finally, a hint-guided instruction-based editing network is proposed for editing image generations based on the sizeable text-to-image diffusion model to accept the hints for generation. Extensive experiments demonstrate that our method has competitive editing abilities on complex real-world images.

