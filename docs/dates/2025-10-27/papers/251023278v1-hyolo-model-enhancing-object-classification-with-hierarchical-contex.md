---
layout: default
title: hYOLO Model: Enhancing Object Classification with Hierarchical Context in YOLOv8
---

# hYOLO Model: Enhancing Object Classification with Hierarchical Context in YOLOv8
**arXiv**：[2510.23278v1](https://arxiv.org/abs/2510.23278) · [PDF](https://arxiv.org/pdf/2510.23278.pdf)  
**作者**：Veska Tsenkova, Peter Stanchev, Daniel Petrov, Deyan Lazarov  

**一句话要点**：提出hYOLO模型，在YOLOv8中引入层次结构以增强物体分类

**关键词**：层次分类, YOLO模型, 损失函数优化, 物体检测, 上下文建模

## 3 点简述
- 核心问题：传统CNN分类忽略物体层次关系，影响分类准确性。
- 方法要点：设计层次架构、修改损失函数和性能指标，实现端到端检测。
- 实验或效果：在两种层次分类数据集上验证，提升上下文理解和错误控制。

## 摘要（原文）

> Current convolution neural network (CNN) classification methods are
> predominantly focused on flat classification which aims solely to identify a
> specified object within an image. However, real-world objects often possess a
> natural hierarchical organization that can significantly help classification
> tasks. Capturing the presence of relations between objects enables better
> contextual understanding as well as control over the severity of mistakes.
> Considering these aspects, this paper proposes an end-to-end hierarchical model
> for image detection and classification built upon the YOLO model family. A
> novel hierarchical architecture, a modified loss function, and a performance
> metric tailored to the hierarchical nature of the model are introduced. The
> proposed model is trained and evaluated on two different hierarchical
> categorizations of the same dataset: a systematic categorization that
> disregards visual similarities between objects and a categorization accounting
> for common visual characteristics across classes. The results illustrate how
> the suggested methodology addresses the inherent hierarchical structure present
> in real-world objects, which conventional flat classification algorithms often
> overlook.

