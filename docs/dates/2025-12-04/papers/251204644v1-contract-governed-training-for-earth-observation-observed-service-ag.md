---
layout: default
title: Contract-Governed Training for Earth Observation: Observed Service Agreement Graphs and Coverage-Accuracy Trade-offs
---

# Contract-Governed Training for Earth Observation: Observed Service Agreement Graphs and Coverage-Accuracy Trade-offs
**arXiv**：[2512.04644v1](https://arxiv.org/abs/2512.04644) · [PDF](https://arxiv.org/pdf/2512.04644.pdf)  
**作者**：Wenzhang Du  

**一句话要点**：提出合同治理训练范式，通过观测服务协议图优化地球观测模型的服务覆盖与准确性权衡。

**关键词**：地球观测模型, 合同治理训练, 服务覆盖优化, 准确性权衡, 采样策略, 语义合同设计

## 3 点简述
- 核心问题：地球观测模型训练缺乏对特定区域或类别的服务覆盖保证，导致全局准确性优先但服务不均。
- 方法要点：引入服务合同分组样本，使用观测服务协议图监控和调整合同级覆盖，通过采样权重和正则化参数实现治理。
- 实验或效果：在AVIRIS和Sentinel-2数据集上验证，能显著减少优先覆盖误差，保持全局准确性并提升高优先级准确性。

## 摘要（原文）

> Earth observation (EO) models are frequently trained under implicit sampling policies that optimize global accuracy but provide no explicit guarantees on who (which regions, classes, or mission-critical strata) is being served throughout training. This paper introduces a contract-governed training paradigm for EO in which training samples are grouped into service contracts -- semantically meaningful units such as (dataset, region, rare-crop indicator) -- and each contract is assigned a target service share. We instantiate this paradigm as an Observed Service Agreement Graph (OSAG), a lightweight governance layer that (i) monitors contract-level exposure (coverage) during optimization, (ii) drives empirical coverage toward target shares via contract-normalized sampling weights, and (iii) exposes explicit accuracy-governance trade-offs through two knobs: a sampling mixture coefficient alpha and a contract-regularization weight lambda_C. We provide a compact theory in a toy setting: OSAG sampling concentrates empirical coverage to targets; coverage deviations upper-bound service-risk deviations; and contract design (coarse vs. fine) modulates governance cost. Experiments on AVIRIS hyperspectral scenes (Indian Pines plus Salinas) and multispectral Sentinel-2 EuroSAT demonstrate that OSAG can substantially reduce priority coverage error while maintaining global accuracy and improving high-priority accuracy. A EuroSAT coarse-vs-fine contract ablation further evidences how semantically refined contracts can reduce the accuracy cost per unit of governance improvement.

