---
layout: default
title: SelvaMask: Segmenting Trees in Tropical Forests and Beyond
---

# SelvaMask: Segmenting Trees in Tropical Forests and Beyond
**arXiv**：[2602.02426v1](https://arxiv.org/abs/2602.02426) · [PDF](https://arxiv.org/pdf/2602.02426.pdf)  
**作者**：Simon-Olivier Duguay, Hugo Baudchon, Etienne Laliberté, Helene Muller-Landau, Gonzalo Rivas-Torres, Arthur Ouaknine  

**一句话要点**：提出SelvaMask数据集与检测-分割流程，以提升热带森林树冠分割精度

**关键词**：树冠分割, 热带森林, 视觉基础模型, 检测-分割流程, 数据集标注

## 3 点简述
- 热带森林树冠分割精度低，现有方法在密集环境中表现不佳
- 引入包含8800个标注树冠的SelvaMask数据集，并基于视觉基础模型构建模块化检测-分割流程
- 在热带和温带数据集上验证，达到最先进性能，优于零样本和全监督方法

## 摘要（原文）

> Tropical forests harbor most of the planet's tree biodiversity and are critical to global ecological balance. Canopy trees in particular play a disproportionate role in carbon storage and functioning of these ecosystems. Studying canopy trees at scale requires accurate delineation of individual tree crowns, typically performed using high-resolution aerial imagery. Despite advances in transformer-based models for individual tree crown segmentation, performance remains low in most forests, especially tropical ones. To this end, we introduce SelvaMask, a new tropical dataset containing over 8,800 manually delineated tree crowns across three Neotropical forest sites in Panama, Brazil, and Ecuador. SelvaMask features comprehensive annotations, including an inter-annotator agreement evaluation, capturing the dense structure of tropical forests and highlighting the difficulty of the task. Leveraging this benchmark, we propose a modular detection-segmentation pipeline that adapts vision foundation models (VFMs), using domain-specific detection-prompter. Our approach reaches state-of-the-art performance, outperforming both zero-shot generalist models and fully supervised end-to-end methods in dense tropical forests. We validate these gains on external tropical and temperate datasets, demonstrating that SelvaMask serves as both a challenging benchmark and a key enabler for generalized forest monitoring. Our code and dataset will be released publicly.

