---
layout: default
title: Multimodal Continual Instruction Tuning with Dynamic Gradient Guidance
---

# Multimodal Continual Instruction Tuning with Dynamic Gradient Guidance
**arXiv**：[2511.15164v1](https://arxiv.org/abs/2511.15164) · [PDF](https://arxiv.org/pdf/2511.15164.pdf)  
**作者**：Songze Li, Mingyu Gao, Tonghua Su, Xu-Yao Zhang, Zhongjie Wang  

**一句话要点**：提出动态梯度引导方法以解决多模态持续指令调优中的灾难性遗忘问题

**关键词**：多模态持续学习, 灾难性遗忘, 梯度引导, 指令调优, 参数空间几何, 伯努利采样

## 3 点简述
- 核心问题：多模态持续学习面临灾难性遗忘，新任务学习导致旧任务性能下降
- 方法要点：利用参数空间几何特性近似缺失梯度，结合重放缓冲和伯努利采样平衡稳定性与可塑性
- 实验或效果：在数据集上实现先进性能，无需模型扩展，有效缓解遗忘并保持紧凑架构

## 摘要（原文）

> Multimodal continual instruction tuning enables multimodal large language models to sequentially adapt to new tasks while building upon previously acquired knowledge. However, this continual learning paradigm faces the significant challenge of catastrophic forgetting, where learning new tasks leads to performance degradation on previous ones. In this paper, we introduce a novel insight into catastrophic forgetting by conceptualizing it as a problem of missing gradients from old tasks during new task learning. Our approach approximates these missing gradients by leveraging the geometric properties of the parameter space, specifically using the directional vector between current parameters and previously optimal parameters as gradient guidance. This approximated gradient can be further integrated with real gradients from a limited replay buffer and regulated by a Bernoulli sampling strategy that dynamically balances model stability and plasticity. Extensive experiments on multimodal continual instruction tuning datasets demonstrate that our method achieves state-of-the-art performance without model expansion, effectively mitigating catastrophic forgetting while maintaining a compact architecture.

