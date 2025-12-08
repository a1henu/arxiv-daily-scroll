---
layout: default
title: UG-FedDA: Uncertainty-Guided Federated Domain Adaptation for Multi-Center Alzheimer's Disease Detection
---

# UG-FedDA: Uncertainty-Guided Federated Domain Adaptation for Multi-Center Alzheimer's Disease Detection
**arXiv**：[2512.05814v1](https://arxiv.org/abs/2512.05814) · [PDF](https://arxiv.org/pdf/2512.05814.pdf)  
**作者**：Fubao Zhu, Zhanyuan Jia, Zhiguo Wang, Huan Huang, Danyang Sun, Chuang Han, Yanting Li, Jiaofen Nan, Chen Zhao, Weihua Zhou  

**一句话要点**：提出不确定性引导的联邦域适应框架，以解决多中心阿尔茨海默病检测中的站点异质性和隐私保护问题。

**关键词**：联邦学习, 域适应, 不确定性量化, 阿尔茨海默病检测, 多中心研究, 磁共振成像

## 3 点简述
- 核心问题：多中心研究中站点间异质性导致分类模型鲁棒性不足，且缺乏不确定性量化机制。
- 方法要点：结合不确定性量化与联邦域适应，通过自注意力变换器提取多模板ROI特征，并降权不确定样本以对齐特征分布。
- 实验或效果：在ADNI、AIBL和OASIS数据集上，UG-FedDA在AD vs. NC等任务中实现跨域性能提升，如AD vs. NC准确率达90.54%（ADNI）。

## 摘要（原文）

> Alzheimer's disease (AD) is an irreversible neurodegenerative disorder, and early diagnosis is critical for timely intervention. However, most existing classification frameworks face challenges in multicenter studies, as they often neglect inter-site heterogeneity and lack mechanisms to quantify uncertainty, which limits their robustness and clinical applicability. To address these issues, we proposed Uncertainty-Guided Federated Domain Adaptation (UG-FedDA), a novel multicenter AD classification framework that integrates uncertainty quantification (UQ) with federated domain adaptation to handle cross-site structure magnetic resonance imaging (MRI) heterogeneity under privacy constraints. Our approach extracts multi-template region-of-interest (RoI) features using a self-attention transformer, capturing both regional representations and their interactions. UQ is integrated to guide feature alignment, mitigating source-target distribution shifts by down-weighting uncertain samples. Experiments are conducted on three public datasets: the Alzheimer's Disease Neuroimaging Initiative (ADNI), the Australian Imaging, Biomarkers and Lifestyle study (AIBL), and the Open Access Series of Imaging Studies (OASIS). UG-FedDA achieved consistent cross-domain improvements in accuracy, sensitivity, and area under the ROC curve across three classification tasks: AD vs. normal controls (NC), mild cognitive impairment (MCI) vs. AD, and NC vs. MCI. For NC vs. AD, UG-FedDA achieves accuracies of 90.54%, 89.04%, and 77.78% on ADNI, AIBL and OASIS datasets, respectively. For MCI vs. AD, accuracies are 80.20% (ADNI), 71.91% (AIBL), and 79.73% (OASIS). For NC vs. MCI, results are 76.87% (ADNI), 73.91% (AIBL), and 83.73% (OASIS). These results demonstrate that the proposed framework not only adapts efficiently across multiple sites but also preserves strict privacy.

