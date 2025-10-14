---
layout: default
title: Exploring and Leveraging Class Vectors for Classifier Editing
---

# Exploring and Leveraging Class Vectors for Classifier Editing
**arXiv**：[2510.11268v1](https://arxiv.org/abs/2510.11268) · [PDF](https://arxiv.org/pdf/2510.11268.pdf)  
**作者**：Jaeik Kim, Jaeyoung Do  

**一句话要点**：提出类向量以支持图像分类器的灵活编辑，应用于医学影像和制造异常检测。

**关键词**：图像分类器编辑, 类向量, 潜在空间调整, 遗忘学习, 对抗防御, 分布适应

## 3 点简述
- 核心问题：图像分类器训练后难以编辑，如遗忘特定类或适应分布变化，现有方法成本高或范围窄。
- 方法要点：类向量在潜在空间捕获类特定表示调整，支持特征引导或权重更新实现编辑。
- 实验或效果：验证在遗忘、环境适应、对抗防御和触发优化等应用中的有效性。

## 摘要（原文）

> Image classifiers play a critical role in detecting diseases in medical
> imaging and identifying anomalies in manufacturing processes. However, their
> predefined behaviors after extensive training make post hoc model editing
> difficult, especially when it comes to forgetting specific classes or adapting
> to distribution shifts. Existing classifier editing methods either focus
> narrowly on correcting errors or incur extensive retraining costs, creating a
> bottleneck for flexible editing. Moreover, such editing has seen limited
> investigation in image classification. To overcome these challenges, we
> introduce Class Vectors, which capture class-specific representation
> adjustments during fine-tuning. Whereas task vectors encode task-level changes
> in weight space, Class Vectors disentangle each class's adaptation in the
> latent space. We show that Class Vectors capture each class's semantic shift
> and that classifier editing can be achieved either by steering latent features
> along these vectors or by mapping them into weight space to update the decision
> boundaries. We also demonstrate that the inherent linearity and orthogonality
> of Class Vectors support efficient, flexible, and high-level concept editing
> via simple class arithmetic. Finally, we validate their utility in applications
> such as unlearning, environmental adaptation, adversarial defense, and
> adversarial trigger optimization.

