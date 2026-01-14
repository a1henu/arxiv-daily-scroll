---
layout: default
title: Cross-modal Proxy Evolving for OOD Detection with Vision-Language Models
---

# Cross-modal Proxy Evolving for OOD Detection with Vision-Language Models
**arXiv**：[2601.08476v1](https://arxiv.org/abs/2601.08476) · [PDF](https://arxiv.org/pdf/2601.08476.pdf)  
**作者**：Hao Tang, Yu Liu, Shuanglin Yan, Fei Shen, Shengfeng He, Jing Qin  

**一句话要点**：提出CoEvo框架，通过双向代理协同演化解决零样本OOD检测中的跨模态失准问题。

**关键词**：零样本OOD检测, 跨模态对齐, 代理演化, 视觉语言模型, 测试时适应

## 3 点简述
- 核心问题：零样本OOD检测中，固定文本代理导致语义空间采样稀疏和跨模态失准，影响预测稳定性。
- 方法要点：CoEvo采用无训练和标注的测试时框架，通过代理对齐协同演化机制，动态更新文本和视觉代理以增强跨模态对齐。
- 实验或效果：在标准基准测试中，CoEvo实现SOTA性能，相比基线在ImageNet-1K上AUROC提升1.33%，FPR95降低45.98%。

## 摘要（原文）

> Reliable zero-shot detection of out-of-distribution (OOD) inputs is critical for deploying vision-language models in open-world settings. However, the lack of labeled negatives in zero-shot OOD detection necessitates proxy signals that remain effective under distribution shift. Existing negative-label methods rely on a fixed set of textual proxies, which (i) sparsely sample the semantic space beyond in-distribution (ID) classes and (ii) remain static while only visual features drift, leading to cross-modal misalignment and unstable predictions. In this paper, we propose CoEvo, a training- and annotation-free test-time framework that performs bidirectional, sample-conditioned adaptation of both textual and visual proxies. Specifically, CoEvo introduces a proxy-aligned co-evolution mechanism to maintain two evolving proxy caches, which dynamically mines contextual textual negatives guided by test images and iteratively refines visual proxies, progressively realigning cross-modal similarities and enlarging local OOD margins. Finally, we dynamically re-weight the contributions of dual-modal proxies to obtain a calibrated OOD score that is robust to distribution shift. Extensive experiments on standard benchmarks demonstrate that CoEvo achieves state-of-the-art performance, improving AUROC by 1.33% and reducing FPR95 by 45.98% on ImageNet-1K compared to strong negative-label baselines.

