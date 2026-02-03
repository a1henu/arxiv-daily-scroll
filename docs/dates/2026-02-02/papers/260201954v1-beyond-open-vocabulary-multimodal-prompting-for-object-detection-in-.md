---
layout: default
title: Beyond Open Vocabulary: Multimodal Prompting for Object Detection in Remote Sensing Images
---

# Beyond Open Vocabulary: Multimodal Prompting for Object Detection in Remote Sensing Images
**arXiv**：[2602.01954v1](https://arxiv.org/abs/2602.01954) · [PDF](https://arxiv.org/pdf/2602.01954.pdf)  
**作者**：Shuai Yang, Ziyue Huang, Jiaxin Chen, Qingjie Liu, Yunhong Wang  

**一句话要点**：提出RS-MPOD框架，通过多模态提示解决遥感图像开放词汇检测中的语义不稳定问题。

**关键词**：遥感图像检测, 开放词汇检测, 多模态提示, 视觉提示, 语义对齐, 实例外观编码

## 3 点简述
- 核心问题：遥感开放词汇检测中，仅依赖文本提示常因语义模糊和分布偏移导致类别指定不稳定。
- 方法要点：引入视觉提示编码器提取实例外观线索，支持无文本类别指定，并结合多模态融合模块整合视觉与文本信息。
- 实验或效果：在标准、跨数据集和细粒度基准上验证，视觉提示在语义模糊下更可靠，多模态提示在文本语义对齐时保持竞争力。

## 摘要（原文）

> Open-vocabulary object detection in remote sensing commonly relies on text-only prompting to specify target categories, implicitly assuming that inference-time category queries can be reliably grounded through pretraining-induced text-visual alignment. In practice, this assumption often breaks down in remote sensing scenarios due to task- and application-specific category semantics, resulting in unstable category specification under open-vocabulary settings. To address this limitation, we propose RS-MPOD, a multimodal open-vocabulary detection framework that reformulates category specification beyond text-only prompting by incorporating instance-grounded visual prompts, textual prompts, and their multimodal integration. RS-MPOD introduces a visual prompt encoder to extract appearance-based category cues from exemplar instances, enabling text-free category specification, and a multimodal fusion module to integrate visual and textual information when both modalities are available. Extensive experiments on standard, cross-dataset, and fine-grained remote sensing benchmarks show that visual prompting yields more reliable category specification under semantic ambiguity and distribution shifts, while multimodal prompting provides a flexible alternative that remains competitive when textual semantics are well aligned.

