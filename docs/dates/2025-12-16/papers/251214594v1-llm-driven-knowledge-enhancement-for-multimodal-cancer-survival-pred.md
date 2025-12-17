---
layout: default
title: LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction
---

# LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction
**arXiv**：[2512.14594v1](https://arxiv.org/abs/2512.14594) · [PDF](https://arxiv.org/pdf/2512.14594.pdf)  
**作者**：Chenyu Zhao, Yingxue Xu, Fengtao Zhou, Yihui Wang, Hao Chen  

**一句话要点**：提出KEMM模型，利用LLM增强知识以解决多模态癌症生存预测中的特征冗余与对齐难题。

**关键词**：多模态生存预测, 知识增强, 跨模态注意力, 癌症预后, LLM驱动

## 3 点简述
- 核心问题：多模态生存预测依赖高维冗余的病理图像和基因组数据，特征提取与对齐困难，且生存标签监督不足。
- 方法要点：集成LLM精炼的专家报告和预后背景知识，通过知识增强跨模态注意力模块聚焦判别性特征。
- 实验或效果：在五个数据集上验证，KEMM达到最先进性能，代码将在接受后发布。

## 摘要（原文）

> Current multimodal survival prediction methods typically rely on pathology images (WSIs) and genomic data, both of which are high-dimensional and redundant, making it difficult to extract discriminative features from them and align different modalities. Moreover, using a simple survival follow-up label is insufficient to supervise such a complex task. To address these challenges, we propose KEMM, an LLM-driven Knowledge-Enhanced Multimodal Model for cancer survival prediction, which integrates expert reports and prognostic background knowledge. 1) Expert reports, provided by pathologists on a case-by-case basis and refined by large language model (LLM), offer succinct and clinically focused diagnostic statements. This information may typically suggest different survival outcomes. 2) Prognostic background knowledge (PBK), generated concisely by LLM, provides valuable prognostic background knowledge on different cancer types, which also enhances survival prediction. To leverage these knowledge, we introduce the knowledge-enhanced cross-modal (KECM) attention module. KECM can effectively guide the network to focus on discriminative and survival-relevant features from highly redundant modalities. Extensive experiments on five datasets demonstrate that KEMM achieves state-of-the-art performance. The code will be released upon acceptance.

