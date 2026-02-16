---
layout: default
title: Dual-Phase Cross-Modal Contrastive Learning for CMR-Guided ECG Representations for Cardiovascular Disease Assessment
---

# Dual-Phase Cross-Modal Contrastive Learning for CMR-Guided ECG Representations for Cardiovascular Disease Assessment
**arXiv**：[2602.12883v1](https://arxiv.org/abs/2602.12883) · [PDF](https://arxiv.org/pdf/2602.12883.pdf)  
**作者**：Laura Alvarez-Florez, Angel Bujalance-Gomez, Femke Raijmakers, Samuel Ruiperez-Campillo, Maarten Z. H. Kolk, Jesse Wiers, Julia Vogt, Erik J. Bekkers, Ivana Išgum, Fleur V. Y. Tjong  

**一句话要点**：提出双阶段跨模态对比学习框架，利用CMR指导ECG表征以改善心血管疾病评估。

**关键词**：跨模态对比学习, 心脏磁共振成像, 心电图表征, 心血管疾病评估, 双阶段对齐, 共享潜在空间

## 3 点简述
- 核心问题：ECG在心脏结构和功能评估上受限，而CMR虽详细但可及性低，需提升ECG的临床相关性。
- 方法要点：通过双阶段对比损失，在共享潜在空间中将ECG与3D CMR的舒张末期和收缩末期相位对齐。
- 实验或效果：在UK Biobank数据上，功能参数提取提升9.2%，临床预测改进0.7%，代码已公开。

## 摘要（原文）

> Cardiac magnetic resonance imaging (CMR) offers detailed evaluation of cardiac structure and function, but its limited accessibility restricts use to selected patient populations. In contrast, the electrocardiogram (ECG) is ubiquitous and inexpensive, and provides rich information on cardiac electrical activity and rhythm, yet offers limited insight into underlying cardiac structure and mechanical function. To address this, we introduce a contrastive learning framework that improves the extraction of clinically relevant cardiac phenotypes from ECG by learning from paired ECG-CMR data. Our approach aligns ECG representations with 3D CMR volumes at end-diastole (ED) and end-systole (ES), with a dual-phase contrastive loss to anchor each ECG jointly with both cardiac phases in a shared latent space. Unlike prior methods limited to 2D CMR representations with or without a temporal component, our framework models 3D anatomy at both ED and ES phases as distinct latent representations, enabling flexible disentanglement of structural and functional cardiac properties. Using over 34,000 ECG-CMR pairs from the UK Biobank, we demonstrate improved extraction of image-derived phenotypes from ECG, particularly for functional parameters ($\uparrow$ 9.2\%), while improvements in clinical outcome prediction remained modest ($\uparrow$ 0.7\%). This strategy could enable scalable and cost-effective extraction of image-derived traits from ECG. The code for this research is publicly available.

