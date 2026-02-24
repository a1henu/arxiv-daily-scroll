---
layout: default
title: RL-RIG: A Generative Spatial Reasoner via Intrinsic Reflection
---

# RL-RIG: A Generative Spatial Reasoner via Intrinsic Reflection
**arXiv**：[2602.19974v1](https://arxiv.org/abs/2602.19974) · [PDF](https://arxiv.org/pdf/2602.19974.pdf)  
**作者**：Tianyu Wang, Zhiyuan Ma, Qian Wang, Xinyi Zhang, Xinwei Long, Bowen Zhou  

**一句话要点**：提出RL-RIG强化学习框架，通过内在反思解决图像生成中的空间推理难题

**关键词**：图像生成, 空间推理, 强化学习, 内在反思, 场景图评估

## 3 点简述
- 现有图像生成模型在捕捉细粒度空间关系方面存在不足，导致结构不合理
- 采用Generate-Reflect-Edit范式，结合Diffuser、Checker、Actor和Inverse Diffuser组件提升空间推理能力
- 在LAION-SG数据集上，通过Scene Graph IoU和VLM-as-a-Judge评估，空间准确性提升达11%

## 摘要（原文）

> Recent advancements in image generation have achieved impressive results in producing high-quality images. However, existing image generation models still generally struggle with a spatial reasoning dilemma, lacking the ability to accurately capture fine-grained spatial relationships from the prompt and correctly generate scenes with structural integrity. To mitigate this dilemma, we propose RL-RIG, a Reinforcement Learning framework for Reflection-based Image Generation. Our architecture comprises four primary components: Diffuser, Checker, Actor, and Inverse Diffuser, following a Generate-Reflect-Edit paradigm to spark the Chain of Thought reasoning ability in image generation for addressing the dilemma. To equip the model with better intuition over generation trajectories, we further develop Reflection-GRPO to train the VLM Actor for edit prompts and the Image Editor for better image quality under a given prompt, respectively. Unlike traditional approaches that solely produce visually stunning yet structurally unreasonable content, our evaluation metrics prioritize spatial accuracy, utilizing Scene Graph IoU and employing a VLM-as-a-Judge strategy to assess the spatial consistency of generated images on LAION-SG dataset. Experimental results show that RL-RIG outperforms existing state-of-the-art open-source models by up to 11% in terms of controllable and precise spatial reasoning in image generation.

