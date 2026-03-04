---
layout: default
title: CAPT: Confusion-Aware Prompt Tuning for Reducing Vision-Language Misalignment
---

# CAPT: Confusion-Aware Prompt Tuning for Reducing Vision-Language Misalignment
**arXiv**：[2603.02557v1](https://arxiv.org/abs/2603.02557) · [PDF](https://arxiv.org/pdf/2603.02557.pdf)  
**作者**：Maoyuan Shao, Yutong Gao, Xinyang Huang, Chuang Zhu, Lijuan Sun, Guoshun Nan  

**一句话要点**：提出混淆感知提示调优框架CAPT，以减少视觉语言模型中的系统性误分类。

**关键词**：视觉语言模型, 提示调优, 混淆感知学习, 细粒度分类, 跨模态对齐, 模型泛化

## 3 点简述
- 核心问题：视觉语言模型在视觉和语义相似类别间存在系统性混淆，反映内在偏见和细粒度判别能力不足。
- 方法要点：构建混淆库建模稳定混淆关系，通过语义和样本级挖掘器捕获全局和局部混淆信息，并设计多粒度差异专家模块统一推理。
- 实验或效果：在11个基准数据集上显著减少混淆错误，提升基类和新类的判别性与泛化能力，成功解决50.72%混淆样本对。

## 摘要（原文）

> Vision-language models like CLIP have achieved remarkable progress in cross-modal representation learning, yet suffer from systematic misclassifications among visually and semantically similar categories. We observe that such confusion patterns are not random but persistently occur between specific category pairs, revealing the model's intrinsic bias and limited fine-grained discriminative ability. To address this, we propose CAPT, a Confusion-Aware Prompt Tuning framework that enables models to learn from their own misalignment. Specifically, we construct a Confusion Bank to explicitly model stable confusion relationships across categories and misclassified samples. On this basis, we introduce a Semantic Confusion Miner (SEM) to capture global inter-class confusion through semantic difference and commonality prompts, and a Sample Confusion Miner (SAM) to retrieve representative misclassified instances from the bank and capture sample-level cues through a Diff-Manner Adapter that integrates global and local contexts. To further unify confusion information across different granularities, a Multi-Granularity Difference Expert (MGDE) module is designed to jointly leverage semantic- and sample-level experts for more robust confusion-aware reasoning. Extensive experiments on 11 benchmark datasets demonstrate that our method significantly reduces confusion-induced errors while enhancing the discriminability and generalization of both base and novel classes, successfully resolving 50.72 percent of confusable sample pairs. Code will be released at https://github.com/greatest-gourmet/CAPT.

