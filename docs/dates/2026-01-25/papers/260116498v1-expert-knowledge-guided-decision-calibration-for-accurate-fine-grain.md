---
layout: default
title: Expert Knowledge-Guided Decision Calibration for Accurate Fine-Grained Tree Species Classification
---

# Expert Knowledge-Guided Decision Calibration for Accurate Fine-Grained Tree Species Classification
**arXiv**：[2601.16498v1](https://arxiv.org/abs/2601.16498) · [PDF](https://arxiv.org/pdf/2601.16498.pdf)  
**作者**：Chen Long, Dian Chen, Ruifei Ding, Zhe Chen, Zhen Dong, Bisheng Yang  

**一句话要点**：提出专家知识引导的决策校准网络，以解决细粒度树种分类中的长尾分布和类间相似性问题。

**关键词**：细粒度分类, 决策校准, 专家知识, 长尾分布, 类间相似性, 轻量级模块

## 3 点简述
- 核心问题：现有方法在有限数据下难以处理长尾分布和高类间相似性，导致少样本或易混淆类别分类困难。
- 方法要点：引入外部领域专家，通过局部先验引导知识提取模块和不确定性引导决策校准模块，动态修正模型决策。
- 实验或效果：在三个基准数据集上实现最先进性能，作为轻量级即插即用模块，仅增加0.08M参数即可提升主干网络准确率6.42%和精确率11.46%。

## 摘要（原文）

> Accurate fine-grained tree species classification is critical for forest inventory and biodiversity monitoring. Existing methods predominantly focus on designing complex architectures to fit local data distributions. However, they often overlook the long-tailed distributions and high inter-class similarity inherent in limited data, thereby struggling to distinguish between few-shot or confusing categories. In the process of knowledge dissemination in the human world, individuals will actively seek expert assistance to transcend the limitations of local thinking. Inspired by this, we introduce an external "Domain Expert" and propose an Expert Knowledge-Guided Classification Decision Calibration Network (EKDC-Net) to overcome these challenges. Our framework addresses two core issues: expert knowledge extraction and utilization. Specifically, we first develop a Local Prior Guided Knowledge Extraction Module (LPKEM). By leveraging Class Activation Map (CAM) analysis, LPKEM guides the domain expert to focus exclusively on discriminative features essential for classification. Subsequently, to effectively integrate this knowledge, we design an Uncertainty-Guided Decision Calibration Module (UDCM). This module dynamically corrects the local model's decisions by considering both overall category uncertainty and instance-level prediction uncertainty. Furthermore, we present a large-scale classification dataset covering 102 tree species, named CU-Tree102 to address the issue of scarce diversity in current benchmarks. Experiments on three benchmark datasets demonstrate that our approach achieves state-of-the-art performance. Crucially, as a lightweight plug-and-play module, EKDC-Net improves backbone accuracy by 6.42% and precision by 11.46% using only 0.08M additional learnable parameters. The dataset, code, and pre-trained models are available at https://github.com/WHU-USI3DV/TreeCLS.

