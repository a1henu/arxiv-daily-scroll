---
layout: default
title: Taxon: Hierarchical Tax Code Prediction with Semantically Aligned LLM Expert Guidance
---

# Taxon: Hierarchical Tax Code Prediction with Semantically Aligned LLM Expert Guidance
**arXiv**：[2601.08418v1](https://arxiv.org/abs/2601.08418) · [PDF](https://arxiv.org/pdf/2601.08418.pdf)  
**作者**：Jihang Li, Qing Liu, Zulong Chen, Jing Wang, Wei Wang, Chuanfei Xu, Zeyi Wen  

**一句话要点**：提出Taxon框架，通过语义对齐和专家指导解决电商平台税务编码预测问题。

**关键词**：税务编码预测, 层次分类, 语义对齐, 专家混合架构, 大语言模型蒸馏, 多源训练

## 3 点简述
- 核心问题：税务编码预测需在多级分类体系中准确映射产品，错误会导致财务和监管风险。
- 方法要点：结合特征门控专家混合架构和基于大语言模型的语义一致性模型，提升预测准确性。
- 实验或效果：在TaxCode数据集和公开基准上达到最优性能，已部署于阿里巴巴税务系统，日均处理超50万查询。

## 摘要（原文）

> Tax code prediction is a crucial yet underexplored task in automating invoicing and compliance management for large-scale e-commerce platforms. Each product must be accurately mapped to a node within a multi-level taxonomic hierarchy defined by national standards, where errors lead to financial inconsistencies and regulatory risks. This paper presents Taxon, a semantically aligned and expert-guided framework for hierarchical tax code prediction. Taxon integrates (i) a feature-gating mixture-of-experts architecture that adaptively routes multi-modal features across taxonomy levels, and (ii) a semantic consistency model distilled from large language models acting as domain experts to verify alignment between product titles and official tax definitions. To address noisy supervision in real business records, we design a multi-source training pipeline that combines curated tax databases, invoice validation logs, and merchant registration data to provide both structural and semantic supervision. Extensive experiments on the proprietary TaxCode dataset and public benchmarks demonstrate that Taxon achieves state-of-the-art performance, outperforming strong baselines. Further, an additional full hierarchical paths reconstruction procedure significantly improves structural consistency, yielding the highest overall F1 scores. Taxon has been deployed in production within Alibaba's tax service system, handling an average of over 500,000 tax code queries per day and reaching peak volumes above five million requests during business event with improved accuracy, interpretability, and robustness.

