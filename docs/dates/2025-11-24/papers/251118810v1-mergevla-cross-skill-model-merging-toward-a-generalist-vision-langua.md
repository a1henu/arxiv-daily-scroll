---
layout: default
title: MergeVLA: Cross-Skill Model Merging Toward a Generalist Vision-Language-Action Agent
---

# MergeVLA: Cross-Skill Model Merging Toward a Generalist Vision-Language-Action Agent
**arXiv**：[2511.18810v1](https://arxiv.org/abs/2511.18810) · [PDF](https://arxiv.org/pdf/2511.18810.pdf)  
**作者**：Yuxia Fu, Zhizhen Zhang, Yuqi Zhang, Zijian Wang, Zi Huang, Yadan Luo  

**一句话要点**：提出MergeVLA架构以解决视觉-语言-动作模型多技能合并难题

**关键词**：模型合并, 视觉-语言-动作模型, 稀疏激活, 交叉注意力, 任务路由, 机器人学习

## 3 点简述
- 核心问题：VLA模型微调后参数分歧与自注意力依赖阻碍多技能合并
- 方法要点：使用稀疏激活LoRA适配器和仅交叉注意力块保持参数一致性与模块化
- 实验或效果：在多个数据集和真实机器人上实现与专家模型相当或更优性能

## 摘要（原文）

> Recent Vision-Language-Action (VLA) models reformulate vision-language models by tuning them with millions of robotic demonstrations. While they perform well when fine-tuned for a single embodiment or task family, extending them to multi-skill settings remains challenging: directly merging VLA experts trained on different tasks results in near-zero success rates. This raises a fundamental question: what prevents VLAs from mastering multiple skills within one model? With an empirical decomposition of learnable parameters during VLA fine-tuning, we identify two key sources of non-mergeability: (1) Finetuning drives LoRA adapters in the VLM backbone toward divergent, task-specific directions beyond the capacity of existing merging methods to unify. (2) Action experts develop inter-block dependencies through self-attention feedback, causing task information to spread across layers and preventing modular recombination. To address these challenges, we present MergeVLA, a merging-oriented VLA architecture that preserves mergeability by design. MergeVLA introduces sparsely activated LoRA adapters via task masks to retain consistent parameters and reduce irreconcilable conflicts in the VLM. Its action expert replaces self-attention with cross-attention-only blocks to keep specialization localized and composable. When the task is unknown, it uses a test-time task router to adaptively select the appropriate task mask and expert head from the initial observation, enabling unsupervised task inference. Across LIBERO, LIBERO-Plus, RoboTwin, and multi-task experiments on the real SO101 robotic arm, MergeVLA achieves performance comparable to or even exceeding individually finetuned experts, demonstrating robust generalization across tasks, embodiments, and environments.

