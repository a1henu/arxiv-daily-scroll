---
layout: default
title: Task Prototype-Based Knowledge Retrieval for Multi-Task Learning from Partially Annotated Data
---

# Task Prototype-Based Knowledge Retrieval for Multi-Task Learning from Partially Annotated Data
**arXiv**：[2601.07474v1](https://arxiv.org/abs/2601.07474) · [PDF](https://arxiv.org/pdf/2601.07474.pdf)  
**作者**：Youngmin Oh, Hyung-Il Kim, Jung Uk Kim  

**一句话要点**：提出基于任务原型的知识检索框架，以解决部分标注数据下的多任务学习问题

**关键词**：多任务学习, 部分标注数据, 任务原型, 知识检索, 负迁移, Transformer

## 3 点简述
- 核心问题：部分标注多任务学习中，依赖未标注任务预测易导致负迁移和性能不佳
- 方法要点：使用任务原型嵌入任务特性并量化关联，结合知识检索Transformer自适应优化特征
- 实验或效果：广泛实验验证框架有效性，提升在部分标注场景下的鲁棒性

## 摘要（原文）

> Multi-task learning (MTL) is critical in real-world applications such as autonomous driving and robotics, enabling simultaneous handling of diverse tasks. However, obtaining fully annotated data for all tasks is impractical due to labeling costs. Existing methods for partially labeled MTL typically rely on predictions from unlabeled tasks, making it difficult to establish reliable task associations and potentially leading to negative transfer and suboptimal performance. To address these issues, we propose a prototype-based knowledge retrieval framework that achieves robust MTL instead of relying on predictions from unlabeled tasks. Our framework consists of two key components: (1) a task prototype embedding task-specific characteristics and quantifying task associations, and (2) a knowledge retrieval transformer that adaptively refines feature representations based on these associations. To achieve this, we introduce an association knowledge generating (AKG) loss to ensure the task prototype consistently captures task-specific characteristics. Extensive experiments demonstrate the effectiveness of our framework, highlighting its potential for robust multi-task learning, even when only a subset of tasks is annotated.

