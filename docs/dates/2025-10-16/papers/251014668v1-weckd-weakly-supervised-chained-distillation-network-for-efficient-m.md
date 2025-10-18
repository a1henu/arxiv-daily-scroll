---
layout: default
title: WeCKD: Weakly-supervised Chained Distillation Network for Efficient Multimodal Medical Imaging
---

# WeCKD: Weakly-supervised Chained Distillation Network for Efficient Multimodal Medical Imaging
**arXiv**：[2510.14668v1](https://arxiv.org/abs/2510.14668) · [PDF](https://arxiv.org/pdf/2510.14668.pdf)  
**作者**：Md. Abdur Rahman, Mohaimenul Azam Khan Raiaan, Sami Azam, Asif Karim, Jemima Beissbarth, Amanda Leach  

**一句话要点**：提出弱监督链式蒸馏网络以解决有限数据下医学图像分析问题

**关键词**：知识蒸馏, 弱监督学习, 医学图像分析, 链式结构, 多模态成像

## 3 点简述
- 传统知识蒸馏依赖强教师或大标注数据，易导致知识退化与效率低下
- 采用链式结构，模型逐级学习并精炼知识，减少数据依赖并增强特征学习
- 在多个医学图像数据集上验证，性能超越监督方法，准确率提升高达23%

## 摘要（原文）

> Knowledge distillation (KD) has traditionally relied on a static
> teacher-student framework, where a large, well-trained teacher transfers
> knowledge to a single student model. However, these approaches often suffer
> from knowledge degradation, inefficient supervision, and reliance on either a
> very strong teacher model or large labeled datasets, which limits their
> effectiveness in real-world, limited-data scenarios. To address these, we
> present the first-ever Weakly-supervised Chain-based KD network (WeCKD) that
> redefines knowledge transfer through a structured sequence of interconnected
> models. Unlike conventional KD, it forms a progressive distillation chain,
> where each model not only learns from its predecessor but also refines the
> knowledge before passing it forward. This structured knowledge transfer further
> enhances feature learning, reduces data dependency, and mitigates the
> limitations of one-step KD. Each model in the distillation chain is trained on
> only a fraction of the dataset and demonstrates that effective learning can be
> achieved with minimal supervision. Extensive evaluations across four otoscopic
> imaging datasets demonstrate that it not only matches but in many cases
> surpasses the performance of existing supervised methods. Experimental results
> on two other datasets further underscore its generalization across diverse
> medical imaging modalities, including microscopic and magnetic resonance
> imaging. Furthermore, our evaluations resulted in cumulative accuracy gains of
> up to +23% over a single backbone trained on the same limited data, which
> highlights its potential for real-world adoption.

