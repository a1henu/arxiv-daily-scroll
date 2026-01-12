---
layout: default
title: Cedalion Tutorial: A Python-based framework for comprehensive analysis of multimodal fNIRS & DOT from the lab to the everyday world
---

# Cedalion Tutorial: A Python-based framework for comprehensive analysis of multimodal fNIRS & DOT from the lab to the everyday world
**arXiv**：[2601.05923v1](https://arxiv.org/abs/2601.05923) · [PDF](https://arxiv.org/pdf/2601.05923.pdf)  
**作者**：E. Middell, L. Carlton, S. Moradi, T. Codina, T. Fischer, J. Cutler, S. Kelley, J. Behrendt, T. Dissanayake, N. Harmening, M. A. Yücel, D. A. Boas, A. von Lühmann  

**一句话要点**：提出Cedalion框架以统一多模态fNIRS/DOT分析，支持从实验室到日常世界的可复现、可扩展工作流。

**关键词**：功能性近红外光谱, 扩散光学断层扫描, 多模态神经影像, 可复现分析, 机器学习集成, Python框架

## 3 点简述
- 当前fNIRS/DOT分析工具碎片化，限制可复现性和与机器学习工作流的集成。
- Cedalion基于Python，整合正向建模、信号处理、GLM分析、DOT重建和机器学习方法。
- 提供七个可执行笔记本演示核心功能，支持SNIRF/BIDS标准、云执行和容器化工作流。

## 摘要（原文）

> Functional near-infrared spectroscopy (fNIRS) and diffuse optical tomography (DOT) are rapidly evolving toward wearable, multimodal, and data-driven, AI-supported neuroimaging in the everyday world. However, current analytical tools are fragmented across platforms, limiting reproducibility, interoperability, and integration with modern machine learning (ML) workflows. Cedalion is a Python-based open-source framework designed to unify advanced model-based and data-driven analysis of multimodal fNIRS and DOT data within a reproducible, extensible, and community-driven environment. Cedalion integrates forward modelling, photogrammetric optode co-registration, signal processing, GLM Analysis, DOT image reconstruction, and ML-based data-driven methods within a single standardized architecture based on the Python ecosystem. It adheres to SNIRF and BIDS standards, supports cloud-executable Jupyter notebooks, and provides containerized workflows for scalable, fully reproducible analysis pipelines that can be provided alongside original research publications. Cedalion connects established optical-neuroimaging pipelines with ML frameworks such as scikit-learn and PyTorch, enabling seamless multimodal fusion with EEG, MEG, and physiological data. It implements validated algorithms for signal-quality assessment, motion correction, GLM modelling, and DOT reconstruction, complemented by modules for simulation, data augmentation, and multimodal physiology analysis. Automated documentation links each method to its source publication, and continuous-integration testing ensures robustness. This tutorial paper provides seven fully executable notebooks that demonstrate core features. Cedalion offers an open, transparent, and community extensible foundation that supports reproducible, scalable, cloud- and ML-ready fNIRS/DOT workflows for laboratory-based and real-world neuroimaging.

