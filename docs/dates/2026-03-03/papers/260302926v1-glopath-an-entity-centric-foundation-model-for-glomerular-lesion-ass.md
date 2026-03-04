---
layout: default
title: GloPath: An Entity-Centric Foundation Model for Glomerular Lesion Assessment and Clinicopathological Insights
---

# GloPath: An Entity-Centric Foundation Model for Glomerular Lesion Assessment and Clinicopathological Insights
**arXiv**：[2603.02926v1](https://arxiv.org/abs/2603.02926) · [PDF](https://arxiv.org/pdf/2603.02926.pdf)  
**作者**：Qiming He, Jing Li, Tian Guan, Yifei Ma, Zimo Zhao, Yanxia Wang, Hongjing Chen, Yingming Xu, Shuang Ge, Yexing Zhang, Yizhi Wang, Xinrui Chen, Lianghui Zhu, Yiqing Liu, Qingxia Hou, Shuyan Zhao, Xiaoqin Wang, Lili Ma, Peizhen Hu, Qiang Huang, Zihan Wang, Zhiyuan Shen, Junru Cheng, Siqi Zeng, Jiurun Chen, Zhen Song, Chao He, Zhe Wang, Yonghong He  

**一句话要点**：提出GloPath以解决肾小球病变评估和临床病理关联发现的挑战

**关键词**：肾小球病理学, 基础模型, 自监督学习, 病变评估, 临床病理关联

## 3 点简述
- 核心问题：肾小球形态异质性和细粒度病变模式对AI方法构成挑战。
- 方法要点：基于自监督学习训练实体中心基础模型，使用多尺度多视图数据。
- 实验或效果：在52个任务中超越现有方法，揭示形态与临床指标的显著关联。

## 摘要（原文）

> Glomerular pathology is central to the diagnosis and prognosis of renal diseases, yet the heterogeneity of glomerular morphology and fine-grained lesion patterns remain challenging for current AI approaches. We present GloPath, an entity-centric foundation model trained on over one million glomeruli extracted from 14,049 renal biopsy specimens using multi-scale and multi-view self-supervised learning. GloPath addresses two major challenges in nephropathology: glomerular lesion assessment and clinicopathological insights discovery. For lesion assessment, GloPath was benchmarked across three independent cohorts on 52 tasks, including lesion recognition, grading, few-shot classification, and cross-modality diagnosis-outperforming state-of-the-art methods in 42 tasks (80.8%). In the large-scale real-world study, it achieved an ROC-AUC of 91.51% for lesion recognition, demonstrating strong robustness in routine clinical settings. For clinicopathological insights, GloPath systematically revealed statistically significant associations between glomerular morphological parameters and clinical indicators across 224 morphology-clinical variable pairs, demonstrating its capacity to connect tissue-level pathology with patient-level outcomes. Together, these results position GloPath as a scalable and interpretable platform for glomerular lesion assessment and clinicopathological discovery, representing a step toward clinically translatable AI in renal pathology.

