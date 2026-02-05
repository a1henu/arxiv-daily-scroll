---
layout: default
title: Aortic Valve Disease Detection from PPG via Physiology-Informed Self-Supervised Learning
---

# Aortic Valve Disease Detection from PPG via Physiology-Informed Self-Supervised Learning
**arXiv**：[2602.04266v1](https://arxiv.org/abs/2602.04266) · [PDF](https://arxiv.org/pdf/2602.04266.pdf)  
**作者**：Jiaze Wang, Qinghao Zhao, Zizheng Chen, Zhejun Sun, Deyun Zhang, Yuxi Zhou, Shenda Hong  

**一句话要点**：提出生理引导自监督学习框架，利用大规模无标签PPG数据解决主动脉瓣疾病筛查中的标签稀缺问题。

**关键词**：自监督学习, 光电容积描记术, 主动脉瓣疾病筛查, 生理引导学习, 数字生物标志物, 医疗人工智能

## 3 点简述
- 核心问题：主动脉瓣疾病传统诊断依赖超声心动图，成本高且专业性强，而PPG数据标签极度稀缺限制数据驱动方法。
- 方法要点：基于临床知识定义PPG形态表型，构建脉冲模式识别代理任务进行自监督预训练，采用双分支门控融合架构进行微调。
- 实验或效果：在超过17万无标签PPG样本上预训练，AS和AR筛查AUC分别达0.765和0.776，显著优于监督基线，模型输出验证为独立数字生物标志物。

## 摘要（原文）

> Traditional diagnosis of aortic valve disease relies on echocardiography, but its cost and required expertise limit its use in large-scale early screening. Photoplethysmography (PPG) has emerged as a promising screening modality due to its widespread availability in wearable devices and its ability to reflect underlying hemodynamic dynamics. However, the extreme scarcity of gold-standard labeled PPG data severely constrains the effectiveness of data-driven approaches. To address this challenge, we propose and validate a new paradigm, Physiology-Guided Self-Supervised Learning (PG-SSL), aimed at unlocking the value of large-scale unlabeled PPG data for efficient screening of Aortic Stenosis (AS) and Aortic Regurgitation (AR). Using over 170,000 unlabeled PPG samples from the UK Biobank, we formalize clinical knowledge into a set of PPG morphological phenotypes and construct a pulse pattern recognition proxy task for self-supervised pre-training. A dual-branch, gated-fusion architecture is then employed for efficient fine-tuning on a small labeled subset. The proposed PG-SSL framework achieves AUCs of 0.765 and 0.776 for AS and AR screening, respectively, significantly outperforming supervised baselines trained on limited labeled data. Multivariable analysis further validates the model output as an independent digital biomarker with sustained prognostic value after adjustment for standard clinical risk factors. This study demonstrates that PG-SSL provides an effective, domain knowledge-driven solution to label scarcity in medical artificial intelligence and shows strong potential for enabling low-cost, large-scale early screening of aortic valve disease.

