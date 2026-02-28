---
layout: default
title: SPM-Bench: Benchmarking Large Language Models for Scanning Probe Microscopy
---

# SPM-Bench: Benchmarking Large Language Models for Scanning Probe Microscopy
**arXiv**：[2602.22971v1](https://arxiv.org/abs/2602.22971) · [PDF](https://arxiv.org/pdf/2602.22971.pdf)  
**作者**：Peiyao Xiao, Xiaogang Li, Chengliang Xu, Jiayi Wang, Ben Wang, Zichao Chen, Zeyu Wang, Kejun Yu, Yueqian Chen, Xulin Liu, Wende Xiao, Bing Zhao, Hu Wei  

**一句话要点**：提出SPM-Bench基准以评估大语言模型在扫描探针显微镜领域的专业能力

**关键词**：扫描探针显微镜, 多模态基准, 自动化数据合成, 模型评估指标, 科学领域AI

## 3 点简述
- 现有基准在专业科学领域存在数据污染、复杂度不足和人力成本高的问题
- 通过自动化数据合成管道和Anchor-Gated Sieve技术，从论文中高效提取高质量图像-文本对
- 引入SIP-F1分数评估模型性能，并量化模型个性以揭示AI在复杂物理场景中的推理边界

## 摘要（原文）

> As LLMs achieved breakthroughs in general reasoning, their proficiency in specialized scientific domains reveals pronounced gaps in existing benchmarks due to data contamination, insufficient complexity, and prohibitive human labor costs. Here we present SPM-Bench, an original, PhD-level multimodal benchmark specifically designed for scanning probe microscopy (SPM). We propose a fully automated data synthesis pipeline that ensures both high authority and low-cost. By employing Anchor-Gated Sieve (AGS) technology, we efficiently extract high-value image-text pairs from arXiv and journal papers published between 2023 and 2025. Through a hybrid cloud-local architecture where VLMs return only spatial coordinates "llbox" for local high-fidelity cropping, our pipeline achieves extreme token savings while maintaining high dataset purity. To accurately and objectively evaluate the performance of the LLMs, we introduce the Strict Imperfection Penalty F1 (SIP-F1) score. This metric not only establishes a rigorous capability hierarchy but also, for the first time, quantifies model "personalities" (Conservative, Aggressive, Gambler, or Wise). By correlating these results with model-reported confidence and perceived difficulty, we expose the true reasoning boundaries of current AI in complex physical scenarios. These insights establish SPM-Bench as a generalizable paradigm for automated scientific data synthesis.

