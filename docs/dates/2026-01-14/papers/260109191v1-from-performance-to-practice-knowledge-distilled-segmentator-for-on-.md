---
layout: default
title: From Performance to Practice: Knowledge-Distilled Segmentator for On-Premises Clinical Workflows
---

# From Performance to Practice: Knowledge-Distilled Segmentator for On-Premises Clinical Workflows
**arXiv**：[2601.09191v1](https://arxiv.org/abs/2601.09191) · [PDF](https://arxiv.org/pdf/2601.09191.pdf)  
**作者**：Qizhen Lan, Aaron Choi, Jun Ma, Bo Wang, Zhaogming Zhao, Xiaoqian Jiang, Yu-Chun Hsu  

**一句话要点**：提出基于知识蒸馏的部署框架，将高性能分割模型转化为紧凑学生模型，以解决本地临床工作流中的计算资源限制问题。

**关键词**：医学图像分割, 知识蒸馏, 本地部署, 计算效率, 临床工作流, 模型压缩

## 3 点简述
- 核心问题：本地临床工作流中，高性能分割模型因计算需求大而难以部署和维护。
- 方法要点：通过知识蒸馏生成紧凑学生模型，保持架构兼容性，无需修改推理流程。
- 实验或效果：在脑MRI数据集上，参数减少94%时，分割精度保留98.7%，CPU推理延迟降低67%。

## 摘要（原文）

> Deploying medical image segmentation models in routine clinical workflows is often constrained by on-premises infrastructure, where computational resources are fixed and cloud-based inference may be restricted by governance and security policies. While high-capacity models achieve strong segmentation accuracy, their computational demands hinder practical deployment and long-term maintainability in hospital environments. We present a deployment-oriented framework that leverages knowledge distillation to translate a high-performing segmentation model into a scalable family of compact student models, without modifying the inference pipeline. The proposed approach preserves architectural compatibility with existing clinical systems while enabling systematic capacity reduction. The framework is evaluated on a multi-site brain MRI dataset comprising 1,104 3D volumes, with independent testing on 101 curated cases, and is further examined on abdominal CT to assess cross-modality generalizability. Under aggressive parameter reduction (94%), the distilled student model preserves nearly all of the teacher's segmentation accuracy (98.7%), while achieving substantial efficiency gains, including up to a 67% reduction in CPU inference latency without additional deployment overhead. These results demonstrate that knowledge distillation provides a practical and reliable pathway for converting research-grade segmentation models into maintainable, deployment-ready components for on-premises clinical workflows in real-world health systems.

