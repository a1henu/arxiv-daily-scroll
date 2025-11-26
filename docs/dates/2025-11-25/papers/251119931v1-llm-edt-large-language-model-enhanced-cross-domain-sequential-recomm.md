---
layout: default
title: LLM-EDT: Large Language Model Enhanced Cross-domain Sequential Recommendation with Dual-phase Training
---

# LLM-EDT: Large Language Model Enhanced Cross-domain Sequential Recommendation with Dual-phase Training
**arXiv**：[2511.19931v1](https://arxiv.org/abs/2511.19931) · [PDF](https://arxiv.org/pdf/2511.19931.pdf)  
**作者**：Ziwei Liu, Qidong Liu, Wanyu Wang, Yejing Wang, Tong Xu, Wei Huang, Chong Chen, Peng Chuan, Xiangyu Zhao  

**一句话要点**：提出LLM-EDT以解决跨域序列推荐中的不平衡和转移问题

**关键词**：跨域序列推荐, 大语言模型增强, 双阶段训练, 用户画像, 项目增强, 推荐系统

## 3 点简述
- 核心问题：跨域序列推荐存在交互不平衡和偏好转移困难，导致预测性能差
- 方法要点：使用可转移项目增强器和双阶段训练策略，结合领域感知用户画像模块
- 实验或效果：在三个公共数据集上验证有效性，代码已开源便于复现

## 摘要（原文）

> Cross-domain Sequential Recommendation (CDSR) has been proposed to enrich user-item interactions by incorporating information from various domains. Despite current progress, the imbalance issue and transition issue hinder further development of CDSR. The former one presents a phenomenon that the interactions in one domain dominate the entire behavior, leading to difficulty in capturing the domain-specific features in the other domain. The latter points to the difficulty in capturing users' cross-domain preferences within the mixed interaction sequence, resulting in poor next-item prediction performance for specific domains. With world knowledge and powerful reasoning ability, Large Language Models (LLMs) partially alleviate the above issues by performing as a generator and an encoder. However, current LLMs-enhanced CDSR methods are still under exploration, which fail to recognize the irrelevant noise and rough profiling problems. Thus, to make peace with the aforementioned challenges, we proposed an LLMs Enhanced Cross-domain Sequential Recommendation with Dual-phase Training ({LLM-EDT}). To address the imbalance issue while introducing less irrelevant noise, we first propose the transferable item augmenter to adaptively generate possible cross-domain behaviors for users. Then, to alleviate the transition issue, we introduce a dual-phase training strategy to empower the domain-specific thread with a domain-shared background. As for the rough profiling problem, we devise a domain-aware profiling module to summarize the user's preference in each domain and adaptively aggregate them to generate comprehensive user profiles. The experiments on three public datasets validate the effectiveness of our proposed LLM-EDT. To ease reproducibility, we have released the detailed code online at {https://anonymous.4open.science/r/LLM-EDT-583F}.

