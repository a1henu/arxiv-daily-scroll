---
layout: default
title: FedKDX: Federated Learning with Negative Knowledge Distillation for Enhanced Healthcare AI Systems
---

# FedKDX: Federated Learning with Negative Knowledge Distillation for Enhanced Healthcare AI Systems
**arXiv**：[2601.04587v1](https://arxiv.org/abs/2601.04587) · [PDF](https://arxiv.org/pdf/2601.04587.pdf)  
**作者**：Quang-Tu Pham, Hoang-Dieu Vu, Dinh-Dat Pham, Hieu H. Pham  

**一句话要点**：提出FedKDX框架，通过负知识蒸馏增强医疗AI联邦学习的泛化能力。

**关键词**：联邦学习, 负知识蒸馏, 医疗AI, 隐私保护, 非独立同分布数据

## 3 点简述
- 核心问题：医疗AI联邦学习中数据非独立同分布和隐私限制导致模型泛化不足。
- 方法要点：结合负知识蒸馏、传统知识蒸馏和对比学习，在统一架构中捕获目标与非目标信息。
- 实验或效果：在医疗数据集上提升准确率最高2.53%，加速收敛，并改善非独立同分布数据性能。

## 摘要（原文）

> This paper introduces FedKDX, a federated learning framework that addresses limitations in healthcare AI through Negative Knowledge Distillation (NKD). Unlike existing approaches that focus solely on positive knowledge transfer, FedKDX captures both target and non-target information to improve model generalization in healthcare applications. The framework integrates multiple knowledge transfer techniques--including traditional knowledge distillation, contrastive learning, and NKD--within a unified architecture that maintains privacy while reducing communication costs. Through experiments on healthcare datasets (SLEEP, UCI-HAR, and PAMAP2), FedKDX demonstrates improved accuracy (up to 2.53% over state-of-the-art methods), faster convergence, and better performance on non-IID data distributions. Theoretical analysis supports NKD's contribution to addressing statistical heterogeneity in distributed healthcare data. The approach shows promise for privacy-sensitive medical applications under regulatory frameworks like HIPAA and GDPR, offering a balanced solution between performance and practical implementation requirements in decentralized healthcare settings. The code and model are available at https://github.com/phamdinhdat-ai/Fed_2024.

