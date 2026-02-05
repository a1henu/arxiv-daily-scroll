---
layout: default
title: REDistill: Robust Estimator Distillation for Balancing Robustness and Efficiency
---

# REDistill: Robust Estimator Distillation for Balancing Robustness and Efficiency
**arXiv**：[2602.04677v1](https://arxiv.org/abs/2602.04677) · [PDF](https://arxiv.org/pdf/2602.04677.pdf)  
**作者**：Ondrej Tybl, Lukas Neumann  

**一句话要点**：提出REDistill框架，基于稳健统计平衡知识蒸馏中的鲁棒性与效率。

**关键词**：知识蒸馏, 稳健统计, 幂散度损失, 模型压缩, 鲁棒性优化, 教师-学生架构

## 3 点简述
- 核心问题：传统知识蒸馏依赖教师模型提供可靠软目标，但实际中教师预测常存在噪声或过度自信，影响学生模型性能。
- 方法要点：引入幂散度损失替代标准KL散度，自适应降低不可靠教师输出的权重，保持信息性logit关系，无需额外超参数调优。
- 实验或效果：在CIFAR-100和ImageNet-1k数据集上验证，REDistill能一致提升学生模型准确率，并展示出强泛化能力。

## 摘要（原文）

> Knowledge Distillation (KD) transfers knowledge from a large teacher model to a smaller student by aligning their predictive distributions. However, conventional KD formulations - typically based on Kullback-Leibler divergence - assume that the teacher provides reliable soft targets. In practice, teacher predictions are often noisy or overconfident, and existing correction-based approaches rely on ad-hoc heuristics and extensive hyper-parameter tuning, which hinders generalization. We introduce REDistill (Robust Estimator Distillation), a simple yet principled framework grounded in robust statistics. REDistill replaces the standard KD objective with a power divergence loss, a generalization of KL divergence that adaptively downweights unreliable teacher output while preserving informative logit relationships. This formulation provides a unified and interpretable treatment of teacher noise, requires only logits, integrates seamlessly into existing KD pipelines, and incurs negligible computational overhead. Extensive experiments on CIFAR-100 and ImageNet-1k demonstrate that REDistill consistently improves student accuracy in diverse teacher-student architectures. Remarkably, it achieves these gains without model-specific hyper-parameter tuning, underscoring its robustness and strong generalization to unseen teacher-student pairs.

