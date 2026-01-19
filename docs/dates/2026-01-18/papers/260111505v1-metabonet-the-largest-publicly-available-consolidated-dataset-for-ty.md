---
layout: default
title: MetaboNet: The Largest Publicly Available Consolidated Dataset for Type 1 Diabetes Management
---

# MetaboNet: The Largest Publicly Available Consolidated Dataset for Type 1 Diabetes Management
**arXiv**：[2601.11505v1](https://arxiv.org/abs/2601.11505) · [PDF](https://arxiv.org/pdf/2601.11505.pdf)  
**作者**：Miriam K. Wolff, Peter Calhoun, Eleonora Maria Aiello, Yao Qin, Sam F. Royston  

**一句话要点**：提出MetaboNet数据集以解决1型糖尿病算法开发中数据碎片化和标准化不足的问题

**关键词**：1型糖尿病管理, 数据集整合, 连续血糖监测, 胰岛素泵数据, 算法开发, 数据标准化

## 3 点简述
- 核心问题：现有1型糖尿病管理数据集碎片化且缺乏标准化，阻碍算法开发和泛化。
- 方法要点：整合多个公开数据集，要求包含连续血糖监测和胰岛素泵数据，形成统一资源。
- 实验或效果：数据集包含3135名受试者，提供公开和受限访问子集，支持更泛化的算法性能。

## 摘要（原文）

> Progress in Type 1 Diabetes (T1D) algorithm development is limited by the fragmentation and lack of standardization across existing T1D management datasets. Current datasets differ substantially in structure and are time-consuming to access and process, which impedes data integration and reduces the comparability and generalizability of algorithmic developments. This work aims to establish a unified and accessible data resource for T1D algorithm development. Multiple publicly available T1D datasets were consolidated into a unified resource, termed the MetaboNet dataset. Inclusion required the availability of both continuous glucose monitoring (CGM) data and corresponding insulin pump dosing records. Additionally, auxiliary information such as reported carbohydrate intake and physical activity was retained when present. The MetaboNet dataset comprises 3135 subjects and 1228 patient-years of overlapping CGM and insulin data, making it substantially larger than existing standalone benchmark datasets. The resource is distributed as a fully public subset available for immediate download at https://metabo-net.org/ , and with a Data Use Agreement (DUA)-restricted subset accessible through their respective application processes. For the datasets in the latter subset, processing pipelines are provided to automatically convert the data into the standardized MetaboNet format. A consolidated public dataset for T1D research is presented, and the access pathways for both its unrestricted and DUA-governed components are described. The resulting dataset covers a broad range of glycemic profiles and demographics and thus can yield more generalizable algorithmic performance than individual datasets.

