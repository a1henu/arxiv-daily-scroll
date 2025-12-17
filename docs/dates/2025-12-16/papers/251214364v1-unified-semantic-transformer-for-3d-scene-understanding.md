---
layout: default
title: Unified Semantic Transformer for 3D Scene Understanding
---

# Unified Semantic Transformer for 3D Scene Understanding
**arXiv**：[2512.14364v1](https://arxiv.org/abs/2512.14364) · [PDF](https://arxiv.org/pdf/2512.14364.pdf)  
**作者**：Sebastian Koch, Johanna Wald, Hide Matsuki, Pedro Hermosilla, Timo Ropinski, Federico Tombari  

**一句话要点**：提出UNITE统一语义Transformer，以单一模型解决多任务3D场景理解问题。

**关键词**：3D场景理解, 统一语义Transformer, 多任务学习, 2D蒸馏, 自监督训练, 多视角一致性

## 3 点简述
- 核心问题：现有3D场景理解模型多为任务特定，缺乏统一处理多语义任务的能力。
- 方法要点：基于前馈神经网络，通过2D蒸馏和自监督训练，结合多视角损失确保3D一致性。
- 实验或效果：在多个语义任务上达到先进性能，超越任务特定模型，甚至优于基于真实3D几何的方法。

## 摘要（原文）

> Holistic 3D scene understanding involves capturing and parsing unstructured 3D environments. Due to the inherent complexity of the real world, existing models have predominantly been developed and limited to be task-specific. We introduce UNITE, a Unified Semantic Transformer for 3D scene understanding, a novel feed-forward neural network that unifies a diverse set of 3D semantic tasks within a single model. Our model operates on unseen scenes in a fully end-to-end manner and only takes a few seconds to infer the full 3D semantic geometry. Our approach is capable of directly predicting multiple semantic attributes, including 3D scene segmentation, instance embeddings, open-vocabulary features, as well as affordance and articulations, solely from RGB images. The method is trained using a combination of 2D distillation, heavily relying on self-supervision and leverages novel multi-view losses designed to ensure 3D view consistency. We demonstrate that UNITE achieves state-of-the-art performance on several different semantic tasks and even outperforms task-specific models, in many cases, surpassing methods that operate on ground truth 3D geometry. See the project website at unite-page.github.io

