---
layout: default
title: Fine-Grained Traceability for Transparent ML Pipelines
---

# Fine-Grained Traceability for Transparent ML Pipelines
**arXiv**：[2601.14971v1](https://arxiv.org/abs/2601.14971) · [PDF](https://arxiv.org/pdf/2601.14971.pdf)  
**作者**：Liping Chen, Mujie Liu, Haytham Fayek  

**一句话要点**：提出FG-Trac框架以解决机器学习管道中样本级可追溯性缺失的问题

**关键词**：机器学习管道, 样本级可追溯性, 加密承诺, 透明度机制, 模型无关框架

## 3 点简述
- 核心问题：现有透明度机制缺乏可验证的样本级追溯，无法跟踪数据在管道中的使用情况
- 方法要点：定义样本生命周期事件捕获与验证机制，基于训练检查点计算贡献分数，并锚定到防篡改加密承诺
- 实验或效果：在CNN和多模态图学习管道上验证，保持预测性能，提供可审计的数据使用历史

## 摘要（原文）

> Modern machine learning systems are increasingly realised as multistage pipelines, yet existing transparency mechanisms typically operate at a model level: they describe what a system is and why it behaves as it does, but not how individual data samples are operationally recorded, tracked, and verified as they traverse the pipeline. This absence of verifiable, sample-level traceability leaves practitioners and users unable to determine whether a specific sample was used, when it was processed, or whether the corresponding records remain intact over time. We introduce FG-Trac, a model-agnostic framework that establishes verifiable, fine-grained sample-level traceability throughout machine learning pipelines. FG-Trac defines an explicit mechanism for capturing and verifying sample lifecycle events across preprocessing and training, computes contribution scores explicitly grounded in training checkpoints, and anchors these traces to tamper-evident cryptographic commitments. The framework integrates without modifying model architectures or training objectives, reconstructing complete and auditable data-usage histories with practical computational overhead. Experiments on a canonical convolutional neural network and a multimodal graph learning pipeline demonstrate that FG-Trac preserves predictive performance while enabling machine learning systems to furnish verifiable evidence of how individual samples were used and propagated during model execution.

