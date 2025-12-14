---
layout: default
title: Are We Ready for RL in Text-to-3D Generation? A Progressive Investigation
---

# Are We Ready for RL in Text-to-3D Generation? A Progressive Investigation
**arXiv**：[2512.10949v1](https://arxiv.org/abs/2512.10949) · [PDF](https://arxiv.org/pdf/2512.10949.pdf)  
**作者**：Yiwen Tang, Zoey Guo, Kaixin Zhu, Ray Zhang, Qizhi Chen, Dongzhi Jiang, Junli Liu, Bohan Zeng, Haoming Song, Delin Qu, Tianyi Bai, Dan Xu, Wentao Zhang, Bin Zhao  

**一句话要点**：提出Hi-GRPO和AR3D-R1以解决RL在文本到3D生成中的奖励设计和算法挑战

**关键词**：文本到3D生成, 强化学习, 奖励设计, 层次化优化, 3D基准评估, 自回归生成

## 3 点简述
- 核心问题：3D生成因空间复杂度高，对奖励设计和RL算法敏感，RL应用未充分探索。
- 方法要点：系统研究奖励设计、GRPO算法变体，并引入层次化Hi-GRPO优化全局到局部生成。
- 实验或效果：开发AR3D-R1模型，从粗形状到纹理细化，并发布MME-3DR基准评估推理能力。

## 摘要（原文）

> Reinforcement learning (RL), earlier proven to be effective in large language and multi-modal models, has been successfully extended to enhance 2D image generation recently. However, applying RL to 3D generation remains largely unexplored due to the higher spatial complexity of 3D objects, which require globally consistent geometry and fine-grained local textures. This makes 3D generation significantly sensitive to reward designs and RL algorithms. To address these challenges, we conduct the first systematic study of RL for text-to-3D autoregressive generation across several dimensions. (1) Reward designs: We evaluate reward dimensions and model choices, showing that alignment with human preference is crucial, and that general multi-modal models provide robust signal for 3D attributes. (2) RL algorithms: We study GRPO variants, highlighting the effectiveness of token-level optimization, and further investigate the scaling of training data and iterations. (3) Text-to-3D Benchmarks: Since existing benchmarks fail to measure implicit reasoning abilities in 3D generation models, we introduce MME-3DR. (4) Advanced RL paradigms: Motivated by the natural hierarchy of 3D generation, we propose Hi-GRPO, which optimizes the global-to-local hierarchical 3D generation through dedicated reward ensembles. Based on these insights, we develop AR3D-R1, the first RL-enhanced text-to-3D model, expert from coarse shape to texture refinement. We hope this study provides insights into RL-driven reasoning for 3D generation. Code is released at https://github.com/Ivan-Tang-3D/3DGen-R1.

