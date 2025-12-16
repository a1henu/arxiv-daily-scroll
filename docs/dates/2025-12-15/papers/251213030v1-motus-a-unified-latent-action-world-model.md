---
layout: default
title: Motus: A Unified Latent Action World Model
---

# Motus: A Unified Latent Action World Model
**arXiv**：[2512.13030v1](https://arxiv.org/abs/2512.13030) · [PDF](https://arxiv.org/pdf/2512.13030.pdf)  
**作者**：Hongzhe Bi, Hengkai Tan, Shenghao Xie, Zeyuan Wang, Shuhe Huang, Haitian Liu, Ruowen Zhao, Yao Feng, Chendong Xiang, Yinze Rong, Hongyan Zhao, Hanyu Liu, Zhizhong Su, Lei Ma, Hang Su, Jun Zhu  

**一句话要点**：提出Motus统一潜在动作世界模型，以解决具身智能中模型碎片化问题。

**关键词**：统一世界模型, 潜在动作学习, 混合Transformer, 多模态生成, 机器人控制, 光流分析

## 3 点简述
- 核心问题：当前具身智能方法依赖孤立模型，阻碍多模态生成能力统一和大规模异构数据学习。
- 方法要点：采用混合Transformer架构集成专家，结合光流学习潜在动作，支持灵活建模模式切换。
- 实验或效果：在仿真和真实场景中优于现有方法，提升性能达11%~48%，验证统一建模对下游机器人任务有益。

## 摘要（原文）

> While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios(improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

