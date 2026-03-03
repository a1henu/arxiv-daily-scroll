---
layout: default
title: OpenRad: a Curated Repository of Open-access AI models for Radiology
---

# OpenRad: a Curated Repository of Open-access AI models for Radiology
**arXiv**：[2603.02062v1](https://arxiv.org/abs/2603.02062) · [PDF](https://arxiv.org/pdf/2603.02062.pdf)  
**作者**：Konstantinos Vrettos, Galini Papadaki, Emmanouil Brilakis, Matthaios Triantafyllou, Dimitrios Leventis, Despina Staraki, Maria Mavroforou, Eleftherios Tzanis, Konstantina Giouroukou, Michail E. Klontzas  

**一句话要点**：提出OpenRad以解决放射学AI模型分散问题，提供标准化开放访问资源库。

**关键词**：放射学AI模型库, 模型标准化, 开放访问资源, LLM辅助提取, 多模态成像, 社区贡献

## 3 点简述
- 核心问题：放射学AI模型分散，限制可发现性、可重复性和临床转化。
- 方法要点：创建OpenRad，基于文献回顾和LLM提取，手动验证模型记录。
- 实验或效果：包含约1700个模型，覆盖所有成像模态，CNN和Transformer架构占主导。

## 摘要（原文）

> The rapid developments in artificial intelligence (AI) research in radiology have produced numerous models that are scattered across various platforms and sources, limiting discoverability, reproducibility and clinical translation. Herein, OpenRad was created, a curated, standardized, open-access repository that aggregates radiology AI models and providing details such as the availability of pretrained weights and interactive applications. Retrospective analysis of peer reviewed literature and preprints indexed in PubMed, arXiv and Scopus was performed until Dec 2025 (n = 5239 records). Model records were generated using a locally hosted LLM (gpt-oss:120b), based on the RSNA AI Roadmap JSON schema, and manually verified by ten expert reviewers. Stability of LLM outputs was assessed on 225 randomly selected papers using text similarity metrics. A total of 1694 articles were included after review. Included models span all imaging modalities (CT, MRI, X-ray, US) and radiology subspecialties. Automated extraction demonstrated high stability for structured fields (Levenshtein ratio > 90%), with 78.5% of record edits being characterized as minor during expert review. Statistical analysis of the repository revealed CNN and transformer architectures as dominant, while MRI was the most commonly used modality (in 621 neuroradiology AI models). Research output was mostly concentrated in China and the United States. The OpenRad web interface enables model discovery via keyword search and filters for modality, subspecialty, intended use, verification status and demo availability, alongside live statistics. The community can contribute new models through a dedicated portal. OpenRad contains approx. 1700 open access, curated radiology AI models with standardized metadata, supplemented with analysis of code repositories, thereby creating a comprehensive, searchable resource for the radiology community.

