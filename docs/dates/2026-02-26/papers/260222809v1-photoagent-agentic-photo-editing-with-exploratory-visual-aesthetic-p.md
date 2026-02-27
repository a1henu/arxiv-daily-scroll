---
layout: default
title: PhotoAgent: Agentic Photo Editing with Exploratory Visual Aesthetic Planning
---

# PhotoAgent: Agentic Photo Editing with Exploratory Visual Aesthetic Planning
**arXiv**：[2602.22809v1](https://arxiv.org/abs/2602.22809) · [PDF](https://arxiv.org/pdf/2602.22809.pdf)  
**作者**：Mingde Yao, Zhiyuan You, Tam-King Man, Menglu Wang, Tianfan Xue  

**一句话要点**：提出PhotoAgent系统，通过显式美学规划实现自主图像编辑，解决指令依赖问题。

**关键词**：自主图像编辑, 美学规划, 树搜索, 闭环执行, 评估基准

## 3 点简述
- 核心问题：基于指令的图像编辑质量高度依赖用户精心设计的指令，任务分解和序列化负担重。
- 方法要点：将自主图像编辑建模为长时程决策问题，通过树搜索规划多步编辑动作，结合记忆和视觉反馈闭环执行。
- 实验或效果：引入UGC-Edit基准和测试集，实验显示PhotoAgent在指令遵循和视觉质量上优于基线方法。

## 摘要（原文）

> With the recent fast development of generative models, instruction-based image editing has shown great potential in generating high-quality images. However, the quality of editing highly depends on carefully designed instructions, placing the burden of task decomposition and sequencing entirely on the user. To achieve autonomous image editing, we present PhotoAgent, a system that advances image editing through explicit aesthetic planning. Specifically, PhotoAgent formulates autonomous image editing as a long-horizon decision-making problem. It reasons over user aesthetic intent, plans multi-step editing actions via tree search, and iteratively refines results through closed-loop execution with memory and visual feedback, without requiring step-by-step user prompts. To support reliable evaluation in real-world scenarios, we introduce UGC-Edit, an aesthetic evaluation benchmark consisting of 7,000 photos and a learned aesthetic reward model. We also construct a test set containing 1,017 photos to systematically assess autonomous photo editing performance. Extensive experiments demonstrate that PhotoAgent consistently improves both instruction adherence and visual quality compared with baseline methods. The project page is https://github.com/mdyao/PhotoAgent.

