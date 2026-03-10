---
layout: default
title: Video2LoRA: Unified Semantic-Controlled Video Generation via Per-Reference-Video LoRA
---

# Video2LoRA: Unified Semantic-Controlled Video Generation via Per-Reference-Video LoRA
**arXiv**：[2603.08210v1](https://arxiv.org/abs/2603.08210) · [PDF](https://arxiv.org/pdf/2603.08210.pdf)  
**作者**：Zexi Wu, Qinghe Wang, Jing Dai, Baolu Li, Yiming Zhang, Yue Ma, Xu Jia, Hongming Xu  

**一句话要点**：提出Video2LoRA框架，通过每参考视频LoRA实现统一语义控制视频生成。

**关键词**：语义控制视频生成, LoRA模块, 零样本泛化, 轻量超网络, 扩散模型

## 3 点简述
- 核心问题：现有方法在语义对齐上存在刚性约束或缺乏互操作性，阻碍灵活高效视频生成。
- 方法要点：使用轻量超网络预测个性化LoRA权重，结合辅助矩阵形成自适应模块，集成到冻结扩散主干。
- 实验或效果：模型权重小于150MB，实现跨条件语义对齐生成，并展示零样本泛化能力。

## 摘要（原文）

> Achieving semantic alignment across diverse video generation conditions remains a significant challenge. Methods that rely on explicit structural guidance often enforce rigid spatial constraints that limit semantic flexibility, whereas models tailored for individual control types lack interoperability and adaptability. These design bottlenecks hinder progress toward flexible and efficient semantic video generation. To address this, we propose Video2LoRA, a scalable and generalizable framework for semantic-controlled video generation that conditions on a reference video. Video2LoRA employs a lightweight hypernetwork to predict personalized LoRA weights for each semantic input, which are combined with auxiliary matrices to form adaptive LoRA modules integrated into a frozen diffusion backbone. This design enables the model to generate videos consistent with the reference semantics while preserving key style and content variations, eliminating the need for any per-condition training. Notably, the final model weights less than 150MB, making it highly efficient for storage and deployment. Video2LoRA achieves coherent, semantically aligned generation across diverse conditions and exhibits strong zero-shot generalization to unseen semantics.

