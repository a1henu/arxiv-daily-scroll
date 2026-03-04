---
layout: default
title: Generalizable Knowledge Distillation from Vision Foundation Models for Semantic Segmentation
---

# Generalizable Knowledge Distillation from Vision Foundation Models for Semantic Segmentation
**arXiv**：[2603.02554v1](https://arxiv.org/abs/2603.02554) · [PDF](https://arxiv.org/pdf/2603.02554.pdf)  
**作者**：Chonghua Lv, Dong Zhao, Shuang Wang, Dou Quan, Ning Huyan, Nicu Sebe, Zhun Zhong  

**一句话要点**：提出通用知识蒸馏框架以增强视觉基础模型在语义分割中的跨域泛化能力

**关键词**：知识蒸馏, 语义分割, 视觉基础模型, 域泛化, 特征蒸馏, 跨域学习

## 3 点简述
- 核心问题：传统知识蒸馏在语义分割中忽视跨域泛化，尤其在视觉基础模型蒸馏时削弱其鲁棒性
- 方法要点：采用解耦表示学习与任务学习的多阶段框架，结合选择性特征蒸馏和查询式软蒸馏机制
- 实验或效果：在五个域泛化基准上优于现有方法，平均提升1.9%（F2F）和10.6%（F2L）

## 摘要（原文）

> Knowledge distillation (KD) has been widely applied in semantic segmentation to compress large models, but conventional approaches primarily preserve in-domain accuracy while neglecting out-of-domain generalization, which is essential under distribution shifts. This limitation becomes more severe with the emergence of vision foundation models (VFMs): although VFMs exhibit strong robustness on unseen data, distilling them with conventional KD often compromises this ability. We propose Generalizable Knowledge Distillation (GKD), a multi-stage framework that explicitly enhances generalization. GKD decouples representation learning from task learning. In the first stage, the student acquires domain-agnostic representations through selective feature distillation, and in the second stage, these representations are frozen for task adaptation, thereby mitigating overfitting to visible domains. To further support transfer, we introduce a query-based soft distillation mechanism, where student features act as queries to teacher representations to selectively retrieve transferable spatial knowledge from VFMs. Extensive experiments on five domain generalization benchmarks demonstrate that GKD consistently outperforms existing KD methods, achieving average gains of +1.9% in foundation-to-foundation (F2F) and +10.6% in foundation-to-local (F2L) distillation. The code will be available at https://github.com/Younger-hua/GKD.

