---
layout: default
title: CountZES: Counting via Zero-Shot Exemplar Selection
---

# CountZES: Counting via Zero-Shot Exemplar Selection
**arXiv**：[2512.16415v1](https://arxiv.org/abs/2512.16415) · [PDF](https://arxiv.org/pdf/2512.16415.pdf)  
**作者**：Muhammad Ibraheem Siddiqui, Muhammad Haris Khan  

**一句话要点**：提出CountZES框架，通过零样本示例选择解决复杂场景中未见类别对象计数问题。

**关键词**：零样本对象计数, 示例选择, 开放词汇检测, 密度引导, 特征聚类, 跨域泛化

## 3 点简述
- 核心问题：零样本对象计数中，现有方法依赖开放词汇检测器或随机采样，难以准确识别单实例示例。
- 方法要点：采用三阶段协同框架，包括检测锚定、密度引导和特征共识，逐步发现多样互补示例。
- 实验或效果：在多个数据集上优于现有零样本计数方法，并有效泛化至自然、航拍和医学领域。

## 摘要（原文）

> Object counting in complex scenes remains challenging, particularly in the zero-shot setting, where the goal is to count instances of unseen categories specified only by a class name. Existing zero-shot object counting (ZOC) methods that infer exemplars from text either rely on open-vocabulary detectors, which often yield multi-instance candidates, or on random patch sampling, which fails to accurately delineate object instances. To address this, we propose CountZES, a training-free framework for object counting via zero-shot exemplar selection. CountZES progressively discovers diverse exemplars through three synergistic stages: Detection-Anchored Exemplar (DAE), Density-Guided Exemplar (DGE), and Feature-Consensus Exemplar (FCE). DAE refines open-vocabulary detections to isolate precise single-instance exemplars. DGE introduces a density-driven, self-supervised paradigm to identify statistically consistent and semantically compact exemplars, while FCE reinforces visual coherence through feature-space clustering. Together, these stages yield a diverse, complementary exemplar set that balances textual grounding, count consistency, and feature representativeness. Experiments on diverse datasets demonstrate CountZES superior performance among ZOC methods while generalizing effectively across natural, aerial and medical domains.

