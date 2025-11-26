---
layout: default
title: TaCo: Capturing Spatio-Temporal Semantic Consistency in Remote Sensing Change Detection
---

# TaCo: Capturing Spatio-Temporal Semantic Consistency in Remote Sensing Change Detection
**arXiv**：[2511.20306v1](https://arxiv.org/abs/2511.20306) · [PDF](https://arxiv.org/pdf/2511.20306.pdf)  
**作者**：Han Guo, Chenyang Liu, Haotian Zhang, Bowen Chen, Zhengxia Zou, Zhenwei Shi  

**一句话要点**：提出TaCo网络以解决遥感变化检测中的时空语义不一致问题

**关键词**：遥感变化检测, 时空语义一致性, 文本引导生成, 联合约束, SOTA性能

## 3 点简述
- 核心问题：传统方法依赖掩码监督，导致时空语义一致性不足
- 方法要点：引入文本引导的过渡生成器和时空语义联合约束
- 实验或效果：在六个公开数据集上实现SOTA性能，推理无额外开销

## 摘要（原文）

> Remote sensing change detection (RSCD) aims to identify surface changes across bi-temporal satellite images. Most previous methods rely solely on mask supervision, which effectively guides spatial localization but provides limited constraints on the temporal semantic transitions. Consequently, they often produce spatially coherent predictions while still suffering from unresolved semantic inconsistencies. To address this limitation, we propose TaCo, a spatio-temporal semantic consistent network, which enriches the existing mask-supervised framework with a spatio-temporal semantic joint constraint. TaCo conceptualizes change as a semantic transition between bi-temporal states, in which one temporal feature representation can be derived from the other via dedicated transition features. To realize this, we introduce a Text-guided Transition Generator that integrates textual semantics with bi-temporal visual features to construct the cross-temporal transition features. In addition, we propose a spatio-temporal semantic joint constraint consisting of bi-temporal reconstruct constraints and a transition constraint: the former enforces alignment between reconstructed and original features, while the latter enhances discrimination for changes. This design can yield substantial performance gains without introducing any additional computational overhead during inference. Extensive experiments on six public datasets, spanning both binary and semantic change detection tasks, demonstrate that TaCo consistently achieves SOTA performance.

