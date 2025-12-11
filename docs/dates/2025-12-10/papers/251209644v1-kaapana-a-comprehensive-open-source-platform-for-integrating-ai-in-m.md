---
layout: default
title: Kaapana: A Comprehensive Open-Source Platform for Integrating AI in Medical Imaging Research Environments
---

# Kaapana: A Comprehensive Open-Source Platform for Integrating AI in Medical Imaging Research Environments
**arXiv**：[2512.09644v1](https://arxiv.org/abs/2512.09644) · [PDF](https://arxiv.org/pdf/2512.09644.pdf)  
**作者**：Ünal Akünal, Markus Bujotzek, Stefan Denner, Benjamin Hamm, Klaus Kades, Philipp Schader, Jonas Scherer, Marco Nolden, Peter Neher, Ralf Floca, Klaus Maier-Hein  

**一句话要点**：提出Kaapana开源平台以解决医学影像AI研究中数据访问与工具标准化难题

**关键词**：医学影像AI, 开源平台, 工作流编排, 多中心研究, 数据管理, 可复现性

## 3 点简述
- 核心问题：医学影像AI研究受限于数据访问困难、软件碎片化及多中心协作挑战，导致工具链难以复现和扩展。
- 方法要点：提供模块化框架，统一数据管理、工作流编排和结果检查，支持算法到数据的分布式实验。
- 实验或效果：平台减少技术开销，提升可复现性，支持从本地原型到全国范围的大规模协作研究。

## 摘要（原文）

> Developing generalizable AI for medical imaging requires both access to large, multi-center datasets and standardized, reproducible tooling within research environments. However, leveraging real-world imaging data in clinical research environments is still hampered by strict regulatory constraints, fragmented software infrastructure, and the challenges inherent in conducting large-cohort multicentre studies. This leads to projects that rely on ad-hoc toolchains that are hard to reproduce, difficult to scale beyond single institutions and poorly suited for collaboration between clinicians and data scientists. We present Kaapana, a comprehensive open-source platform for medical imaging research that is designed to bridge this gap. Rather than building single-use, site-specific tooling, Kaapana provides a modular, extensible framework that unifies data ingestion, cohort curation, processing workflows and result inspection under a common user interface. By bringing the algorithm to the data, it enables institutions to keep control over their sensitive data while still participating in distributed experimentation and model development. By integrating flexible workflow orchestration with user-facing applications for researchers, Kaapana reduces technical overhead, improves reproducibility and enables conducting large-scale, collaborative, multi-centre imaging studies. We describe the core concepts of the platform and illustrate how they can support diverse use cases, from local prototyping to nation-wide research networks. The open-source codebase is available at https://github.com/kaapana/kaapana

