---
layout: default
title: Late-to-Early Training: LET LLMs Learn Earlier, So Faster and Better
---

# Late-to-Early Training: LET LLMs Learn Earlier, So Faster and Better
**arXiv**：[2602.05393v1](https://arxiv.org/abs/2602.05393) · [PDF](https://arxiv.org/pdf/2602.05393.pdf)  
**作者**：Ji Zhao, Yufei Gu, Shitong Shao, Xun Zhou, Liang Xiang, Zeke Xie  

**一句话要点**：提出Late-to-Early Training范式，利用小预训练模型加速大模型训练

**关键词**：大语言模型, 预训练加速, 知识迁移, 训练范式, 模型缩放

## 3 点简述
- 核心问题：如何利用现有小预训练模型加速大模型训练，降低计算成本
- 方法要点：通过晚期层表示指导早期层，实现晚期知识在早期步骤和层的学习
- 实验或效果：在1.4B和7B模型上验证，加速达1.6倍，下游任务准确率提升近5%

## 摘要（原文）

> As Large Language Models (LLMs) achieve remarkable empirical success through scaling model and data size, pretraining has become increasingly critical yet computationally prohibitive, hindering rapid development. Despite the availability of numerous pretrained LLMs developed at significant computational expense, a fundamental real-world question remains underexplored: \textit{Can we leverage existing small pretrained models to accelerate the training of larger models?} In this paper, we propose a Late-to-Early Training (LET) paradigm that enables LLMs to explicitly learn later knowledge in earlier steps and earlier layers. The core idea is to guide the early layers of an LLM during early training using representations from the late layers of a pretrained (i.e. late training phase) model. We identify two key mechanisms that drive LET's effectiveness: late-to-early-step learning and late-to-early-layer learning. These mechanisms significantly accelerate training convergence while robustly enhancing both language modeling capabilities and downstream task performance, enabling faster training with superior performance. Extensive experiments on 1.4B and 7B parameter models demonstrate LET's efficiency and effectiveness. Notably, when training a 1.4B LLM on the Pile dataset, our method achieves up to 1.6$\times$ speedup with nearly 5\% improvement in downstream task accuracy compared to standard training, even when using a pretrained model with 10$\times$ fewer parameters than the target model.

