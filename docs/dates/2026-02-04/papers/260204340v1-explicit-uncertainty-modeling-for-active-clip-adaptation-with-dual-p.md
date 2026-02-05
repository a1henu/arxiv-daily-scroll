---
layout: default
title: Explicit Uncertainty Modeling for Active CLIP Adaptation with Dual Prompt Tuning
---

# Explicit Uncertainty Modeling for Active CLIP Adaptation with Dual Prompt Tuning
**arXiv**：[2602.04340v1](https://arxiv.org/abs/2602.04340) · [PDF](https://arxiv.org/pdf/2602.04340.pdf)  
**作者**：Qian-Wei Wang, Yaguang Song, Shu-Tao Xia  

**一句话要点**：提出基于双提示调优的显式不确定性建模框架，以解决主动学习下CLIP适应中样本选择问题。

**关键词**：CLIP适应, 主动学习, 不确定性建模, 提示调优, 图像分类

## 3 点简述
- 核心问题：CLIP模型在有限标注预算下适应下游分类任务时，现有方法未从模型角度显式建模不确定性。
- 方法要点：引入正负双提示，正提示增强分类可靠性，负提示显式建模预测正确概率以指导主动样本选择。
- 实验或效果：在不同微调范式下，该方法在相同标注预算下一致优于现有主动学习方法。

## 摘要（原文）

> Pre-trained vision-language models such as CLIP exhibit strong transferability, yet adapting them to downstream image classification tasks under limited annotation budgets remains challenging. In active learning settings, the model must select the most informative samples for annotation from a large pool of unlabeled data. Existing approaches typically estimate uncertainty via entropy-based criteria or representation clustering, without explicitly modeling uncertainty from the model perspective. In this work, we propose a robust uncertainty modeling framework for active CLIP adaptation based on dual-prompt tuning. We introduce two learnable prompts in the textual branch of CLIP. The positive prompt enhances the discriminability of task-specific textual embeddings corresponding to light-weight tuned visual embeddings, improving classification reliability. Meanwhile, the negative prompt is trained in an reversed manner to explicitly model the probability that the predicted label is correct, providing a principled uncertainty signal for guiding active sample selection. Extensive experiments across different fine-tuning paradigms demonstrate that our method consistently outperforms existing active learning methods under the same annotation budget.

