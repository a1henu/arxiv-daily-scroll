---
layout: default
title: LAB-Det: Language as a Domain-Invariant Bridge for Training-Free One-Shot Domain Generalization in Object Detection
---

# LAB-Det: Language as a Domain-Invariant Bridge for Training-Free One-Shot Domain Generalization in Object Detection
**arXiv**：[2602.06474v1](https://arxiv.org/abs/2602.06474) · [PDF](https://arxiv.org/pdf/2602.06474.pdf)  
**作者**：Xu Zhang, Zhe Chen, Jing Zhang, Dacheng Tao  

**一句话要点**：提出LAB-Det，利用语言作为领域不变桥梁，实现无需训练的单样本领域泛化目标检测。

**关键词**：目标检测, 领域泛化, 单样本学习, 语言引导, 训练免费适应, 数据稀缺场景

## 3 点简述
- 核心问题：基础目标检测器在数据稀缺的专门领域（如水下图像或工业缺陷）性能下降，传统微调方法成本高且易过拟合。
- 方法要点：通过将单样本示例投影为描述性文本，作为领域不变桥梁，引导冻结检测器进行语言条件化适应，无需权重更新。
- 实验或效果：在UODD和NEU-DET基准上，LAB-Det无需参数更新，相比微调基线提升高达5.4 mAP，验证了语言适应的高效性和可解释性。

## 摘要（原文）

> Foundation object detectors such as GLIP and Grounding DINO excel on general-domain data but often degrade in specialized and data-scarce settings like underwater imagery or industrial defects. Typical cross-domain few-shot approaches rely on fine-tuning scarce target data, incurring cost and overfitting risks. We instead ask: Can a frozen detector adapt with only one exemplar per class without training? To answer this, we introduce training-free one-shot domain generalization for object detection, where detectors must adapt to specialized domains with only one annotated exemplar per class and no weight updates. To tackle this task, we propose LAB-Det, which exploits Language As a domain-invariant Bridge. Instead of adapting visual features, we project each exemplar into a descriptive text that conditions and guides a frozen detector. This linguistic conditioning replaces gradient-based adaptation, enabling robust generalization in data-scarce domains. We evaluate on UODD (underwater) and NEU-DET (industrial defects), two widely adopted benchmarks for data-scarce detection, where object boundaries are often ambiguous, and LAB-Det achieves up to 5.4 mAP improvement over state-of-the-art fine-tuned baselines without updating a single parameter. These results establish linguistic adaptation as an efficient and interpretable alternative to fine-tuning in specialized detection settings.

