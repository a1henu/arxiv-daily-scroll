---
layout: default
title: pMoE: Prompting Diverse Experts Together Wins More in Visual Adaptation
---

# pMoE: Prompting Diverse Experts Together Wins More in Visual Adaptation
**arXiv**：[2602.22938v1](https://arxiv.org/abs/2602.22938) · [PDF](https://arxiv.org/pdf/2602.22938.pdf)  
**作者**：Shentong Mo, Xufang Luo, Dongsheng Li  

**一句话要点**：提出pMoE方法，通过多专家提示调优提升视觉适应任务的性能与效率。

**关键词**：视觉适应, 提示调优, 多专家模型, 参数高效微调, 分类与分割

## 3 点简述
- 核心问题：现有提示调优方法通常依赖单一预训练模型，忽略了多领域知识融合的潜力。
- 方法要点：引入专家专用提示令牌和可学习调度器，动态整合多专家知识于统一框架。
- 实验或效果：在47个适应任务中验证，pMoE在性能提升和计算效率间取得最优平衡。

## 摘要（原文）

> Parameter-efficient fine-tuning has demonstrated promising results across various visual adaptation tasks, such as classification and segmentation. Typically, prompt tuning techniques have harnessed knowledge from a single pre-trained model, whether from a general or a specialized medical domain. However, this approach typically overlooks the potential synergies that could arise from integrating diverse domain knowledge within the same tuning process. In this work, we propose a novel Mixture-of-Experts prompt tuning method called pMoE, which leverages the strengths of multiple expert domains through expert-specialized prompt tokens and the learnable dispatcher, effectively combining their expertise in a unified model framework. Our pMoE introduces expert-specific prompt tokens and utilizes a dynamic token dispatching mechanism at various prompt layers to optimize the contribution of each domain expert during the adaptation phase. By incorporating both domain knowledge from diverse experts, the proposed pMoE significantly enhances the model's versatility and applicability to a broad spectrum of tasks. We conduct extensive experiments across 47 adaptation tasks, including both classification and segmentation in general and medical domains. The results demonstrate that our pMoE not only achieves superior performance with a large margin of improvements but also offers an optimal trade-off between computational efficiency and adaptation effectiveness compared to existing methods.

