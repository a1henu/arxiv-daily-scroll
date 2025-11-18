---
layout: default
title: InterMoE: Individual-Specific 3D Human Interaction Generation via Dynamic Temporal-Selective MoE
---

# InterMoE: Individual-Specific 3D Human Interaction Generation via Dynamic Temporal-Selective MoE
**arXiv**：[2511.13488v1](https://arxiv.org/abs/2511.13488) · [PDF](https://arxiv.org/pdf/2511.13488.pdf)  
**作者**：Lipeng Wang, Hongxing Fan, Haohua Chen, Zehuan Huang, Lu Sheng  

**一句话要点**：提出InterMoE框架以解决3D人体交互生成中个体特征保持和语义忠实度问题

**关键词**：3D人体交互生成, 混合专家模型, 动态路由机制, 语义忠实度, 个体特征保持

## 3 点简述
- 核心问题：现有方法难以保持个体特征和文本描述忠实度
- 方法要点：使用动态时间选择性MoE，结合文本语义和运动上下文路由特征
- 实验或效果：在InterHuman和InterX数据集上FID分数分别降低9%和22%

## 摘要（原文）

> Generating high-quality human interactions holds significant value for applications like virtual reality and robotics. However, existing methods often fail to preserve unique individual characteristics or fully adhere to textual descriptions. To address these challenges, we introduce InterMoE, a novel framework built on a Dynamic Temporal-Selective Mixture of Experts. The core of InterMoE is a routing mechanism that synergistically uses both high-level text semantics and low-level motion context to dispatch temporal motion features to specialized experts. This allows experts to dynamically determine the selection capacity and focus on critical temporal features, thereby preserving specific individual characteristic identities while ensuring high semantic fidelity. Extensive experiments show that InterMoE achieves state-of-the-art performance in individual-specific high-fidelity 3D human interaction generation, reducing FID scores by 9% on the InterHuman dataset and 22% on InterX.

