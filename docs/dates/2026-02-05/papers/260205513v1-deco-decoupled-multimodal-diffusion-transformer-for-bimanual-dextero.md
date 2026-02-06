---
layout: default
title: DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter
---

# DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter
**arXiv**：[2602.05513v1](https://arxiv.org/abs/2602.05513) · [PDF](https://arxiv.org/pdf/2602.05513.pdf)  
**作者**：Xukun Li, Yu Sun, Lei Zhang, Bosheng Huang, Yibo Peng, Yuan Meng, Haojun Jiang, Shaoxuan Xie, Guacai Yao, Alois Knoll, Zhenshan Bing, Xinlong Wang, Zhenguo Sun  

**一句话要点**：提出DECO框架，通过解耦多模态条件实现双手机器人灵巧操作，并附带触觉适配器。

**关键词**：双手机器人操作, 多模态学习, 扩散变换器, 触觉感知, 策略微调, 数据集构建

## 3 点简述
- 核心问题：双手机器人灵巧操作中多模态信号（如图像、触觉）的有效整合与策略学习。
- 方法要点：基于DiT的解耦多模态扩散变换器，使用自适应层归一化和交叉注意力注入不同模态，并采用LoRA适配器微调。
- 实验或效果：构建DECO-50数据集，包含4场景28子任务，超过50小时数据，用于评估策略性能。

## 摘要（原文）

> Overview of the Proposed DECO Framework.} DECO is a DiT-based policy that decouples multimodal conditioning. Image and action tokens interact via joint self attention, while proprioceptive states and optional conditions are injected through adaptive layer normalization. Tactile signals are injected via cross attention, while a lightweight LoRA-based adapter is used to efficiently fine-tune the pretrained policy. DECO is also accompanied by DECO-50, a bimanual dexterous manipulation dataset with tactile sensing, consisting of 4 scenarios and 28 sub-tasks, covering more than 50 hours of data, approximately 5 million frames, and 8,000 successful trajectories.

