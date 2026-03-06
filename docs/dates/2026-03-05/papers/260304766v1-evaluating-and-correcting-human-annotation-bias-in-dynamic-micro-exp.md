---
layout: default
title: Evaluating and Correcting Human Annotation Bias in Dynamic Micro-Expression Recognition
---

# Evaluating and Correcting Human Annotation Bias in Dynamic Micro-Expression Recognition
**arXiv**：[2603.04766v1](https://arxiv.org/abs/2603.04766) · [PDF](https://arxiv.org/pdf/2603.04766.pdf)  
**作者**：Feng Liu, Bingyu Nan, Xuezhong Qian, Xiaolan Fu  

**一句话要点**：提出GAMDSS架构以解决跨文化微表情识别中人工标注偏差问题

**关键词**：微表情识别, 标注偏差校正, 时空建模, 关键帧选择, 跨文化数据集

## 3 点简述
- 核心问题：跨文化场景下微表情关键帧人工标注存在误差，影响识别准确性。
- 方法要点：通过动态帧重选机制识别Onset和Apex帧，构建丰富时空动态表示。
- 实验或效果：在七个数据集上验证，GAMDSS减少主观误差，提升识别性能，无需增加参数。

## 摘要（原文）

> Existing manual labeling of micro-expressions is subject to errors in accuracy, especially in cross-cultural scenarios where deviation in labeling of key frames is more prominent. To address this issue, this paper presents a novel Global Anti-Monotonic Differential Selection Strategy (GAMDSS) architecture for enhancing the effectiveness of spatio-temporal modeling of micro-expressions through keyframe re-selection. Specifically, the method identifies Onset and Apex frames, which are characterized by significant micro-expression variation, from complete micro-expression action sequences via a dynamic frame reselection mechanism. It then uses these to determine Offset frames and construct a rich spatio-temporal dynamic representation. A two-branch structure with shared parameters is then used to efficiently extract spatio-temporal features. Extensive experiments are conducted on seven widely recognized micro-expression datasets. The results demonstrate that GAMDSS effectively reduces subjective errors caused by human factors in multicultural datasets such as SAMM and 4DME. Furthermore, quantitative analyses confirm that offset-frame annotations in multicultural datasets are more uncertain, providing theoretical justification for standardizing micro-expression annotations. These findings directly support our argument for reconsidering the validity and generalizability of dataset annotation paradigms. Notably, this design can be integrated into existing models without increasing the number of parameters, offering a new approach to enhancing micro-expression recognition performance. The source code is available on GitHub[https://github.com/Cross-Innovation-Lab/GAMDSS].

