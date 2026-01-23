---
layout: default
title: Evolving Without Ending: Unifying Multimodal Incremental Learning for Continual Panoptic Perception
---

# Evolving Without Ending: Unifying Multimodal Incremental Learning for Continual Panoptic Perception
**arXiv**：[2601.15643v1](https://arxiv.org/abs/2601.15643) · [PDF](https://arxiv.org/pdf/2601.15643.pdf)  
**作者**：Bo Yuan, Danpei Zhao, Wentao Li, Tian Li, Zhiguo Jiang  

**一句话要点**：提出持续全景感知模型以解决多模态多任务持续学习中的语义混淆与灾难性遗忘问题

**关键词**：持续全景感知, 多模态持续学习, 知识蒸馏, 跨模态对齐, 灾难性遗忘, 端到端模型

## 3 点简述
- 核心问题：多模态多任务持续学习存在语义混淆和灾难性遗忘，导致模型性能下降
- 方法要点：采用协作跨模态编码器、可塑知识继承模块和跨模态一致性约束，实现端到端持续全景感知
- 实验或效果：在多模态数据集和多样持续学习任务上验证了模型优越性，尤其在细粒度任务中表现突出

## 摘要（原文）

> Continual learning (CL) is a great endeavour in developing intelligent perception AI systems. However, the pioneer research has predominantly focus on single-task CL, which restricts the potential in multi-task and multimodal scenarios. Beyond the well-known issue of catastrophic forgetting, the multi-task CL also brings semantic obfuscation across multimodal alignment, leading to severe model degradation during incremental training steps. In this paper, we extend CL to continual panoptic perception (CPP), integrating multimodal and multi-task CL to enhance comprehensive image perception through pixel-level, instance-level, and image-level joint interpretation. We formalize the CL task in multimodal scenarios and propose an end-to-end continual panoptic perception model. Concretely, CPP model features a collaborative cross-modal encoder (CCE) for multimodal embedding. We also propose a malleable knowledge inheritance module via contrastive feature distillation and instance distillation, addressing catastrophic forgetting from task-interactive boosting manner. Furthermore, we propose a cross-modal consistency constraint and develop CPP+, ensuring multimodal semantic alignment for model updating under multi-task incremental scenarios. Additionally, our proposed model incorporates an asymmetric pseudo-labeling manner, enabling model evolving without exemplar replay. Extensive experiments on multimodal datasets and diverse CL tasks demonstrate the superiority of the proposed model, particularly in fine-grained CL tasks.

