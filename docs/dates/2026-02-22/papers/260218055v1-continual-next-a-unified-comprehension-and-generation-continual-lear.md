---
layout: default
title: Continual-NExT: A Unified Comprehension And Generation Continual Learning Framework
---

# Continual-NExT: A Unified Comprehension And Generation Continual Learning Framework
**arXiv**：[2602.18055v1](https://arxiv.org/abs/2602.18055) · [PDF](https://arxiv.org/pdf/2602.18055.pdf)  
**作者**：Jingyang Qiao, Zhizhong Zhang, Xin Tan, Jingyu Gong, Yanyun Qu, Yuan Xie  

**一句话要点**：提出Continual-NExT框架与MAGE方法以解决双模态大语言模型在持续学习中的遗忘与知识迁移问题。

**关键词**：持续学习, 双模态大语言模型, 灾难性遗忘, 跨模态知识迁移, LoRA方法, 评估指标

## 3 点简述
- 核心问题：双模态大语言模型在持续学习中面临灾难性遗忘、幻觉、指令不遵循和跨模态知识迁移失败等挑战。
- 方法要点：设计MAGE方法，通过混合和聚合通用LoRA与专家LoRA来促进跨模态知识迁移并减轻遗忘。
- 实验或效果：MAGE在实验中优于其他持续学习方法，实现了最先进的性能。

## 摘要（原文）

> Dual-to-Dual MLLMs refer to Multimodal Large Language Models, which can enable unified multimodal comprehension and generation through text and image modalities. Although exhibiting strong instantaneous learning and generalization capabilities, Dual-to-Dual MLLMs still remain deficient in lifelong evolution, significantly affecting continual adaptation to dynamic real-world scenarios. One of the challenges is that learning new tasks inevitably destroys the learned knowledge. Beyond traditional catastrophic forgetting, Dual-to-Dual MLLMs face other challenges, including hallucination, instruction unfollowing, and failures in cross-modal knowledge transfer. However, no standardized continual learning framework for Dual-to-Dual MLLMs has been established yet, leaving these challenges unexplored. Thus, in this paper, we establish Continual-NExT, a continual learning framework for Dual-to-Dual MLLMs with deliberately-architected evaluation metrics. To improve the continual learning capability of Dual-to-Dual MLLMs, we propose an efficient MAGE (Mixture and Aggregation of General LoRA and Expert LoRA) method to further facilitate knowledge transfer across modalities and mitigate forgetting. Extensive experiments demonstrate that MAGE outperforms other continual learning methods and achieves state-of-the-art performance.

