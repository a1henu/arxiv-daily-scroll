---
layout: default
title: Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment
---

# Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment
**arXiv**：[2602.12281v1](https://arxiv.org/abs/2602.12281) · [PDF](https://arxiv.org/pdf/2602.12281.pdf)  
**作者**：Jacky Kwok, Xilun Zhang, Mengdi Xu, Yuejiang Liu, Azalia Mirhoseini, Chelsea Finn, Marco Pavone  

**一句话要点**：提出CoVer验证框架，通过测试时缩放提升视觉-语言-动作对齐效果

**关键词**：视觉-语言-动作对齐, 测试时验证, 缩放定律, 对比学习, 机器人指令跟随, 意图-动作差距

## 3 点简述
- 核心问题：VLA模型生成动作与指令存在对齐差距，影响机器人通用性。
- 方法要点：引入测试时验证，联合缩放重述指令和生成动作以增加样本多样性，设计对比验证器CoVer。
- 实验或效果：在SIMPLER和PolaRiS基准上实现显著性能提升，优于策略预训练缩放。

## 摘要（原文）

> The long-standing vision of general-purpose robots hinges on their ability to understand and act upon natural language instructions. Vision-Language-Action (VLA) models have made remarkable progress toward this goal, yet their generated actions can still misalign with the given instructions. In this paper, we investigate test-time verification as a means to shrink the "intention-action gap.'' We first characterize the test-time scaling law for embodied instruction following and demonstrate that jointly scaling the number of rephrased instructions and generated actions greatly increases test-time sample diversity, often recovering correct actions more efficiently than scaling each dimension independently. To capitalize on these scaling laws, we present CoVer, a contrastive verifier for vision-language-action alignment, and show that our architecture scales gracefully with additional computational resources and data. We then introduce "boot-time compute" and a hierarchical verification inference pipeline for VLAs. At deployment, our framework precomputes a diverse set of rephrased instructions from a Vision-Language-Model (VLM), repeatedly generates action candidates for each instruction, and then uses a verifier to select the optimal high-level prompt and low-level action chunks. Compared to scaling policy pre-training on the same data, our verification approach yields 22% gains in-distribution and 13% out-of-distribution on the SIMPLER benchmark, with a further 45% improvement in real-world experiments. On the PolaRiS benchmark, CoVer achieves 14% gains in task progress and 9% in success rate.

