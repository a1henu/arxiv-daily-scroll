---
layout: default
title: Contract-Governed Training for Earth Observation: Observed Service Agreement Graphs and Coverage-Accuracy Trade-offs
---

# Contract-Governed Training for Earth Observation: Observed Service Agreement Graphs and Coverage-Accuracy Trade-offs
**arXiv**：[2512.04644v1](https://arxiv.org/abs/2512.04644) · [PDF](https://arxiv.org/pdf/2512.04644.pdf)  
**作者**：Wenzhang Du  

**一句话要点**：提出基于契约治理的地球观测训练框架，通过服务协议图平衡覆盖与精度

**关键词**：地球观测, 契约治理训练, 服务协议图, 采样策略, 覆盖-精度权衡, 遥感图像分类

## 3 点简述
- 地球观测模型训练缺乏对特定区域或类别的服务保障，导致隐式采样策略可能忽视关键需求
- 引入契约分组和OSAG治理层，通过采样权重调整实现契约级覆盖目标，并揭示精度-治理权衡
- 在AVIRIS和Sentinel-2数据集上实验，OSAG显著减少优先级覆盖误差，同时保持或提升全局精度

## 摘要（原文）

> Earth observation (EO) models are frequently trained under implicit sampling policies that optimize global accuracy but provide no explicit guarantees on who (which regions, classes, or mission-critical strata) is being served throughout training. This paper introduces a contract-governed training paradigm for EO in which training samples are grouped into service contracts -- semantically meaningful units such as (dataset, region, rare-crop indicator) -- and each contract is assigned a target service share. We instantiate this paradigm as an Observed Service Agreement Graph (OSAG), a lightweight governance layer that (i) monitors contract-level exposure (coverage) during optimization, (ii) drives empirical coverage toward target shares via contract-normalized sampling weights, and (iii) exposes explicit accuracy-governance trade-offs through two knobs: a sampling mixture coefficient alpha and a contract-regularization weight lambda_C. We provide a compact theory in a toy setting: OSAG sampling concentrates empirical coverage to targets; coverage deviations upper-bound service-risk deviations; and contract design (coarse vs. fine) modulates governance cost. Experiments on AVIRIS hyperspectral scenes (Indian Pines plus Salinas) and multispectral Sentinel-2 EuroSAT demonstrate that OSAG can substantially reduce priority coverage error while maintaining global accuracy and improving high-priority accuracy. A EuroSAT coarse-vs-fine contract ablation further evidences how semantically refined contracts can reduce the accuracy cost per unit of governance improvement.

