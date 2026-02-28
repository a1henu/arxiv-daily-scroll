---
layout: default
title: PGVMS: A Prompt-Guided Unified Framework for Virtual Multiplex IHC Staining with Pathological Semantic Learning
---

# PGVMS: A Prompt-Guided Unified Framework for Virtual Multiplex IHC Staining with Pathological Semantic Learning
**arXiv**：[2602.23292v1](https://arxiv.org/abs/2602.23292) · [PDF](https://arxiv.org/pdf/2602.23292.pdf)  
**作者**：Fuqiang Chen, Ranran Zhang, Wanming Hu, Deboch Eyob Abera, Yue Peng, Boyun Zheng, Yiwen Sun, Jing Cai, Wenjian Qin  

**一句话要点**：提出PGVMS框架以解决虚拟多重IHC染色中的语义指导不足、分布不一致和空间错位问题。

**关键词**：虚拟多重IHC染色, 病理语义学习, 提示引导框架, 蛋白质感知学习, 原型一致学习, 自适应提示机制

## 3 点简述
- 核心问题：虚拟多重IHC染色面临语义指导不足、染色分布不一致和空间错位三大挑战。
- 方法要点：采用自适应提示引导机制、蛋白质感知学习策略和原型一致学习策略。
- 实验或效果：未知，但框架旨在通过仅使用单重训练数据提升染色准确性和一致性。

## 摘要（原文）

> Immunohistochemical (IHC) staining enables precise molecular profiling of protein expression, with over 200 clinically available antibody-based tests in modern pathology. However, comprehensive IHC analysis is frequently limited by insufficient tissue quantities in small biopsies. Therefore, virtual multiplex staining emerges as an innovative solution to digitally transform H&E images into multiple IHC representations, yet current methods still face three critical challenges: (1) inadequate semantic guidance for multi-staining, (2) inconsistent distribution of immunochemistry staining, and (3) spatial misalignment across different stain modalities. To overcome these limitations, we present a prompt-guided framework for virtual multiplex IHC staining using only uniplex training data (PGVMS). Our framework introduces three key innovations corresponding to each challenge: First, an adaptive prompt guidance mechanism employing a pathological visual language model dynamically adjusts staining prompts to resolve semantic guidance limitations (Challenge 1). Second, our protein-aware learning strategy (PALS) maintains precise protein expression patterns by direct quantification and constraint of protein distributions (Challenge 2). Third, the prototype-consistent learning strategy (PCLS) establishes cross-image semantic interaction to correct spatial misalignments (Challenge 3).

