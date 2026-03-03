---
layout: default
title: FastLightGen: Fast and Light Video Generation with Fewer Steps and Parameters
---

# FastLightGen: Fast and Light Video Generation with Fewer Steps and Parameters
**arXiv**：[2603.01685v1](https://arxiv.org/abs/2603.01685) · [PDF](https://arxiv.org/pdf/2603.01685.pdf)  
**作者**：Shao Shitong, Gu Yufei, Xie Zeke  

**一句话要点**：提出FastLightGen算法，通过协同蒸馏模型大小与推理步骤，实现快速轻量视频生成。

**关键词**：视频生成, 模型蒸馏, 推理加速, 参数剪枝, 轻量化模型

## 3 点简述
- 核心问题：现有视频生成模型因参数多、推理步骤多导致计算开销大，阻碍实际部署。
- 方法要点：构建最优教师模型，在协同框架中同时蒸馏模型大小和推理步骤，生成快速轻量学生模型。
- 实验或效果：在HunyuanVideo-ATI2V和WanX-TI2V上，4步采样和30%参数剪枝在受限推理预算下达到最优视觉质量，超越现有方法。

## 摘要（原文）

> The recent advent of powerful video generation models, such as Hunyuan, WanX, Veo3, and Kling, has inaugurated a new era in the field. However, the practical deployment of these models is severely impeded by their substantial computational overhead, which stems from enormous parameter counts and the iterative, multi-step sampling process required during inference. Prior research on accelerating generative models has predominantly followed two distinct trajectories: reducing the number of sampling steps (e.g., LCM, DMD, and MagicDistillation) or compressing the model size for more efficient inference (e.g., ICMD). The potential of simultaneously compressing both to create a fast and lightweight model remains an unexplored avenue. In this paper, we propose FastLightGen, an algorithm that transforms large, computationally expensive models into fast, lightweight counterparts. The core idea is to construct an optimal teacher model, one engineered to maximize student performance, within a synergistic framework for distilling both model size and inference steps. Our extensive experiments on HunyuanVideo-ATI2V and WanX-TI2V reveal that a generator using 4-step sampling and 30\% parameter pruning achieves optimal visual quality under a constrained inference budget. Furthermore, FastLightGen consistently outperforms all competing methods, establishing a new state-of-the-art in efficient video generation.

