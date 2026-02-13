---
layout: default
title: How Well Do Large-Scale Chemical Language Models Transfer to Downstream Tasks?
---

# How Well Do Large-Scale Chemical Language Models Transfer to Downstream Tasks?
**arXiv**：[2602.11618v1](https://arxiv.org/abs/2602.11618) · [PDF](https://arxiv.org/pdf/2602.11618.pdf)  
**作者**：Tatsuya Sagawa, Ryosuke Kojima  

**一句话要点**：评估化学语言模型预训练资源扩展对下游分子属性预测任务性能的影响

**关键词**：化学语言模型, 分子属性预测, 预训练扩展, 迁移性能评估, 任务依赖分析

## 3 点简述
- 核心问题：验证化学语言模型预训练资源增加是否提升下游任务性能，发现预训练损失下降但下游性能改善有限
- 方法要点：通过扩展模型大小、数据集规模和训练计算资源预训练CLMs，并测量在多样分子属性预测任务上的迁移性能
- 实验或效果：识别下游性能饱和或下降的条件，分析任务依赖的失败模式，强调需考虑下游任务特性的评估策略

## 摘要（原文）

> Chemical Language Models (CLMs) pre-trained on large scale molecular data are widely used for molecular property prediction. However, the common belief that increasing training resources such as model size, dataset size, and training compute improves both pretraining loss and downstream task performance has not been systematically validated in the chemical domain. In this work, we evaluate this assumption by pretraining CLMs while scaling training resources and measuring transfer performance across diverse molecular property prediction (MPP) tasks. We find that while pretraining loss consistently decreases with increased training resources, downstream task performance shows limited improvement. Moreover, alternative metrics based on the Hessian or loss landscape also fail to estimate downstream performance in CLMs. We further identify conditions under which downstream performance saturates or degrades despite continued improvements in pretraining metrics, and analyze the underlying task dependent failure modes through parameter space visualizations. These results expose a gap between pretraining based evaluation and downstream performance, and emphasize the need for model selection and evaluation strategies that explicitly account for downstream task characteristics.

