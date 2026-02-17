---
layout: default
title: Concepts' Information Bottleneck Models
---

# Concepts' Information Bottleneck Models
**arXiv**：[2602.14626v1](https://arxiv.org/abs/2602.14626) · [PDF](https://arxiv.org/pdf/2602.14626.pdf)  
**作者**：Karim Galliamov, Syed M Ahsan Kazmi, Adil Khan, Adín Ramírez Rivera  

**一句话要点**：提出概念信息瓶颈正则化器以提升概念瓶颈模型的准确性和忠实性

**关键词**：概念瓶颈模型, 信息瓶颈, 正则化, 可解释人工智能, 概念泄露, 最小充分表示

## 3 点简述
- 核心问题：概念瓶颈模型存在准确性下降和概念泄露问题，影响预测忠实性。
- 方法要点：在概念层引入信息瓶颈正则化，最小化输入与概念互信息，保留任务相关信息。
- 实验或效果：在六个模型家族和三个基准测试中，正则化模型一致优于原始模型，改善预测性能和干预可靠性。

## 摘要（原文）

> Concept Bottleneck Models (CBMs) aim to deliver interpretable predictions by routing decisions through a human-understandable concept layer, yet they often suffer reduced accuracy and concept leakage that undermines faithfulness. We introduce an explicit Information Bottleneck regularizer on the concept layer that penalizes $I(X;C)$ while preserving task-relevant information in $I(C;Y)$, encouraging minimal-sufficient concept representations. We derive two practical variants (a variational objective and an entropy-based surrogate) and integrate them into standard CBM training without architectural changes or additional supervision. Evaluated across six CBM families and three benchmarks, the IB-regularized models consistently outperform their vanilla counterparts. Information-plane analyses further corroborate the intended behavior. These results indicate that enforcing a minimal-sufficient concept bottleneck improves both predictive performance and the reliability of concept-level interventions. The proposed regularizer offers a theoretic-grounded, architecture-agnostic path to more faithful and intervenable CBMs, resolving prior evaluation inconsistencies by aligning training protocols and demonstrating robust gains across model families and datasets.

