---
layout: default
title: TTP: Test-Time Padding for Adversarial Detection and Robust Adaptation on Vision-Language Models
---

# TTP: Test-Time Padding for Adversarial Detection and Robust Adaptation on Vision-Language Models
**arXiv**：[2512.16523v1](https://arxiv.org/abs/2512.16523) · [PDF](https://arxiv.org/pdf/2512.16523.pdf)  
**作者**：Zhiwei Li, Yitian Pang, Weining Wang, Zhenan Sun, Qi Li  

**一句话要点**：提出测试时填充方法，以增强视觉语言模型的对抗检测与鲁棒适应能力

**关键词**：视觉语言模型, 对抗检测, 测试时适应, 鲁棒性增强, CLIP模型, 空间填充

## 3 点简述
- 视觉语言模型如CLIP在零样本识别中表现优异，但对对抗扰动高度敏感，现有防御方法存在依赖标注数据或检测不可靠的问题。
- TTP通过空间填充前后特征嵌入的余弦相似度偏移进行对抗检测，并使用可训练填充恢复注意力模式，结合相似性感知集成策略提升鲁棒性。
- 实验表明，TTP在多种CLIP骨干和细粒度基准上超越现有测试时防御方法，显著提升对抗鲁棒性而不损害干净准确率。

## 摘要（原文）

> Vision-Language Models (VLMs), such as CLIP, have achieved impressive zero-shot recognition performance but remain highly susceptible to adversarial perturbations, posing significant risks in safety-critical scenarios. Previous training-time defenses rely on adversarial fine-tuning, which requires labeled data and costly retraining, while existing test-time strategies fail to reliably distinguish between clean and adversarial inputs, thereby preventing both adversarial robustness and clean accuracy from reaching their optimum. To address these limitations, we propose Test-Time Padding (TTP), a lightweight defense framework that performs adversarial detection followed by targeted adaptation at inference. TTP identifies adversarial inputs via the cosine similarity shift between CLIP feature embeddings computed before and after spatial padding, yielding a universal threshold for reliable detection across architectures and datasets. For detected adversarial cases, TTP employs trainable padding to restore disrupted attention patterns, coupled with a similarity-aware ensemble strategy for a more robust final prediction. For clean inputs, TTP leaves them unchanged by default or optionally integrates existing test-time adaptation techniques for further accuracy gains. Comprehensive experiments on diverse CLIP backbones and fine-grained benchmarks show that TTP consistently surpasses state-of-the-art test-time defenses, delivering substantial improvements in adversarial robustness without compromising clean accuracy. The code for this paper will be released soon.

