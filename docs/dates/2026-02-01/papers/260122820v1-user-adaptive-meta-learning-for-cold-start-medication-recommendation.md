---
layout: default
title: User-Adaptive Meta-Learning for Cold-Start Medication Recommendation with Uncertainty Filtering
---

# User-Adaptive Meta-Learning for Cold-Start Medication Recommendation with Uncertainty Filtering
**arXiv**：[2601.22820v1](https://arxiv.org/abs/2601.22820) · [PDF](https://arxiv.org/pdf/2601.22820.pdf)  
**作者**：Arya Hadizadeh Moghaddam, Mohsen Nayebi Kerdabadi, Dongjie Wang, Mei Liu, Zijun Yao  

**一句话要点**：提出MetaDrug框架，通过元学习和不确定性过滤解决患者冷启动药物推荐问题。

**关键词**：药物推荐, 患者冷启动, 元学习, 不确定性量化, 电子健康记录, 个性化医疗

## 3 点简述
- 核心问题：现有方法难以处理患者冷启动，因新患者缺乏足够处方历史，导致推荐不可靠。
- 方法要点：采用两级元适应机制，结合自适应和同伴适应，并引入不确定性量化模块过滤无关信息。
- 实验或效果：在MIMIC-III和AKI数据集上验证，MetaDrug在冷启动患者上优于现有方法。

## 摘要（原文）

> Large-scale Electronic Health Record (EHR) databases have become indispensable in supporting clinical decision-making through data-driven treatment recommendations. However, existing medication recommender methods often struggle with a user (i.e., patient) cold-start problem, where recommendations for new patients are usually unreliable due to the lack of sufficient prescription history for patient profiling. While prior studies have utilized medical knowledge graphs to connect medication concepts through pharmacological or chemical relationships, these methods primarily focus on mitigating the item cold-start issue and fall short in providing personalized recommendations that adapt to individual patient characteristics. Meta-learning has shown promise in handling new users with sparse interactions in recommender systems. However, its application to EHRs remains underexplored due to the unique sequential structure of EHR data. To tackle these challenges, we propose MetaDrug, a multi-level, uncertainty-aware meta-learning framework designed to address the patient cold-start problem in medication recommendation. MetaDrug proposes a novel two-level meta-adaptation mechanism, including self-adaptation, which adapts the model to new patients using their own medical events as support sets to capture temporal dependencies; and peer-adaptation, which adapts the model using similar visits from peer patients to enrich new patient representations. Meanwhile, to further improve meta-adaptation outcomes, we introduce an uncertainty quantification module that ranks the support visits and filters out the unrelated information for adaptation consistency. We evaluate our approach on the MIMIC-III and Acute Kidney Injury (AKI) datasets. Experimental results on both datasets demonstrate that MetaDrug consistently outperforms state-of-the-art medication recommendation methods on cold-start patients.

