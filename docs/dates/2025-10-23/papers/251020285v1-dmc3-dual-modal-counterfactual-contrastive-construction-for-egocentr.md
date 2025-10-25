---
layout: default
title: DMC$^3$: Dual-Modal Counterfactual Contrastive Construction for Egocentric Video Question Answering
---

# DMC$^3$: Dual-Modal Counterfactual Contrastive Construction for Egocentric Video Question Answering
**arXiv**：[2510.20285v1](https://arxiv.org/abs/2510.20285) · [PDF](https://arxiv.org/pdf/2510.20285.pdf)  
**作者**：Jiayi Zou, Chaofan Chen, Bing-Kun Bao, Changsheng Xu  

**一句话要点**：提出双模态反事实对比构建框架以解决第一人称视频问答中的多事件和手物交互挑战

**关键词**：第一人称视频问答, 反事实样本构建, 对比学习, 多模态理解, 手物交互识别

## 3 点简述
- 核心问题：第一人称视频问答中忽略多事件理解和手物交互识别等独特挑战
- 方法要点：通过事件描述改写和核心交互挖掘构建反事实样本，并应用对比损失优化
- 实验或效果：在EgoTaskQA和QAEGO4D数据集上达到最先进性能，准确率分别为52.51%/46.04%和13.2%

## 摘要（原文）

> Egocentric Video Question Answering (Egocentric VideoQA) plays an important
> role in egocentric video understanding, which refers to answering questions
> based on first-person videos. Although existing methods have made progress
> through the paradigm of pre-training and fine-tuning, they ignore the unique
> challenges posed by the first-person perspective, such as understanding
> multiple events and recognizing hand-object interactions. To deal with these
> challenges, we propose a Dual-Modal Counterfactual Contrastive Construction
> (DMC$^3$) framework, which contains an egocentric videoqa baseline, a
> counterfactual sample construction module and a counterfactual sample-involved
> contrastive optimization. Specifically, We first develop a counterfactual
> sample construction module to generate positive and negative samples for
> textual and visual modalities through event description paraphrasing and core
> interaction mining, respectively. Then, We feed these samples together with the
> original samples into the baseline. Finally, in the counterfactual
> sample-involved contrastive optimization module, we apply contrastive loss to
> minimize the distance between the original sample features and the positive
> sample features, while maximizing the distance from the negative samples.
> Experiments show that our method achieve 52.51\% and 46.04\% on the
> \textit{normal} and \textit{indirect} splits of EgoTaskQA, and 13.2\% on
> QAEGO4D, both reaching the state-of-the-art performance.

